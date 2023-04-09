# slack_tokumeisan

## 概要説明

slackでの匿名投稿ツールです。
どこから入力しても特定チャネルに匿名で投稿されるので、自分のチャネルで入力すれば入力中表示もされません。

## 環境変数

docker-compose.ymlと同じディレクトリに`.env`を設置して下さい

```console
SLACK_APP_TOKEN=[App-Level Tokens: xapp-で始まる文字列]
SLACK_BOT_TOKEN=[Bot User OAuth Token: xoxb-で始まる文字列]
CHANNEL_ID=[匿名投稿先チャネルID: Cで始まる12桁英数文字]
```

## コマンド
