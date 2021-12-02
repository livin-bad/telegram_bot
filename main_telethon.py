from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
# api_id = 12345
# api_hash = '0123456789abcdef0123456789abcdef'

#  tutorial - https://pypi.org/project/Telethon/

# Creating a client
api_id = 11043944
api_hash = '65eaf1b44fb742cdd6c91b1cbdd7d6ba'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Doing stuff
print(client.get_me().__str__())

username = '@ell70_bot'

client.send_message(username, 'Hello! Talking to you from Telethon')
# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# client.download_profile_photo('me')
messages = client.get_messages(username)

print(messages)


# messages[0].download_media()

# @client.on(events.NewMessage(pattern='(?i)hi|hello'))
# async def handler(event):
    # await event.respond('Hey!')
    # await event.reply('Hi!')
    # await event.get_chat()d


client.run_until_disconnected()
