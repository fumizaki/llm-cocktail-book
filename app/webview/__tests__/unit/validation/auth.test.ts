import { describe, it, expect } from 'vitest';
import { z } from 'zod';
import { selectAuthToken, signUpRequest, signInRequest, refreshTokenRequest } from '@/domain/validation'; // your-module.ts など、適切なパスに変更

// テスト用の enum を定義
enum AuthorizationToken {
    Bearer = 'Bearer',
}

enum AuthorizationGrant {
    Password = 'password',
    RefreshToken = 'refresh_token',
}

describe('selectAuthToken', () => {
    it('should parse with valid data', () => {
        // 有効なデータでパースできること
        const validData = {
            accessToken: 'valid_access_token',
            tokenType: AuthorizationToken.Bearer,
            expiresIn: 3600,
            refreshToken: 'valid_refresh_token',
        };
        expect(selectAuthToken.parse(validData)).toEqual(validData);
    });

    it('should parse with optional scope and idToken', () => {
        // オプションの scope と idToken を含むデータでパースできること
        const validData = {
            accessToken: 'valid_access_token',
            tokenType: AuthorizationToken.Bearer,
            expiresIn: 3600,
            refreshToken: 'valid_refresh_token',
            scope: 'openid profile email',
            idToken: 'valid_id_token',
        };
        expect(selectAuthToken.parse(validData)).toEqual(validData);
    });

    it('should throw an error with invalid tokenType', () => {
        // 無効な tokenType でエラーが発生すること
        const invalidData = {
            accessToken: 'valid_access_token',
            tokenType: 'invalid_token_type',
            expiresIn: 3600,
            refreshToken: 'valid_refresh_token',
        };
        expect(() => selectAuthToken.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with negative expiresIn', () => {
        // expiresIn が負の値の場合にエラーが発生すること
        const invalidData = {
            accessToken: 'valid_access_token',
            tokenType: AuthorizationToken.Bearer,
            expiresIn: -1,
            refreshToken: 'valid_refresh_token',
        };
        expect(() => selectAuthToken.parse(invalidData)).toThrowError(z.ZodError);
    });
});

describe('signUpRequest', () => {
    it('should parse with valid data', () => {
        // 有効なデータでパースできること
        const validData = {
            email: 'test@example.com',
            password: 'password123',
        };
        expect(signUpRequest.parse(validData)).toEqual(validData);
    });

    it('should throw an error with invalid email', () => {
        // 無効なメールアドレスでエラーが発生すること
        const invalidData = {
            email: 'invalid-email',
            password: 'password123',
        };
        expect(() => signUpRequest.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with short password', () => {
        // 短すぎるパスワードでエラーが発生すること
        const invalidData = {
            email: 'test@example.com',
            password: 'short',
        };
        expect(() => signUpRequest.parse(invalidData)).toThrowError(z.ZodError);
    });
});

describe('signInRequest', () => {
    it('should parse with valid data', () => {
        // 有効なデータでパースできること
        const validData = {
            email: 'test@example.com',
            password: 'password123',
            grantType: AuthorizationGrant.Password,
        };
        expect(signInRequest.parse(validData)).toEqual(validData);
    });

    it('should parse with optional scope', () => {
        // オプションの scope を含むデータでパースできること
        const validData = {
            email: 'test@example.com',
            password: 'password123',
            grantType: AuthorizationGrant.Password,
            scope: 'openid profile',
        };
        expect(signInRequest.parse(validData)).toEqual(validData);
    });

    it('should throw an error with invalid grantType', () => {
        // 無効な grantType でエラーが発生すること
        const invalidData = {
            email: 'test@example.com',
            password: 'password123',
            grantType: 'invalid_grant_type',
        };
        expect(() => signInRequest.parse(invalidData)).toThrowError(z.ZodError);
    });
});

describe('refreshTokenRequest', () => {
    it('should parse with valid data', () => {
        // 有効なデータでパースできること
        const validData = {
            grantType: AuthorizationGrant.RefreshToken,
            refreshToken: 'valid_refresh_token',
        };
        expect(refreshTokenRequest.parse(validData)).toEqual(validData);
    });

    it('should parse with optional scope', () => {
        // オプションの scope を含むデータでパースできること
        const validData = {
            grantType: AuthorizationGrant.RefreshToken,
            refreshToken: 'valid_refresh_token',
            scope: 'openid profile',
        };
        expect(refreshTokenRequest.parse(validData)).toEqual(validData);
    });

    it('should throw an error with invalid grantType', () => {
        // 無効な grantType でエラーが発生すること
        const invalidData = {
            grantType: 'invalid_grant_type',
            refreshToken: 'valid_refresh_token',
        };
        expect(() => refreshTokenRequest.parse(invalidData)).toThrowError(z.ZodError);
    });

    it('should throw an error with empty refreshToken', () => {
        // refreshToken が空の場合にエラーが発生すること
        const invalidData = {
            grantType: AuthorizationGrant.RefreshToken,
            refreshToken: '',
        };
        expect(() => refreshTokenRequest.parse(invalidData)).toThrowError(z.ZodError);
    });


});