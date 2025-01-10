import { describe, it, expect } from 'vitest';
import { z } from 'zod';
import { selectChatbotMessage, insertChatbotMessage } from '@/domain/validation';

// テスト用の MessageRole enum を定義
enum MessageRole {
    User = 'user',
    Assistant = 'assistant',
    System = 'system',
}

// zodのenumを生成
const MessageRoleEnum = z.nativeEnum(MessageRole);

describe('selectChatbotMessage', () => {
    it('should parse with valid data', () => {
        // 有効なデータでパースできること
        const validData = {
            id: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
            chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
            content: '有効なコンテンツ',
            role: MessageRole.User,
        };
        expect(selectChatbotMessage.parse(validData)).toEqual(validData);
    });

    it('should throw an error with invalid ID (not a UUID)', () => {
        // IDがUUIDではない場合にエラーが発生すること
        const invalidData = {
            id: 'invalid-uuid',
            chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
            content: 'コンテンツ',
            role: MessageRole.User,
        };
        expect(() => selectChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with invalid chatbotId (not a UUID)', () => {
        // chatbotIdがUUIDではない場合にエラーが発生すること
        const invalidData = {
            id: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
            chatbotId: 'invalid-chatbot-uuid',
            content: 'コンテンツ',
            role: MessageRole.User,
        };
        expect(() => selectChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with empty content', () => {
        // コンテンツが空の場合にエラーが発生すること
        const invalidData = {
            id: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
            chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
            content: ' ', // 空白のみ
            role: MessageRole.User,
        };
        expect(() => selectChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with invalid role', () => {
        // roleが不正な値の場合にエラーが発生すること
        const invalidData = {
            id: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
            chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
            content: 'コンテンツ',
            role: 'invalid-role', // 不正な値
        };
        expect(() => selectChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });
});

describe('insertChatbotMessage', () => {
    it('should parse with valid data', () => {
        // 有効なデータでパースできること
        const validData = {
            chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
            meta: { llm: 'gpt-3.5-turbo', mode: 'chat' },
            prompt: '有効なプロンプト',
        };
        expect(insertChatbotMessage.parse(validData)).toEqual(validData);
    });

    it('should throw an error with invalid chatbotId (not a UUID)', () => {
        // chatbotIdがUUIDではない場合にエラーが発生すること
        const invalidData = {
            chatbotId: 'invalid-chatbot-uuid',
            meta: { llm: 'gpt-3.5-turbo', mode: 'chat' },
            prompt: 'プロンプト',
        };
        expect(() => insertChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with empty prompt', () => {
        // プロンプトが空の場合にエラーが発生すること
        const invalidData = {
            chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
            meta: { llm: 'gpt-3.5-turbo', mode: 'chat' },
            prompt: ' ', // 空白のみ
        };
        expect(() => insertChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with missing meta', () => {
      // metaがない場合にエラーが発生すること
      const invalidData = {
        chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
        prompt: 'プロンプト',
      };
      expect(() => insertChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with invalid meta format', () => {
      // metaの形式が不正な場合にエラーが発生すること
      const invalidData = {
        chatbotId: 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
        meta: { llm: 123, mode: true }, // llmがnumber, modeがboolean
        prompt: 'プロンプト',
      };
      expect(() => insertChatbotMessage.parse(invalidData)).toThrowError(z.ZodError);
    });
});

