from telethon import TelegramClient, events

api_id = "API ID"  # Replace with your API ID
api_hash = "API HASH"  # Replace with your API Hash

# Create a session to monitor messages
client = TelegramClient('interceptor_session', api_id, api_hash)

@client.on(events.NewMessage)
async def intercept_message(event):
    sender = await event.get_sender()
    sender_name = sender.username if sender.username else sender.first_name
    message_text = event.raw_text

    print(f"Intercepted message from {sender_name}: {message_text}")

    # Log the message (simulate data exfiltration)
    with open("intercepted_messages.log", "a") as log_file:
        log_file.write(f"From {sender_name}: {message_text}\n")

client.start()
print("Interceptor is running...")
client.run_until_disconnected()
