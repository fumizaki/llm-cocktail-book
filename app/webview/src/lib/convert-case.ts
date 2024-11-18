// スネークケースの文字列をキャメルケースの文字列に変換
const convertSnakeStrToCamelStr = (str: string): string => {
    return str.split('_').map((c, i) => {
        if (i === 0) {
            return c.toLowerCase()
        }
        return c.charAt(0).toUpperCase() + c.slice(1).toLowerCase()
    }).join('')
}

// スネークケースのオブジェクト配列をキャメルケースのオブジェクト配列に変換
const convertSnakeArrayOfObjectsToCamelArrayOfObjects = <T extends object>(array: T[]): T[] => {
    const arrayType = toString.call(array).slice(8, -1).toLowerCase()
    if (arrayType !== 'array') {
      return []
    }
    return array.map((obj) => convertSnakeToCamel(obj))
}

// スネークケースのオブジェクトをキャメルケースのオブジェクトに変換
export const convertSnakeToCamel = <T extends object>(obj: T): T => {
    const result = {} as T
    Object.entries(obj).forEach(([key, val]) => {
        const valType = toString.call(val).slice(8, -1).toLowerCase()
        if (valType === 'object') {
            val = convertSnakeToCamel(val as Record<string, unknown>)
        } else if (valType === 'array') {
            val = convertSnakeArrayOfObjectsToCamelArrayOfObjects(val as Record<string, unknown>[])
        };
        (result as Record<string, unknown>)[convertSnakeStrToCamelStr(key)] = val
    })
    return result
}


// キャメルケースの文字列をスネークケースの文字列に変換
const convertCamelStrToSnakeStr = (str: string): string => {
    return str
        .split(/(?=[A-Z])/)
        .join('_')
        .toLowerCase()
}

// キャメルケースのオブジェクト配列をスネークケースのオブジェクト配列に変換
const convertCamelArrayOfObjectsToSnakeArrayOfObjects = <T extends object>(array: T[]): T[] => {
    return array.map((obj) => convertCamelToSnake(obj))
}

// キャメルケースのオブジェクトをスネークケースのオブジェクトに変換
export const convertCamelToSnake = <T extends object>(obj: T): T => {
    const result = {} as T
    Object.entries(obj).forEach(([key, val]) => {
        const valType = toString.call(val).slice(8, -1).toLowerCase()
        if (valType === 'object') {
            val = convertCamelToSnake(val as Record<string, unknown>)
        } else if (valType === 'array') {
            val = convertCamelArrayOfObjectsToSnakeArrayOfObjects(val as Record<string, unknown>[])
        };
        (result as Record<string, unknown>)[convertCamelStrToSnakeStr(key)] = val
    })
    return result
};