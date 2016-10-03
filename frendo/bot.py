Class Bot:
    def __init__(self, bot_username, oath_key, msg_template="{}"):
        self.s = socket.socket()
        self.bot_username = bot_username
        self.oath_key = oath_key
        self.msg_template = msg_template

    def join(self, channel):
        servername = "irc.twitch.tv"
        port = 6667
        self.connect(servername,port)
		self.send("PASS {}\r\n".format(self.oath_key).encode("utf-8"))
		self.send("USER {}\r\n".format(self.bot_username).encode("utf-8"))
		self.send("NICK {}\r\n".format(self.bot_username).encode("utf-8"))
        self.send("JOIN #{}\r\n".format(channel.lower()).encode("utf-8"))
        self.msg_template = "PRIVMSG #{} :{}\r\n".format(,channel,self.msg_template)
        self.bot_msg("Hello! I am a bot built with Frendo. You can always build me a friend."\
                "Check it out @ https://github.com/samhal/frendo !")

    def send(self, msg):
        self.s.send(msg)

    def connect(self, servername, port):
        self.s.connect(servername,port)

    def send_bot_msg(self,msg):
        bot_msg = self.msg_template.format(msg)
        self.send(bot_msg)
