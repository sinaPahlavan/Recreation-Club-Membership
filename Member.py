from Month import Month
#from Meeting import Meeting
class Member:
    def __init__(self,name,phone,address,calendar):
        self.name = name

        self.calendar = calendar

        self.__messages = []
        # a list of lists in the format [Title of class attended,payment status]
        self.phone = phone
        self.address = address
        self.attendedClasses = []
        self.paidClasses = []
        self.unpaidClasses = []
        self.monthsPaidUpfront = []
        self.getDiscount = False




    def getAttendance(self):
        return self.attendedClasses


    def __str__(self):
        return "%s" % (self.name)

    def print(self):
        print("Name: %s Phone Number: %d Address: %s Classes: " % (self.name,self.phone,self.address),end = " ")
        for cl in self.attendedClasses:
            if cl in self.paidClasses:
                print("%s(paid) " % cl,end=' ')
            else:
                print("%s(not paid) " % cl, end=' ')
        print("\n")

    def payOneMonth(self):
        mo = input("Which month would you like to pay for in advance? ")
        if mo in self.calendar.keys():
            self.calendar[mo].addOneMonth(self)
            self.monthsPaidUpfront.append(mo)


            for me in self.calendar[mo].meetings.values():
                me.paid.append(self.name)
                date = mo
                date += " "
                date += str(me.title)
                self.attendedClasses.append(date)
                self.paidClasses.append(date)
                me.addAttendee(self,1)
                me.balance += 10

    def receiveMessage(self,message):
        self.__messages.insert(0,message)

    def viewMessages(self):
        i = 0
        print("Your messages starting from the latest to the earliest")
        for message in self.__messages:
            print("\t%d. %s" % (i+1,message))
            i += 1

        print("\n")

    def printMeetings(self):
        for mo in self.calendar:
            for me in self.calendar[mo].meetings:
                print("%s %d"%(mo,me),end = ' ')
            print('\n')
        print('\n')

    def signUp(self):
        cond = True
        print("Please choose a meeting from the list below")
        self.printMeetings()

        while cond:
            choice = input("Which meeting would you like to sign up for? ")
            choice = choice.split(' ')
            mo = choice[0]

            if mo in self.monthsPaidUpfront:
                print("You have already signed up for classes in %s" % mo)
            else:
                me = int(choice[1])
                pay = int(input("Would you like to pay for this meeting? Press 1 for yes or any other integer for no: "))
                date = mo
                date += " "
                date += str(me)
                self.attendedClasses.append(date)
                if pay == 1:
                    self.calendar[mo].meetings[me].addAttendee(self,1)

                    self.paidClasses.append(date)
                    if self.getDiscount == True:
                        self.calendar[mo].meetings[me].balance += 9
                        self.getDiscount = False
                    else:
                        self.calendar[mo].meetings[me].balance += 10

                else:
                    self.calendar[mo].meetings[me].addAttendee(self, 0)
                    self.unpaidClasses.append(date)
            cond = False

    def loop(self):
        print("\n\tWelcome %s to the member panel\n" % self.name)
        cond = True
        while cond:

            print("Please choose one of the following option. Or press any other integer to return to the main menu.")

            option = int(input("\t1. Sign up and pay for a meeting\n\t2. Pay for a month in advance\n\t3. View your messages\n\t4. See your classes\nYour choice: "))

            if option == 1:

                self.signUp()

            elif option == 2:
                self.payOneMonth()

            elif option == 3:
                self.viewMessages()

            elif option == 4:
                theList = self.getAttendance()
                size = len(theList)

                if size == 0:
                    print("No classes yet")
                elif size == 1:
                    print("Your classes: %s" % theList[0])
                else:
                    print("Your classes:", end=" ")
                    print(', '.join([x for x in theList]))
            else:
                cond = False
            
