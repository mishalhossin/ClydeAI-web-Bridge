# ClydeAI-web-Bridge

![image](https://github.com/mishalhossin/ClydeAI-web-Bridge/assets/91066601/98c9637a-abbe-4aa6-a9ee-8bf4f6e2d4a1)


This is a Flask-based Discord self-bot that allows you to send messages to a clyde on Discord and get response from clyde by making a POST request to the `/chat` endpoint. It uses the discord.py library to interact with the Discord API.

### Prerequisites

Before running the self-bot, make sure you have the following installed:
- Python 3.x
- discord.py-self library
- Flask library

### Installation

1. Clone the repository: `git clone https://github.com/mishalhossin/ClydeAI-web-Bridge`
2. Change into the project directory: `cd ClydeAI-web-Bridge`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set the `DISCORD_USER_TOKEN` environment variable to your Discord user token.

### Usage

To start the self-bot, run the following command:

```
python -m poetry install
python main.py
```

Once the self-bot is running, you can send messages to the specified Discord channel by making a POST request to `http://localhost/chat`. The message content should be in the `content` field of the request body.

### Example

Here is an example using cURL to send a message to the self-bot:

```
curl -X POST -H "Content-Type: application/json" -d '{"content": "Hello, this is a test message!"}' http://localhost/chat
```

Upon receiving the request, the self-bot will send the message to the @Clyde on Discord and return response

### Note

Please be aware that the use of self-bots is against Discord's Terms of Service. Use this self-bot at your own risk, and make sure to comply with Discord's guidelines.
