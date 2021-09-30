<!-- ABOUT THE PROJECT -->
## Automate your Telegram channel with a Django Telegram Bot

This code allows you to send automated messages to telegram channel using a bot with django
so let's take a look at how its done.



---

### Installation
1. clone the repository

   ```sh
   git clone https://github.com/shareefmhd03/impress.ai.git
   ```

2. Install requirements.txt
   ```sh
   pip install -r requirments.txt
   ```
3. create a telegram channel and telegram bot and make the bot the administrator of the channel

**note** 
save the bot token obtained while creating the bot, this is required to send messages with the bot.



---
4. add telegram bot parameters to settings.py 
   ```sh
   TELEGRAM = {
    'bot_token': '123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'channel_name': 'channel_name',
    }
    ```   


**note** 

To interact with the Telegram bot API I chose python-telegram-bot because it looks quite simple to integrate and use.
to know more visit : https://github.com/python-telegram-bot/python-telegram-bot


5. Create DB and migrate the changes
    ```sh
   python manage.py migrate
   ```   

6. Run server: <br>
   ```JS
   python manage.py runserver
   ```