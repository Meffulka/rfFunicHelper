# Funiculor helper

## What this

Userbot for telegram game 'RF telegram'. Helps partyleaders to avoid encounters with other groups in the caves. Forwarding messages to coordination chat.

## How to run

Use environment or .env

### .env example

```
api_id=<you_telegram_api_id>
api_hash='<you_telegram_api_hash>'
chat_id=<chat_id_for_notify>
nickname=<you_nickname>
```

### Docker

build docker image:

```
docker build -t funicHelper .
```

first run for authorization:

```
docker run -it --network host --name funic_helper -v ${PWD}:/app -e api_id=<you_telegram_api_id> -e api_hash=<you_telegram_api_hash> -e chat_id=<chat_id_for_notify> -e nickname=<you_nickname> --rm funic_helper
```

another runs:

```
docker run -d --network host --name funic_helper -v ${PWD}/<you_nickname>.session:/app/<you_nickname>.session -e api_id=<you_telegram_api_id> -e api_hash=<you_telegram_api_hash> -e chat_id=<chat_id_for_notify> -e nickname=<you_nickname> --restart=unless-stopped funic_helper
```

### Local run

```
pip3 install -r requirements.txt
python3 ./main.py
```
