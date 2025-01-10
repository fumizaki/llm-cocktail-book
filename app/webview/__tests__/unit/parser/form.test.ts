import { describe, it, expect } from 'vitest';
import { parseFormDataToObject } from '@/lib/parse-form';

describe('parseFormDataToObject', () => {
    it('should parse simple form data', () => {
        const formData = new FormData();
        formData.append('name', 'John Doe');
        formData.append('age', '30');

        expect(parseFormDataToObject(formData)).toEqual({ name: 'John Doe', age: '30' });
    });

    it('should parse nested object form data', () => {
        const formData = new FormData();
        formData.append('address.street', '123 Main St');
        formData.append('address.city', 'Anytown');

        expect(parseFormDataToObject(formData)).toEqual({ address: { street: '123 Main St', city: 'Anytown' } });
    });

    it('should parse array form data', () => {
        const formData = new FormData();
        formData.append('items[0]', 'Item 1');
        formData.append('items[1]', 'Item 2');
        formData.append('items[2]', 'Item 3');

        expect(parseFormDataToObject(formData)).toEqual({ items: ['Item 1', 'Item 2', 'Item 3'] });
    });

    it('should parse nested object with array form data', () => {
        const formData = new FormData();
        formData.append('user.addresses[0].street', '123 Main St');
        formData.append('user.addresses[0].city', 'Anytown');
        formData.append('user.addresses[1].street', '456 Oak Ave');
        formData.append('user.addresses[1].city', 'Springfield');

        expect(parseFormDataToObject(formData)).toEqual({
            user: {
                addresses: [
                    { street: '123 Main St', city: 'Anytown' },
                    { street: '456 Oak Ave', city: 'Springfield' },
                ],
            },
        });
    });

    it('should handle duplicate keys as array', () => {
        const formData = new FormData();
        formData.append('tags', 'tag1');
        formData.append('tags', 'tag2');
        formData.append('tags', 'tag3');

        expect(parseFormDataToObject(formData)).toEqual({ tags: ['tag1', 'tag2', 'tag3'] });
    });

    it('should handle mixed nested objects and arrays', () => {
        const formData = new FormData();
        formData.append('products[0].name', 'Product A');
        formData.append('products[0].price', '10');
        formData.append('products[1].name', 'Product B');
        formData.append('products[1].price', '20');
        formData.append('cart.items[0]', 'Item X');
        formData.append('cart.total', '30');

        expect(parseFormDataToObject(formData)).toEqual({
          products: [
            { name: 'Product A', price: '10' },
            { name: 'Product B', price: '20' },
          ],
          cart: { items: ['Item X'], total: '30' },
        });
    });

    it('should handle empty FormData', () => {
        const formData = new FormData();
        expect(parseFormDataToObject(formData)).toEqual({});
    });

    it('should handle array with empty index', () => {
        const formData = new FormData();
        formData.append('items[]', 'Item 1');
        formData.append('items[]', 'Item 2');
        expect(parseFormDataToObject(formData)).toEqual({ items: ['Item 1', 'Item 2']});
    });

     it('should handle array with non-sequential index', () => {
        const formData = new FormData();
        formData.append('items[0]', 'Item 1');
        formData.append('items[2]', 'Item 3');
        expect(parseFormDataToObject(formData)).toEqual({ items: ['Item 1', undefined, 'Item 3']});
    });

    it('should handle number like string', () => {
        const formData = new FormData();
        formData.append('count', '123');
        expect(parseFormDataToObject(formData)).toEqual({ count: '123' });
    })

    it('should handle boolean like string', () => {
        const formData = new FormData();
        formData.append('flag', 'true');
        expect(parseFormDataToObject(formData)).toEqual({ flag: 'true' });
    })

    it('should handle null like string', () => {
        const formData = new FormData();
        formData.append('value', 'null');
        expect(parseFormDataToObject(formData)).toEqual({ value: 'null' });
    })
});