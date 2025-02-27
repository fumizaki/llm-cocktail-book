/**
 * オブジェクトをFormDataに変換する
 * ネストした構造やファイル、配列をサポート
 * 
 * @param obj 変換元のオブジェクト
 * @param formData 既存のFormData (オプション)
 * @param parentKey 親キー (再帰呼び出し用)
 * @returns FormDataオブジェクト
 */
export function parseObjectToFormData<T extends Record<string, any>>(
	obj: T,
	formData: FormData = new FormData(),
	parentKey: string = ''
  ): FormData {
	for (const key in obj) {
	  if (Object.prototype.hasOwnProperty.call(obj, key)) {
		const value = obj[key];
		const formKey = parentKey ? `${parentKey}.${key}` : key;
  
		// 値の型に応じた処理
		if (value === null || value === undefined) {
		  // null/undefinedは空文字として追加
		  formData.append(formKey, '');
		} else if (isFile(value)) {
		  // Fileオブジェクトはそのまま追加
		  formData.append(formKey, value);
		} else if (isDate(value)) {
		  // Date型はISO文字列に変換
		  formData.append(formKey, value.toISOString());
		} else if (Array.isArray(value)) {
		  // 配列の処理
		  if (value.length === 0) {
			// 空配列の場合は空のインデックスを追加
			formData.append(`${formKey}`, '');
		  } else {
			// 配列要素を処理
			value.forEach((item: any, index: number) => {
			  if (item === null || item === undefined) {
				formData.append(`${formKey}`, '');
			  } else if (typeof item === 'object' && !isFile(item) && !isDate(item) && !isBlob(item)) {
				// オブジェクトは再帰的に処理
				parseObjectToFormData(item, formData, `${formKey}`);
			  } else {
				// プリミティブ値、File、Date、Blobなど
				formData.append(
				  `${formKey}`, 
				  isFile(item) || isBlob(item)
					? item 
					: isDate(item)
					  ? item.toISOString() 
					  : String(item)
				);
			  }
			});
		  }
		} else if (typeof value === 'object' && !isBlob(value)) {
		  // オブジェクトは再帰的に処理 (Blob以外)
		  parseObjectToFormData(value, formData, formKey);
		} else {
		  // その他の値は文字列に変換して追加
		  formData.append(formKey, String(value));
		}
	  }
	}
  
	return formData;
}
  
/**
 * 値がFileオブジェクトかどうかを型安全にチェック
 */
function isFile(value: any): value is File {
	return typeof value === 'object' && value !== null && 
		typeof File !== 'undefined' && value instanceof File;
}
  
/**
 * 値がDateオブジェクトかどうかを型安全にチェック
 */
function isDate(value: any): value is Date {
	return typeof value === 'object' && value !== null && value instanceof Date;
}
  
/**
 * 値がBlobオブジェクトかどうかを型安全にチェック
 */
function isBlob(value: any): value is Blob {
	return typeof value === 'object' && value !== null && 
		typeof Blob !== 'undefined' && value instanceof Blob;
}
  
/**
 * FormDataをオブジェクトに変換する
 * ネストした構造やファイル、配列をサポート
 * 
 * @param T 変換後のオブジェクト
 * @param formData FormData
 * @returns オブジェクト
 */
export function parseFormDataToObject<T>(formData: FormData): T {
	const result: Record<string, any> = {};

	formData.forEach((value, key) => {
		const parts = key.split(".");
		let current = result;

		for (let i = 0; i < parts.length - 1; i++) {
			const part = parts[i];
			const arrayMatch = part.match(/^([^\[]+)\[(\d*)\]$/); // 空のインデックスもキャッチするように変更

			if (arrayMatch) {
				const [, name, index] = arrayMatch;
				current[name] = current[name] || [];

				// indexが空文字列の場合はpushで追加
				if (index === "") {
					current = current[name]; // currentを配列自身に設定
				} else {
					const numIndex = Number.parseInt(index);
					current[name][numIndex] = current[name][numIndex] || {};
					current = current[name][numIndex];
				}
			} else {
				current[part] = current[part] || {};
				current = current[part];
			}
		}

		const lastPart = parts[parts.length - 1];
		const arrayMatch = lastPart.match(/^([^\[]+)\[(\d*)\]$/); // 空のインデックスもキャッチするように変更

		if (arrayMatch) {
			const [, name, index] = arrayMatch;
			current[name] = current[name] || [];

			if (index === "") {
				current[name].push(value instanceof File ? value : value.toString());
			} else {
				const numIndex = Number.parseInt(index);
				current[name][numIndex] = value instanceof File ? value : value.toString();
			}
		} else {
			if (current[lastPart] !== undefined) {
				if (!Array.isArray(current[lastPart])) {
					current[lastPart] = [current[lastPart]];
				}
				current[lastPart].push(value instanceof File ? value : value.toString());
			} else {
				current[lastPart] = value instanceof File ? value : value.toString();
			}
		}
	});

	return result as T;
}

