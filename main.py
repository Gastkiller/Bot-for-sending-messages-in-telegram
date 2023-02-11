import requests  
import json

# Your token from BotFather
bot_token = 'YOUR_TOKEN_BOT'

# Link to submit a request
url = f"https://api.telegram.org/botYOUR_BOT_TOKEN/sendMessage"

# MESSAGE
message = "YOUR_MESSAGE"

# Telegram ID recipients
users_ids = [1234567890, 1485647396, 407978987, 1710150580, 312386286, 934859197, 1236311981, 1725876481, 900918008, 638602506, 820050885, 1183978425, 665747664, 1106416837, 1501523554, 842722347, 1275633721, 960063579, 616243845, 834389577, 733124994, 726911161, 1124468792]

# Sending a request to send a message
for user_id in users_ids:
    data = {
        'chat_id': user_id,
        'text': message
    }

    response = requests.post(url, data=data)
    response_json = response.json()

# Server Response Check
if response_json['ok']:
    print('Message sent to user with ID {}'.format(user_id))
else:
    print('Message sending error: {}'.format(response_json['description']))
