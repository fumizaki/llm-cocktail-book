# LLM Cocktail Book - WebAPI

## Overview

### 技術スタック

* フレームワーク: FastAPI
* 大規模言語モデル: OpenAI, Anthropic, Google
* メール配信: Resend
* 決済: Stripe

## Externals

# OpenAI

このドキュメントでは、`OpenAI`を利用したアプリケーション開発のセットアップと基本的な使用方法について説明します。

# Anthropic

このドキュメントでは、`Anthropic`を利用したアプリケーション開発のセットアップと基本的な使用方法について説明します。

# Google

このドキュメントでは、`Google`を利用したアプリケーション開発のセットアップと基本的な使用方法について説明します。

# Resend

このドキュメントでは、`Resend`を利用したアプリケーション開発のセットアップと基本的な使用方法について説明します。


# Stripe

## 概要

このドキュメントでは、`Stripe`を利用したアプリケーション開発のセットアップと基本的な使用方法について説明します。

## セットアップ

### サインアップ/サインイン

`Stripe`アカウントを作成またはログインします。

* [サインアップ](https://dashboard.stripe.com/register)
* [サインイン](https://dashboard.stripe.com/login)

### APIキー

APIキーは、`Stripe API`を使用するために必要な認証情報です。テスト環境と本番環境で異なるキーを使用します。

* [テスト環境のAPIキー](https://dashboard.stripe.com/test/apikeys)

### Webhook

`Webhook`は、`Stripe`で発生したイベントをリアルタイムにアプリケーションに通知する仕組みです。

1. **Stripe CLIのインストール:**

   ```bash
   brew install stripe/stripe-cli/stripe
   ```

2. **Stripe CLIでログイン:**

    ```bash
    stripe login --api-key sk_test_your_secret_key # テスト環境のシークレットキー
    ```

3. **Webhookの転送設定:**

    ```bash
    stripe listen --forward-to http://localhost:8000/stripe/webhook
    ```
    このコマンドを実行すると、`Stripe`からの`Webhook`イベントが`http://localhost:8000/stripe/webhook`に転送されます。

4. **Webhookイベントのトリガー:**

    ```bash
    stripe trigger payment_intent.succeeded
    ```
    このコマンドを実行すると、`payment_intent.succeeded`イベントがトリガーされ、設定した`URL`に送信されます。