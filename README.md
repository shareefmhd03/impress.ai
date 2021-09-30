Automate your Telegram channel with a Django Telegram Bot

This code allows you to send automated messages to telegram channel using a bot with django
so let's take a look at how its done.

step 1: clone the repository
git clone https://github.com/shareefmhd03/impress.ai.git

step 2: install requirements
pip install -r requirements.txt


step 3: create a telegram channel and telegram bot and make the bot the administrator of the channel

note: save the bot token obtained while creating the bot, this is required to send messages with the bot

step 3: add telegram bot parameters to settings.py 

TELEGRAM = {
    'bot_token': '123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'channel_name': 'channel_name',
}

note: To interact with the Telegram bot API I chose python-telegram-bot because it looks quite simple to integrate and use.
to know more visit : https://github.com/python-telegram-bot/python-telegram-bot

step 4: create Database and migrate the changes
python manage.py migrate

step 5 :run the server and use
python manage.py runserver