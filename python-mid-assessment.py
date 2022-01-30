class Logger:

    # Defining constructor
    def __init__(self):
        self.dict = {}

    # Defining method
    def should_print_message(self, message, timestamp):
        if message not in self.dict.keys() or timestamp - self.dict[message] >= 10:
            self.dict[message] = timestamp
            return True
        else:
            return False


# Creating an object
logger = Logger()

messages_list = ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
                 "shouldPrintMessage", "shouldPrintMessage"]
timestamp_and_message_list = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

result = []

for v in range(1, len(messages_list)):
    timestamp = timestamp_and_message_list[v][0]
    messages = timestamp_and_message_list[v][1]
    result = logger.should_print_message(messages, timestamp)
    print(result)


