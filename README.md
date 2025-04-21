
# Welcome Bot for Discord

A simple and customizable bot that welcomes new users to your Discord server. It can send a private welcome message, post a greeting in a designated channel, and assign a specific role to new members.

---

## Features

- Sends a private message to new users upon joining
- Posts a welcome message in a specific channel
- Automatically assigns a role to new users

---

## Intents Setup

To make sure the bot works properly, enable the **Members** privileged intent in your bot's settings:

1. Go to your bot’s application settings on the Discord Developer Portal.
2. Navigate to the “Bot” tab.
3. Scroll down to “Privileged Gateway Intents”.
4. Enable the “Server Members Intent”.

---

## Installation Guide

Make sure Python 3.6 or above is installed on your system before proceeding.

### 🐧 Linux Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MC769/discord-welcome-bot.git
   cd discord-welcome-bot
   ```

2. Update the package list:
   ```bash
   sudo apt update -y
   ```

3. Install Python 3 if not already installed:
   ```bash
   sudo apt install python3
   ```

4. Run the bot:
   ```bash
   python3 welcome-bot.py
   ```

### 🪟 Windows Installation

1. Install the latest version of Python 3 from the official website.
2. Download and extract this repository.
3. Navigate into the extracted folder.
4. Double-click `welcome-bot.py` to run the bot.

---

## Docker Installation (for server/raspberry pi)

### Building the Docker Image

1. Copy the project folder (including the Dockerfile) to your server.
2. Build the image:
   ```bash
   docker build -t welcome-bot .
   ```

3. Verify the image:
   ```bash
   docker images
   ```

### Create and Run the Container

1. Create a container:
   ```bash
   docker create --name welcome-bot welcome-bot
   ```

2. Start the bot:
   ```bash
   docker start welcome-bot
   ```

### Optional: Set Up a Cronjob

To restart the bot every 10 minutes (optional):

1. Edit crontab:
   ```bash
   crontab -e
   ```

2. Add this line:
   ```bash
   */10 * * * * docker stop welcome-bot && docker start welcome-bot
   ```

Use a tool like Crontab Guru if you want to modify the schedule.

---

## Logs

To view real-time logs from the container:

```bash
docker container logs -f welcome-bot
```

---

## Final Step

**Don't forget to replace the placeholder bot token at the bottom of the `welcome-bot.py` file with your actual bot token.**

