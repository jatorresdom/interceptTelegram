from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

bot_token_2 = "API TOKEN"  # Replace with BotFather token for Bot 2

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received message: {update.message.text}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Your message has been interc")

# Create the application
app = Application.builder().token(bot_token_2).build()

# Add the message handler
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# Start polling
print("Receiver Bot is running...")
app.run_polling()

