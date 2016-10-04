import logging
import datetime


class Bot:
    def __init__(self, bot_username, oath_key, channel, msg_template="{}"):
        self.s = socket.socket()
        self.bot_username = bot_username
        self.oath_key = oath_key
        self.channel = channel
        self.msg_template = msg_template

    def join(self):
        servername = "irc.twitch.tv"
        port = 6667
        self.connect(servername, port)
        self.send_join_msgs(self.channel)
        logging.info("[{}]\tSuccessfully connected to the channel!"
                .format(datetime.datetime.now())
        self.msg_template = "PRIVMSG #{} :{}\r\n"
                .format(self.channel,self.msg_template)
        self.say_hello()

    def send_join_msgs(self):
        self.send("PASS {}\r\n".format(self.oath_key).encode("utf-8"))
        self.send("USER {}\r\n".format(self.bot_username).encode("utf-8"))
        self.send("NICK {}\r\n".format(self.bot_username).encode("utf-8"))
        self.send("JOIN #{}\r\n".format(self.channel.lower()).encode("utf-8"))

    def say_hello(self):
        self.send_bot_msg(
                "Hello! I am a bot built with Frendo. You "
                "can always build me a friend."
                " Check it out @ https://github.com/samhal/frendo !")

    def send(self, msg):
        self.s.send(msg)

    def connect(self, servername, port):
        self.s.connect(servername,port)

    def send_bot_msg(self,msg):
        bot_msg = self.msg_template.format(msg)
        self.send(bot_msg)
