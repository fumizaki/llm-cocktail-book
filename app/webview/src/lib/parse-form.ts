export function parseFormDataToObject<T>(formData: FormData): T {
  const result: Record<string, any> = {};

  formData.forEach((value, key) => {
    // キーをドット記法で分割
    const parts = key.split('.');
    let current = result;

    // 最後の要素以外をループ
    for (let i = 0; i < parts.length - 1; i++) {
      const part = parts[i];
      
      // 配列表記 ([0], [1] など) かチェック
      const arrayMatch = part.match(/^([^\[]+)\[(\d+)\]$/);
      
      if (arrayMatch) {
        // 配列の場合
        const [, name, index] = arrayMatch;
        current[name] = current[name] || [];
        current[name][parseInt(index)] = current[name][parseInt(index)] || {};
        current = current[name][parseInt(index)];
      } else {
        // オブジェクトの場合
        current[part] = current[part] || {};
        current = current[part];
      }
    }

    // 最後の部分を処理
    const lastPart = parts[parts.length - 1];
    const arrayMatch = lastPart.match(/^([^\[]+)\[(\d+)\]$/);

    if (arrayMatch) {
      // 配列の最後の要素の場合
      const [, name, index] = arrayMatch;
      current[name] = current[name] || [];
      current[name][parseInt(index)] = value;
    } else {
      // 既存の値がある場合は配列に変換
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