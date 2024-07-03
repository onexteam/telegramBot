import os

#API ID & API Hash -----> my.telegram.org
api_id = 1088653
api_hash = 'e151caeac8a925c0491cc631021cc212'

#Bot Token -----> @BotFather
token = '7464492863:AAGtpFF4aMP1Udyb_w91MfS0X6gsrOcd9Ro'

#Session Name -----> optional
session_name = 'FTP_Manager'


#The robot admin (the person who can give orders to the robot.) -----> @myidbot
admins = [6519108070]

# Chat id to send technical logs
dev = 1117638015

# When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server.
# Here you need to specify its temporary storage path
# For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
dl_path = os.path.abspath(os.getcwd()) + '/'


# The upload path where we give FTP access to the bot.
ftp_path = '/Vods/'

# The files are temporarily downloaded after they are on the bot server. They are uploaded to another host through FTP.
# Here we have to give FTP access to the bot.
ftp_ip = '95.1'
ftp_username = 'nox-cloud'
ftp_password = 'a219945f-378b-483b-b6d21050a094-019a-4186'
ftp_domain = 'storage.bunnycdn.com'
