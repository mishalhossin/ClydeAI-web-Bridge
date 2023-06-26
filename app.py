import discord
import selfcord
from discord.ext import commands
import os
from flask import Flask, request, jsonify


app = Flask(__name__)
client = commands.Bot(self_bot=True)
message_to_send = "EMPTY"
thing_to_send = "EMPTY"

@client.event
async def on_ready():
    user = client.get_channel(1122767186642079805)
    await user.send(thing_to_send)
  
@client.event
async def on_message(message):
    global message_to_send
    if message.author.id == 1081004946872352958:
      message_to_send = message.content
      await client.close()
  
@app.route('/chat', methods=['POST'])
async def chat_handler():
    global message_to_send, thing_to_send
    content = request.json.get('content')
    thing_to_send = content
  
    await client.start(os.environ['DISCORD_USER_TOKEN'], bot=False)
  
    while True:
       if  message_to_send != "EMPTY":
         break
         
    current_message = message_to_send
    message_to_send = "EMPTY"
  
    return jsonify({'message': current_message})

@app.route('/')
def root():
    return 'Try doing this curl -X POST -H "Content-Type: application/json" -d \'\{"content": "Hello, this is a test message!"\}\' https://clydeapi.mishal0legit.repl.co/chat'

app.run(host="0.0.0.0", port=80, threaded=True)
