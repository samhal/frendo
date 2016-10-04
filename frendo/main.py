import configparser
import logging
import os


def main():
    if os.path.isfile("~/.frendorc"):
        bot = get_bot_from_config()
    else:
        bot = get_bot_from_user()
    bot.join()


def get_bot_from_user():
    config = configparser.Configparser()
    print("Please read the instructions on how to answer following question"
          "@ https://github.com/samhal/frendo\n")
    bot_username = input("Bot username: ")
    oath_key = input("Oath-key: ")
    channel = input("Channel to join (e.g Lirik): ")
    return Bot()

if __name__ == "__main__":
    main()
