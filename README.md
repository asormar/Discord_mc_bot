# Jaime – Discord Bot for Consumcraft

A Discord bot designed to manage the **Consumcraft** Minecraft server hosted on FalixNodes.

## Overview

Jaime is a custom bot that helps players access server information quickly and provides direct links to start the server on FalixNodes. It also interacts with users in a friendly way using personalized greetings and visually appealing embeds.

## Features

* **Server Information**: Quickly view the IP and server details
* **Direct Links**: Instant access to start the server on FalixNodes
* **Friendly Interaction**: Responds to personalized greetings
* **Stylish Embeds**: Beautiful, color-coded, and well-formatted messages

## Commands

| Command          | Description                         |
| ---------------- | ----------------------------------- |
| `!ip`            | Display the Minecraft server IP     |
| `!consumcraft`   | Show server info + link to start it |
| `que tal jaime?` | Personalized greeting from the bot  |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/asormar/Discord_Bot.git
cd Discord_Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your_bot_token_here
SUBDOMAIN=consumcraft
URL=consumcraft.falixsrv.me:35253
```

### 4. Run the Bot

```bash
python main.py
```

## Configuration

### Obtaining the Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the **Bot** section
4. Create a bot and copy its token
5. Paste the token into your `.env` file

### Inviting the Bot to Your Server

1. In the Developer Portal, go to **OAuth2 > URL Generator**
2. Select the scope: `bot`
3. Assign the permissions: `Send Messages`, `Embed Links`
4. Use the generated URL to invite the bot to your server

## Project Structure

```
Discord_Bot/
├── main.py              # Main bot code
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included)
├── .gitignore           # Git ignored files
├── README.md            # This file
└── discord.log          # Auto-generated log file
```

## Usage

Once the bot is online on your Discord server:

1. **Check server IP**: `!ip`
2. **Get start link**: `!consumcraft`
3. **Greet the bot**: `que tal jaime?`

## Technologies

* **Python 3.7+**
* **discord.py** – Discord API library
* **python-dotenv** – Environment variable management
* **FalixNodes** – Minecraft server hosting

## Notes

This project is intended as an exploration of Discord bot capabilities. Jaime will continue to be improved and expanded with new features in the future.
