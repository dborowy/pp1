class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        messageU = message[0].upper()+message[1:]+'BYE.'
        self.message = messageU
x = Message()
x.set_message('Witam.')
print(x.message)
        