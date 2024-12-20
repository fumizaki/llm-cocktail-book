import { z } from 'zod';
import * as validation from '@/domain/validation';

// Auth
export type AuthToken = z.infer<typeof validation.selectAuthToken>;
export type SignUpRequestParams = z.infer<typeof validation.signUpRequest>;
export type SignInRequestParams = z.infer<typeof validation.signInRequest>;
export type RefreshTokenRequestParams = z.infer<typeof validation.refreshTokenRequest>;


// Chat
export type ChatMessage = z.infer<typeof validation.selectChatMessage>
export type NewChatMessage = z.infer<typeof validation.insertChatMessage>