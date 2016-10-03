import configparser
import logging

def main():
    config = configparser.Configparser()
    config.read("bot.ini")
if __name__ == "__main__":
    main()
