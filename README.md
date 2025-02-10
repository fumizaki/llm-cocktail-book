# LLM Cocktail Book

This is Fullstack Web Application Using LLM.

## Quick Start

### Command
```
make init

# >> Setup Environment variables in `.env*` files

make docker-up
```

### Setup

#### Environment variables

##### Root(`/.env*`)

| key | type | what | ex |
| ---- | ---- | ---- | ---- |
| WEBVIEW_PORT | Required | setting WebView's running Port | 3000 |
| WEBAPI_PORT | Required | setting WebAPI's running Port | 8000 |
| RDB_NAME | Required | setting RDB's Name | rdb |
| RDB_USER | Required | setting RDB's User | rdb |
| RDB_PASSWORD | Required | setting RDB's Password | rdb |
| RDB_PORT | Required | setting RDB's running Port | 5432 |
| KVS_PORT | Required | setting KVS's running Port | 6379 |
| VECTOR_PORT | Required | setting Vector's running Port | 6333 |
|  |  |  |  |

##### WebView(`/app/webview/.env*`)

| key | type | what | ex |
| ---- | ---- | ---- | ---- |
| NODE_ENV | Optional |  | development |
| BASE_URL | Required | setting WebView's running Url | http://webview:3000 |
| API_BASE_URL | Required | setting WebAPI's running Url | http://webapi:8000 |
| AUTH_SECRET | Required |  | added by auth.js >> `npx auth` |
| NEXT_PUBLIC_STRIPE_PUBLIC_KEY | Required | setting Your' Stripe APIKey for Payment | https://stripe.com/ |
|  |  |  |  |

##### WebAPI(`/app/webapi/.env*`)

| key | type | what | ex |
| ---- | ---- | ---- | ---- |
| VIEW_BASE_URL | Required | setting WebView's running Url | http://webview:3000 |
| API_BASE_URL | Required | setting WebAPI's running Url | http://webapi:8000 |
| OAUTH2_ISSUER | Required |  | your-domain |
| OAUTH2_AUDIENCE | Required |  | your-domain |
| OAUTH2_ALGORITHM | Required |  | HS256 |
| OAUTH2_TOKEN_SECRET | Required |  | abcdefghijklmnopqrstuvwxyz1234567890 |
| RDB_HOST | Required | setting RDB's Host | rdb |
| RDB_NAME | Required | setting RDB's Name | rdb |
| RDB_USER | Required | setting RDB's User | rdb |
| RDB_PASSWORD | Required | setting RDB's Password | rdb |
| RDB_PORT | Required | setting RDB's running Port | 5432 |
| KVS_HOST | Required | setting KVS's Host | kvs |
| KVS_PORT | Required | setting KVS's running Port | 6379 |
| VECTOR_HOST | Required | setting Vector's Host | vector |
| VECTOR_PORT | Required | setting Vector's running Port | 6333 |
| EMAIL_FROM_ADDRESS | Required | setting Your' Email Address |  |
| RESEND_API_KEY | Required | setting Your' Resend APIKey for Sending Email | https://resend.com/ |
| STRIPE_SECRET_KEY | Required | setting Your' Stripe SecretKey for Payment | https://stripe.com/ |
| STRIPE_ENDPOINT_SECRET | Required | setting Your' Stripe Endpoint Secret for Payment | https://stripe.com/ |
| OPENAI_API_KEY | Required | setting Your' OpenAI APIKey for LLM | https://platform.openai.com/ |
| GOOGLE_API_KEY | Required | setting Your' Google APIKey for LLM | https://aistudio.google.com/ |
| ANTHROPIC_API_KEY | Required | setting Your' Anthropic APIKey for LLM | https://console.anthropic.com/ |
|  |  |  |  |


## Feature

### 1. Chatbot

One of the core features of this application is a chatbot that leverages multiple Large Language Models (LLMs) to provide an advanced natural language processing-based conversational experience. Users can select the optimal LLM according to their needs and preferences, enabling high-quality communication based on diverse expressions and contextual understanding.


## Deployment

TBD


