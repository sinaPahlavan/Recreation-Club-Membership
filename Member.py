class Member:
    def __init__(self,name):
        self.__name = name
        self.__debt = 0
        self.__messages = []
        # a list of lists in the format [Title of class attended,payment status]
        self.__attendedClasses = []
        self.__hasPaidLumpSum = False

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

    def attend(self,meetingTitle,paymentStatus):

        self.__attendedClasses.append([meetingTitle,paymentStatus])

    def getAttendance(self):
        for i in self.__attendedClasses:
            if i[1] == 1:
                print("\tYou attended %s meeting and paid its fee." % i[0])

            else:
                print("\tYou attended %s meeting but didn't pay" % i[0])

    def hasPaidLumpSum(self):
        return self.__hasPaidLumpSum



    def __str__(self):
        return "Name: %s and balance: %d" % (self.__name,self.__debt)

    def payOneMonth(self):
        #this is only available if self.__debt is 0
        if self.__debt == 0:
            self.__debt -= 40
            self.__hasPaidLumpSum = True
        else:
            print("Sorry, you may not pay for one month in advance because your balance is not clear.")

    def receiveMessage(self,message):
        self.__messages.insert(0,message)
    def viewMessages(self):
        return self.__messages

    def loop(self):
        print("Welcome %s" % self.__name)
        cond = True
        while cond:

            print("Please choose one of the following option. Or press 6 to return to the main menu.")

            option = int(input("\t1. View your debt\n\t2. View your messages\n\t3. Pay Your Debt\n\t4. Pay for one month in advance\n\t5. See your attendance\nYour choice: "))

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
            elif option == 5:
                self.getAttendance()
            elif option == 6:
                cond = False
            else:
                print ("Wrong option")
            
