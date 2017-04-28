class Chat(object):
    """docstring for Chat."""
    def __init__(self):
        self.chat_id = ''
        self.file_path = 'docs/{}.txt'
        self.user_name = ''

    # Read all messages in the chat
    def readChat(self):
        file = open(self.file_path, 'r')
        chat = file.readlines()
        file.close()
        return chat

    # Save all new messages in the chat
    def saveMessage(self, message):
        file = open(self.file_path, 'a+')
        file.write(message + '\n')
        file.close()

    # Read last message from bot in the chat
    def readLastMessage(self):
        chat = self.readChat(self.chat_id)
        return chat[len(chat) - 1].replace('@fit_expert_bot:', '').replace('\n', '').replace(' ', '_').lower()

    def setChatId(self, chat_id):
        self.chat_id = chat_id
        self.file_path = self.file_path.format(chat_id)

    def getChatId(self):
        return  self.chat_id

    def setUserName(self, user_name):
        self.user_name = user_name

    def getUserName(self):
        return self.user_name

    def getFilePath(self):
        return  self.file_path

# Test
# chat = Chat()
# print(chat.getChatId()+'\n')
# print(chat.getFilePath()+'\n')
# chat.setChatId('345464564332')
# print(chat.getChatId())
# print(chat.getFilePath())
# chat.saveMessage('hola como van')
