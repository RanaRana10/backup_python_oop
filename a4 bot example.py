class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        pass

class ChatBot(Bot):
    def send_message(self, message):
        print(f"ChatBot {self.name} sends: {message}")

class GameBot(Bot):
    def send_message(self, message):
        print(f"GameBot {self.name} sends: {message}")

chatbot = ChatBot("ChatMaster")
gamebot = GameBot("GameWizard")

chatbot.send_message("Hello, how can I help you?")
gamebot.send_message("Get ready to play!")

# Output:
# ChatBot ChatMaster sends: Hello, how can I help you?
# GameBot GameWizard sends: Get ready to play!
