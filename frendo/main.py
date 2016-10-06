#! /usr/bin/python3
from configparser import ConfigParser
import os
from bot import Bot
from _thread import start_new_thread


class Frendo:
    def __init__(self):
        self.configfile_path = os.path.expanduser("~/.frendorc")

    def start(self):
        if os.path.isfile(self.configfile_path):
            bot = self.get_bot_from_config()
        else:
            bot = self.get_bot_from_user()
        bot.join()

    def get_bot_from_user(self):
        print("Please read the instructions on how to answer following question"
              "@ https://github.com/samhal/frendo\n")
        bot_username = self.get_bot_username_from_user()
        oauth_token = self.get_oauth_token_from_user()
        channel = self.get_channel_from_user()
        msg_template = self.get_msg_template_from_user()
        start_new_thread(self.write_configfile, (channel,
                bot_username, oauth_token, msg_template,))
        return Bot(bot_username, oauth_token, channel, msg_template)

    def get_bot_from_config(self):
        config = ConfigParser()
        config.read(self.configfile_path)
        bot_section = config["BOT"]
        channel_section = config["CHANNEL"]
        bot_username = bot_section["bot_username"]
        oauth_token = bot_section["oauth_token"]
        msg_template = bot_section["message_template"]
        channel = channel_section["channel_name"]
        return Bot(bot_username, oauth_token, channel, msg_template)

    def write_configfile(self, channel, bot_username, oauth_token, msg_template):
        config = ConfigParser()
        config["CHANNEL"] = {"channel_name": channel}
        config["BOT"] = {"bot_username": bot_username, "oauth_token": oauth_token,
                "message_template": msg_template}
        with open(self.configfile_path, "w+") as configfile:
            config.write(configfile)

    def get_oauth_token_from_user(self):
        return input("oauth-key: ")

    def get_bot_username_from_user(self):
        return input("Bot username: ")

    def get_channel_from_user(self):
        return input("Channel to join (e.g Lirik): ")

    def get_msg_template_from_user(self):
        return input("Template for messages (e.g Kappa \{\} Kappa): ")

if __name__ == "__main__":
    frendo = Frendo()
    frendo.start()
