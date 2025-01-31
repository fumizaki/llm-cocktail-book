# LLM Cocktail Book - WebAPI

## Overview



## Externals

# Stripe

## 概要

このドキュメントでは、Stripe を利用したアプリケーション開発のセットアップと基本的な使用方法について説明します。

## セットアップ

### サインアップ/サインイン

Stripe アカウントを作成またはログインします。

* [サインアップ](https://dashboard.stripe.com/register)
* [サインイン](https://dashboard.stripe.com/login)

### API キー

API キーは、Stripe API を使用するために必要な認証情報です。テスト環境と本番環境で異なるキーを使用します。

* [テスト環境の API キー](https://dashboard.stripe.com/test/apikeys)

### Webhook

Webhook は、Stripe で発生したイベントをリアルタイムにアプリケーションに通知する仕組みです。

1. **Stripe CLI のインストール:**

   ```bash
   brew install stripe/stripe-cli/stripe
   ```

2. **Stripe CLI でログイン:**

    ```bash
    stripe login --api-key sk_test_your_secret_key # テスト環境のシークレットキー
    ```

3. **Webhook の転送設定:**

    ```bash
    stripe listen --forward-to http://localhost:8000/stripe/webhook
    ```
    このコマンドを実行すると、`Stripe`からの`Webhook`イベントが`http://localhost:8000/stripe/webhook`に転送されます。

4. **Webhook イベントのトリガー:**

    ```bash
    stripe trigger payment_intent.succeeded
    ```
    このコマンドを実行すると、`payment_intent.succeeded`イベントがトリガーされ、設定した`URL`に送信されます。