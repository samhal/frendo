import logging
import datetime
import socket
from _thread import start_new_thread
from parser import *
from importlib import import_module


class Bot:
    def __init__(self, bot_username, oauth_token, channel, msg_template="{}"):
        self.socket = socket.socket()
        self.bot_username = bot_username
        self.oauth_token = oauth_token
        self.channel = channel
        self.msg_template = msg_template

    def join(self):
        servername = "irc.twitch.tv"
        port = 6667
        self.connect(servername, port)
        self.send_join_msgs()
        (
            logging.info("[{}]\tSuccessfully connected to the channel!"
                .format(datetime.datetime.now()))
        )
        self.msg_template = ("PRIVMSG #{} :{}\r\n"
                .format(self.channel, self.msg_template))
        self.say_hello()

    def serve(self):
        while True:
            received_msg = self.socket.recv(2048).decode("ascii", "ignore")
            with open("Output.txt", "a") as text_file:
                text_file.write(received_msg + "\n")
            start_new_thread(self.check_received_msg, (received_msg,))

    def check_received_msg(self, msg):
        if "PRIVMSG" in msg:
            self.respond_to_privmsg(msg)
        elif "PING" in msg:
            self.respond_to_ping(msg)

    def respond_to_ping(self):
        self.send("PONG :tmi.twitch.tv\r\n")

    def respond_to_privmsg(self, msg):
        # TODO fix
        command = parse_command(msg)

    def send_join_msgs(self):
        self.send("PASS {}\r\n".format(self.oauth_token))
        self.send("USER {}\r\n".format(self.bot_username))
        self.send("NICK {}\r\n".format(self.bot_username))
        self.send("JOIN #{}\r\n".format(self.channel.lower()))

    def say_hello(self):
        print("hello")
        # self.send_bot_msg(
        #        "Hello! I am a bot built with Frendo. You "
        #        "can always build me a friend."
        #        " Check it out @ https://github.com/samhal/frendo !")

    def send(self, msg):
        self.socket.send(msg.encode("utf-8"))

    def connect(self, servername, port):
        self.socket.connect((servername, port))

    def send_bot_msg(self, msg):
        bot_msg = self.msg_template.format(msg)
        self.send(bot_msg)
