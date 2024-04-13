import discord
import json
import random
import asyncio
import os
import requests
from discord.ext import commands
from discord.enums import ActivityType
import time


def HONEYPOT_3():
    print("[HONEYPOT_3] Establishing connection to bot_instance...")
    time.sleep(0.2)
    print("[HONEYPOT_3] Connection established to bot_instance.")
    time.sleep(0.5)


def load_token_config(file_name):
    with open(os.path.join('Tokens', file_name), 'r') as f:
        print(f"[HONEYPOT_3] Config {file_name} was loaded.")
        return json.load(f)


def load_database(file_name):
    with open(os.path.join('Database', file_name), 'r') as f:
        print(f"[HONEYPOT_3] Config {file_name} was loaded.")
        return json.load(f)


pronouns = load_database('pronouns.json')  # Not directly used in this example
names = load_database('nicknames.json')
images = [os.path.join('Database', 'images', img) for img in load_database('images.json')]
statuses = load_database('status.json')
bios = load_database('about_me.json')  # Added for bio updates
token_data = load_token_config('token_3.json')

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, self_bot=True)


def get_activity(status):
    activity_type = getattr(ActivityType, status.get("type", "").lower(), None)
    if activity_type is None:
        return discord.Game(name=status.get("name"))
    elif activity_type == ActivityType.streaming:
        return discord.Streaming(name=status.get("name"), url=status.get("url"))
    else:
        return discord.Activity(type=activity_type, name=status.get("name"))


def update_bio(token, new_bio):
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": f"Bot {token}"}
    json_data = {"bio": new_bio}
    response = requests.patch(url, headers=headers, json=json_data)
    return response.status_code


async def change_profile():
    while True:
        new_name = random.choice(names)
        new_image_path = random.choice(images)
        new_bio = random.choice(bios)  # Select a new bio

        try:
            await bot.user.edit(username=new_name)
            print(f"[HONEYPOT_3] Changed username to {new_name}")
        except discord.HTTPException as e:
            print(f"[HONEYPOT_3] Failed to change username: {e}")

        try:
            with open(new_image_path, 'rb') as img:
                await bot.user.edit(avatar=img.read())
                print(f"[HONEYPOT_3] Changed avatar image to {new_image_path}")
        except discord.HTTPException as e:
            print(f"[HONEYPOT_3] Failed to change avatar: {e}")

        # Update the bio using the external function
        status_code = update_bio(bot_token, new_bio)
        if status_code != 200:
            print(f"[HONEYPOT_3] Failed to update bio: HTTP {status_code}")

        await asyncio.sleep(random.randint(12 * 3600, 72 * 3600))


async def change_status():
    while True:
        status_info = random.choice(statuses)
        new_status = get_activity(status_info)
        print(f"[HONEYPOT_3] Changed status to {new_status}")
        await bot.change_presence(activity=new_status)
        await asyncio.sleep(random.randint(600, 1800))


@bot.event
async def on_ready():
    print(f'[HONEYPOT_3] Logged in as {bot.user.name}. Changing username...')
    bot.loop.create_task(change_profile())
    print(f'[HONEYPOT_3] Attempting to change avatar and username')
    bot.loop.create_task(change_status())
    print(f'[HONEYPOT_3] Attempting to change status')


@bot.event
async def on_message(message):
    if not message.guild:  # Check if the message is a DM
        # Correctly getting the profile photo URL
        avatar_url = str(message.author.avatar.url if message.author.avatar else None)

        # Construct a log entry string with the desired information
        log_entry_str = f"[HONEYPOT_3] DM Received - Time: {message.created_at}, From: {message.author} (ID: {message.author.id}, Avatar URL: {avatar_url}, Message: {message.content}"
        print(log_entry_str)  # Print the constructed log entry string to the console

        log_entry = {
            "time": str(message.created_at),
            "from": {
                "id": message.author.id,
                "name": str(message.author),
                "avatar_url": avatar_url,
            },
            "message": message.content
        }
        logs_path = os.path.join('Honeypot-Logs', "honeypot_dm_logs_3.json")

        # Load existing logs or initialize an empty list
        if os.path.exists(logs_path) and os.path.getsize(logs_path) > 0:
            with open(logs_path, 'r') as file:
                logs = json.load(file)
        else:
            logs = []

        logs.append(log_entry)

        # Write updated logs to file
        with open(logs_path, 'w') as file:
            json.dump(logs, file, indent=4)

        # Immediately send the log to the specified channel
        await send_dm_log_to_channel(log_entry)

    await bot.process_commands(message)


async def send_dm_log_to_channel(log_entry):
    channel_id = token_data.get('channel_id')
    if not channel_id:
        print("[HONEYPOT_3] Channel ID is not set in token.json.")
        return

    channel = bot.get_channel(int(channel_id))
    if not channel:
        print(f"[HONEYPOT_3] Channel with ID {channel_id} not found.")
        return

    message_content = (
        "## HONEYPOT NO.1 WAS TRIGGERED\n"
        f"- **HONEYPOT NO.1 RUNNING AS: @{bot.user.name}**\n"
        f"- **DATE:** {log_entry['time'][:10]}\n"
        f"- **TIME:** {log_entry['time'][11:19]}\n"
        f"- **USERNAME:** {log_entry['from']['name']}\n"
        f"- **USER ID:** {log_entry['from']['id']}\n"
        f"- **USER AVATAR:** [Link]({log_entry['from']['avatar_url']})\n"
        f"- **MESSAGE CONTENTS:** {log_entry['message']}"
    )
    await channel.send(message_content)


# Use the token from your token.json
bot_token = token_data['token']
bot.run(bot_token)
