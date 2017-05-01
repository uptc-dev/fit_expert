class Chat(object):
    """docstring for Chat."""
    def __init__(self):
        self.chat_id = ''
        self.file_path = 'docs/{}.txt'
        self.user = ''

    # Read all messages in the chat
    def read_chat(self):
        file = open(self.file_path, 'r')
        chat = file.readlines()
        file.close()
        return chat

    # Save all new messages in the chat
    def save_message(self, message):
        file = open(self.file_path, 'a+')
        file.write(message + '\n')
        file.close()

    # Read last message from bot in the chat
    def read_last_message(self):
        chat = self.readChat(self.chat_id)
        return chat[len(chat) - 1].replace('@fit_expert_bot:', '').replace('\n', '').replace(' ', '_').lower()

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id
        self.file_path = self.file_path.format(chat_id)

    def get_chat_id(self):
        return  self.chat_id

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def get_file_path(self):
        return  self.file_path

# Test
# chat = Chat()
# print(chat.getChatId()+'\n')
# print(chat.get_file_path()+'\n')
# chat.setChatId('345464564332')
# print(chat.getChatId())
# print(chat.get_file_path())
# chat.saveMessage('hola como van')
