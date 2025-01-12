import { describe, it, expect } from "vitest";
import { parseSnakeToCamel, parseCamelToSnake } from "@/lib/parse-case";

describe("parseSnakeToCamel", () => {
	it("should convert snake_case keys to camelCase in objects", () => {
		expect(parseSnakeToCamel({ snake_case: "value" })).toEqual({
			snakeCase: "value",
		});
		expect(
			parseSnakeToCamel({ nested_object: { another_key: "another_value" } }),
		).toEqual({ nestedObject: { anotherKey: "another_value" } });
		expect(
			parseSnakeToCamel({
				mixed_case: "test",
				number_value: 123,
				bool_value: true,
			}),
		).toEqual({ mixedCase: "test", numberValue: 123, boolValue: true });
	});

	it("should handle arrays correctly", () => {
		expect(parseSnakeToCamel([{ snake_case: "value" }])).toEqual([
			{ snakeCase: "value" },
		]);
		expect(
			parseSnakeToCamel([{ nested_object: { another_key: "another_value" } }]),
		).toEqual([{ nestedObject: { anotherKey: "another_value" } }]);
		expect(
			parseSnakeToCamel([1, "string", true, { test_key: "test" }]),
		).toEqual([1, "string", true, { testKey: "test" }]);
		expect(parseSnakeToCamel([[{ inner_array_object: "value" }]])).toEqual([
			[{ innerArrayObject: "value" }],
		]);
	});
});

describe("parseCamelToSnake", () => {
	it("should convert camelCase keys to snake_case in objects", () => {
		expect(parseCamelToSnake({ camelCase: "value" })).toEqual({
			camel_case: "value",
		});
		expect(
			parseCamelToSnake({ nestedObject: { anotherKey: "another_value" } }),
		).toEqual({ nested_object: { another_key: "another_value" } });
		expect(
			parseCamelToSnake({
				mixedCase: "test",
				numberValue: 123,
				boolValue: true,
			}),
		).toEqual({ mixed_case: "test", number_value: 123, bool_value: true });
	});

	it("should handle arrays correctly", () => {
		expect(parseCamelToSnake([{ camelCase: "value" }])).toEqual([
			{ camel_case: "value" },
		]);
		expect(
			parseCamelToSnake([{ nestedObject: { anotherKey: "another_value" } }]),
		).toEqual([{ nested_object: { another_key: "another_value" } }]);
		expect(parseCamelToSnake([1, "string", true, { testKey: "test" }])).toEqual(
			[1, "string", true, { test_key: "test" }],
		);
		expect(parseCamelToSnake([[{ innerArrayObject: "value" }]])).toEqual([
			[{ inner_array_object: "value" }],
		]);
	});
});
