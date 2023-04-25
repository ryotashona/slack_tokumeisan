# slack_tokumeisan

## 概要説明

slackでの匿名投稿ツールです。
どこから入力しても特定チャネルに匿名で投稿されるので、自分のチャネルで入力すれば入力中表示もされません。

## slack_appの追加/設定
1. https://api.slack.com/apps/ にアクセス
2. [Create New App] > アプリ名、ワークスペースを選択してアプリ作成
3. [Socket Mode] > [Enable Socket Mode] On > [Token Name] 適当に入力 > [Token]をコピー(これが[SLACK_APP_TOKEN])
4. [Slash Commands] > 下記[コマンド]項目のスラッシュコマンドを登録
5. [App Home] > [Your App’s Presence in Slack] > 適当に入力
6. [OAuth & Permissions] > [Bot Token Scopes] > [channels:read][chat:write][reactions:write][users:read]
7. [OAuth & Permissions] > [OAuth Tokens for Your Workspace] > [Install to Workspace] > [許可] > [Bot User OAuth Token]をコピー(これが[SLACK_BOT_TOKEN])
8. Slackで匿名投稿したいチャネルに作成したアプリを追加(チャネルで[/i]を入力したらアプリ追加が表示されると思います)
9. アプリを追加したチャネルの詳細を表示して、下に記載されている[チャネルID]をコピー(これが[CHANNEL_ID])

## 環境変数

docker-compose.ymlと同じディレクトリに`.env`を設置して下さい

```console
SLACK_APP_TOKEN=[App-Level Tokens: xapp-で始まる文字列]
SLACK_BOT_TOKEN=[Bot User OAuth Token: xoxb-で始まる文字列]
CHANNEL_ID=[匿名投稿先チャネルID: Cで始まる12桁英数文字]
```

## コマンド

### 匿名投稿

`/tokumei [投稿コメント]`

CHANNEL_IDで指定したチャネルに[投稿コメント]を匿名アプリ名義で投稿する

### 匿名スタンプ(リアクション)

`/tokumei_stamp [対象投稿URL] [スタンプ(リアクション)]`

CHANNEL_IDで指定したチャネルの[対象投稿URL]に[スタンプ(リアクション)]でリアクションする

### 匿名スレッド返信

`/tokumei_thread [対象投稿URL] [返信コメント]`

CHANNEL_IDで指定したチャネルの[対象投稿URL]に[返信コメント]でスレッド返信する
