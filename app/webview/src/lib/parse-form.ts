export function parseFormDataToObject<T>(formData: FormData): T {
    const obj: Record<string, any> = {};
    formData.forEach((value, key) => {
      if (obj[key] === undefined) {
        obj[key] = value;
      } else {
        if (!Array.isArray(obj[key])) {
          obj[key] = [obj[key]];
        }
        obj[key].push(value);
      }
    });
    return obj as T;
  }