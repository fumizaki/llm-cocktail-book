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
				current[name].push(value);
			} else {
				const numIndex = Number.parseInt(index);
				current[name][numIndex] = value;
			}
		} else {
			if (current[lastPart] !== undefined) {
				if (!Array.isArray(current[lastPart])) {
					current[lastPart] = [current[lastPart]];
				}
				current[lastPart].push(value);
			} else {
				current[lastPart] = value;
			}
		}
	});

	return result as T;
}
