import re


def parse(regex, text):
    text = re.search(regex, text, re.MULTILINE)
    if text:
        return text.group(1)
    else:
        return False


def parse_user(text):
    user = parse("@([a-zA-Z0-9]+).tmi.twitch.tv", text)
    if (user):
        return user
    else:
        return ""


def parse_command(text):
    command = parse(":!([a-zA-Z0-9]+)", text)
    if command:
        return command
    else:
        return ""


def parse_arguments(text):
    arguments = parse(":!(?:[a-zA-Z0-9]+) (.*)", text)
    if arguments:
        return arguments.split()
    else:
        return []
