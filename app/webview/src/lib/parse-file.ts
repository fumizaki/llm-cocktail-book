export interface Base64File {
    name: string;
    size: number;
    type: string;
    base64: string;
};

const encodeBase64 = (file: File): Promise<Base64File> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();

      reader.onload = () => {
        if (typeof reader.result === 'string') {
          const base64File: Base64File = {
            name: file.name,
            size: file.size,
            type: file.type,
            base64: reader.result.split(',')[1],
          };
          resolve(base64File);
        } else {
          reject(new Error('Failed to read file as base64'));
        }
      };

      reader.onerror = (error) => {
        reject(error);
      };

      reader.readAsDataURL(file);
    });
  };


  export const parseFilesToBase64 = async (files: FileList): Promise<Base64File[]> => {
    return Promise.all(Array.from(files).map((file) => encodeBase64(file)));
}