class Instructor:
    def __init__(self):
        self.__attendance = 0
        self.__messages = []
        self.__balance = 0
        self.__attendedClasses = []

    def attends(self):
        self.__attendance += 1


    def addAttendedClass(self,title):
        self.__attendedClasses.append(title)

    def getAttendance(self):
        return self.__attendance

    def getAttendedClasses(self):
        print("You have attended the following classes: ",end=" ")
        for cl in self.__attendedClasses:
            print("%s" % cl, sep=", ")


    def getPaid(self,amount):
        self.__balance += amount

    def getBalance(self):
        return "Your balance is %d" % self.__balance

    def getPaid(self,amount):
        self.__balance += amount

    def receiveMessage(self,message):
        if len(self.__messages) > 0:
            self.__messages.pop(0)
        self.__messages.append(message)

    def viewMessages(self):
        if len(self.__messages) == 0:
            return "Your mailbox is currently empty\n"
        return self.__messages

    def reset(self):
        self.__attendance = 0

    def instructorLoop(self):
        cond = True
        while cond:
            print("Please choose one of the following options")
            newoption = int(input("\t1. to view your messages\n\t2. to view your balance\n\t3. to see your attendance\n\t4. to exit "))

            if newoption == 1:

                print(self.viewMessages())

            elif newoption == 2:
                print(self.getBalance())

            elif newoption == 3:
                self.getAttendedClasses()

            else:
                cond = False