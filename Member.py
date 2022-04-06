class Member:
    def __init__(self,name):
        self.__name = name
        self.__debt = 0
        self.__messages = []
    def getDebt(self):
        return self.__debt
    def addDebt(self,amount):
        self.__debt += amount
    def payDebt(self):
        self.__debt = 0
    def hasDebt(self):
        if self.__debt > 0:
            return True
        return False

    def __str__(self):
        return "Name: %s and balance: %d" % (self.__name,self.__debt)
    def payOneMonth(self):
        #this is only available if self.__debt is 0
        if self.__debt == 0:
            self.__debt -= 40
        else:
            print("Sorry, you may not pay for one month in advance because your balance is not clear.")
    def receiveMessage(self,message):
        if len(self.__messages) > 0:
            self.__messages.pop(0)
        self.__messages.append(message)
    def viewMessages(self):
        return self.__messages

    def loop(self):
        print("Welcome %s" % self.__name)

        print("Please choose one of the following option.")

        option = int(input("\t1. View your debt\n\t2. View your messages\n\t3. Pay Your Debt\n\t4. Pay for one month in advance\nYour choice: "))

        if option == 1:

            print("Your debt is %d" % self.__debt)

        elif option == 2:
            print(self.__messages)

        elif option == 3:
            if self.__debt == 0:

                print ("You currently have no outstanding balance. Thank you!")

            else:

                self.payDebt()
                print("Thank you for clearing your balance")
                print(self.getDebt())

        elif option == 4:
            self.payOneMonth()
        else:
            print ("Wrong option")
            
