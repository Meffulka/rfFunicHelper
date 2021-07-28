# Funiculor helper

## What this

Userbot for telegram game 'RF telegram'. Helps partyleaders to avoid encounters with other groups in the caves. Forwarding messages to coordination chat.

# How to run

build docker image:

```
docker build -t funicHelper .
```

first run for authorization:

```
docker run -it --network host --name funicHelper -v ${PWD}/<you_nickname>.session:/app/<you_nickname>.session -e api_id=<you_telegram_api_id> -e api_hash=<you_telegram_api_hash> -e chat_id=<chat_id_for_notify> -e nickname=<you_nickname> --rm funicHelper
```

another runs:

```
docker run -d --network host --name funicHelper -v ${PWD}/<you_nickname>.session:/app/<you_nickname>.session -e api_id=<you_telegram_api_id> -e api_hash=<you_telegram_api_hash> -e chat_id=<chat_id_for_notify> -e nickname=<you_nickname> --restart=unless-stopped funicHelper
```