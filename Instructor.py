class Instructor:
    def __init__(self):
        self.__attendance = 0
        self.__messages = []
    def attends(self):
        self.__attendance+= 1

    def getAttendance(self):
        return self.__attendance

    def receiveMessage(self,message):
        if len(self.__messages) > 0:
            self.__messages.pop(0)
        self.__messages.append(message)

    def viewMessage(self):
        if len(self.__messages) == 0:
            return "Your mailbox is currently empty\n"
        return self.__messages

