export const AuthorizationResponse = {
    CODE: 'code',
    TOKEN: 'token',
    ID_TOKEN: 'id_token',
};

export type AuthorizationResponseType = (typeof AuthorizationResponse)[keyof typeof AuthorizationResponse];


export const AuthorizationGrant = {
    AUTHORIZATION_CODE: 'authorization_code',
    PASSWORD: 'password',
    CLIENT_CREDENTIALS: 'client_credentials',
    REFRESH_TOKEN: 'refresh_token',
}

export type AuthorizationGrantType = (typeof AuthorizationGrant)[keyof typeof AuthorizationGrant];


export const AuthorizationToken = {
    BEARER: 'Bearer',
    MAC: 'MAC',
    JWT: 'JWT',
}

export type AuthorizationTokenType = (typeof AuthorizationToken)[keyof typeof AuthorizationToken];


export const MessageRole = {
    USER: 'user',
    ASSISTANT: 'assistant',
    SYSTEM: 'system',
}

export type MessageRoleType = (typeof MessageRole)[keyof typeof MessageRole];
