# Rym-Approval

Rym-Approval Bot for accepting new Telegram channel or group join requests.

## 🏷 Environment Variables
Set the following environment variables for the bot to function correctly:
- `API_ID`: Your Telegram API ID. Get it [here](https://my.telegram.org)
- `API_HASH`: Your Telegram API HASH. Get it [here](https://my.telegram.org)
- `BOT_TOKEN`: Your Bot Token. Get it from [BotFather](https://t.me/BotFather)
- `CHID`: Your force subscribe channel ID. Make the bot an admin here.
- `SUDO`: Bot owner's ID(s) for broadcast and stats commands. Use space between multiple IDs.
- `MONGO_URI`: MongoDB database URI.

## Bot Commands

- `/start` - Start the bot and get a welcome message.
- `/users` - Get statistics of users and groups (accessible only by SUDO users).
- `/bcast` - Broadcast a message to all users (accessible only by SUDO users).
- `/fcast` - Forward a message to all users (accessible only by SUDO users).

## Credits

- **[Rym-Official](https://t.me/RymOfficial)**
