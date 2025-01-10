type ObjectOrArray = { [key: string]: any } | any[];

// スネークケースの文字列をキャメルケースの文字列に変換
const parseSnakeStrToCamelStr = (str: string): string => {
	return str
		.split("_")
		.map((c, i) => {
			if (i === 0) {
				return c.toLowerCase();
			}
			return c.charAt(0).toUpperCase() + c.slice(1).toLowerCase();
		})
		.join("");
};

// キャメルケースの文字列をスネークケースの文字列に変換
const parseCamelStrToSnakeStr = (str: string): string => {
	return str
		.split(/(?=[A-Z])/)
		.join("_")
		.toLowerCase();
};

// 値の型を判定
const getType = (val: unknown): string => {
	return toString.call(val).slice(8, -1).toLowerCase();
};

// スネークケースからキャメルケースへの変換（配列またはオブジェクト）
export function parseSnakeToCamel<T extends ObjectOrArray>(input: T): T {
	// 配列の場合
	if (Array.isArray(input)) {
		return input.map((item) => {
			const itemType = getType(item);
			if (itemType === "object") {
				return parseSnakeToCamel(item as object);
			}
			if (itemType === "array") {
				return parseSnakeToCamel(item as any[]);
			}
			return item;
		}) as T;
	}

	// オブジェクトの場合
	if (getType(input) === "object") {
		const result = {} as { [key: string]: any };

		Object.entries(input as object).forEach(([key, val]) => {
			const valType = getType(val);
			let parseedVal: any = val;

			if (valType === "object") {
				parseedVal = parseSnakeToCamel(val as object);
			} else if (valType === "array") {
				parseedVal = parseSnakeToCamel(val as any[]);
			}

			result[parseSnakeStrToCamelStr(key)] = parseedVal;
		});

		return result as T;
	}

	return input;
}

// キャメルケースからスネークケースへの変換（配列またはオブジェクト）
export function parseCamelToSnake<T extends ObjectOrArray>(input: T): T {
	// 配列の場合
	if (Array.isArray(input)) {
		return input.map((item) => {
			const itemType = getType(item);
			if (itemType === "object") {
				return parseCamelToSnake(item as object);
			}
			if (itemType === "array") {
				return parseCamelToSnake(item as any[]);
			}
			return item;
		}) as T;
	}

	// オブジェクトの場合
	if (getType(input) === "object") {
		const result = {} as { [key: string]: any };

		Object.entries(input as object).forEach(([key, val]) => {
			const valType = getType(val);
			let parseedVal: any = val;

			if (valType === "object") {
				parseedVal = parseCamelToSnake(val as object);
			} else if (valType === "array") {
				parseedVal = parseCamelToSnake(val as any[]);
			}

			result[parseCamelStrToSnakeStr(key)] = parseedVal;
		});

		return result as T;
	}

	return input;
}
