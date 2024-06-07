old_messages = []


def print_only_new(message):
    if message not in old_messages:
        print(message)
    old_messages.append(message)
