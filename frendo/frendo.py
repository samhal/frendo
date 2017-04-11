#! /usr/bin/python3
import logging
import os
from configparser import ConfigParser

from bot import Bot


class Frendo:
    def __init__(self):
        logging.basicConfig(format="[%(levelname)s][%(asctime)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
        self.configfile_path = os.path.expanduser("~/.frendorc")

    def start(self):
        # check if user has a config-file
        if os.path.isfile(self.configfile_path):
            bot = self.get_bot_from_config()
        else:
            # config-file not found
            logging.error("Config-file not found at ~/.frendorc")
            exit(0)
        bot.join()
        bot.serve()

    def get_bot_from_config(self):
        config = ConfigParser()
        config.read(self.configfile_path)
        bot_section = config["BOT"]
        channel_section = config["CHANNEL"]
        bot_username = bot_section["bot_username"]
        oauth_token = bot_section["oauth_token"]
        # msg_template = bot_section["message_template"]
        msg_template = "{}"
        channel = channel_section["channel_name"]
        return Bot(bot_username, oauth_token, channel, msg_template)