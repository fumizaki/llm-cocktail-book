import { describe, it, expect } from "vitest";
import { z } from "zod";
import { selectChatbot, insertChatbot } from "@/domain/validation";

describe("selectChatbot", () => {
	it("should parse with valid data", () => {
		// 有効なデータでパースできること
		const validData = {
			id: "f47ac10b-58cc-4372-a567-0e02b2c3d479", // 有効なUUID
			title: "有効なタイトル",
		};
		expect(selectChatbot.parse(validData)).toEqual(validData);
	});

	it("should throw an error with invalid ID (not a UUID)", () => {
		// 無効なID（UUIDではない）でエラーが発生すること
		const invalidData = {
			id: "invalid-uuid",
			title: "タイトル",
		};
		expect(() => selectChatbot.parse(invalidData)).toThrowError(z.ZodError);
	});

	it("should throw an error with empty title", () => {
		// 空のタイトルでエラーが発生すること
		const invalidData = {
			id: "f47ac10b-58cc-4372-a567-0e02b2c3d479",
			title: " ", // 空白のみの文字列
		};
		expect(() => selectChatbot.parse(invalidData)).toThrowError(z.ZodError);
	});

	it("should throw an error with only whitespace title", () => {
		// 空白のみのタイトルでエラーが発生すること
		const invalidData = {
			id: "f47ac10b-58cc-4372-a567-0e02b2c3d479",
			title: "", // 空文字列
		};
		expect(() => selectChatbot.parse(invalidData)).toThrowError(z.ZodError);
	});
});

describe("insertChatbot", () => {
	it("should parse with valid data", () => {
		// 有効なデータでパースできること
		const validData = {
			title: "有効なタイトル",
		};
		expect(insertChatbot.parse(validData)).toEqual(validData);
	});

	it("should throw an error with empty title", () => {
		// 空のタイトルでエラーが発生すること
		const invalidData = {
			title: " ", // 空白のみの文字列
		};
		expect(() => insertChatbot.parse(invalidData)).toThrowError(z.ZodError);
	});

	it("should throw an error with only whitespace title", () => {
		// 空白のみのタイトルでエラーが発生すること
		const invalidData = {
			title: "", // 空文字列
		};
		expect(() => insertChatbot.parse(invalidData)).toThrowError(z.ZodError);
	});

	it("should parse with Japanese title", () => {
		// 日本語のタイトルでもパースできること
		const validData = {
			title: "日本語のタイトル",
		};
		expect(insertChatbot.parse(validData)).toEqual(validData);
	});

	it("should parse with title containing special characters", () => {
		// 特殊文字を含むタイトルでもパースできること
		const validData = {
			title: "!@#$%^&*()_+=-`~[]{}|;':\",./<>?",
		};
		expect(insertChatbot.parse(validData)).toEqual(validData);
	});

	it("should parse with title containing emojis", () => {
		// 絵文字を含むタイトルでもパースできること
		const validData = {
			title: "絵文字を含むタイトル",
		};
		expect(insertChatbot.parse(validData)).toEqual(validData);
	});
});
