from Member import Member
from Month import Month
from Meeting import Meeting
from tabulate import tabulate
class Treasurer:
    def __init__(self,instructor,calendar,members):
        self.instructor = instructor
        self.calendar = calendar
        self.members  = members

    def payAllDebt(self):
        #clears all debt
        for month in self.calendar.values():
            month.rentPaid = True
            month.instructorPaid = True

    def payDebt(self):
        #clears debt for select months
        cond = True
        while cond:
            mo = input("Enter the month you're trying to pay debt for: ")
            if mo not in self.calendar.keys():
                pass
            else:
                self.calendar[mo].rentPaid = True
                self.calendar[mo].instructorPaid = True
                cond = False

    def seeDebt(self):
        #shows debt for each month
        print("\tHall Expenses\tCoach Expenses")
        theList = [[mo.monthName,mo.rentDebt(),mo.coachDebt()] for mo in self.calendar.values()]
        print(tabulate(theList,headers=["Rent","Coach"],tablefmt="github"))

    def seeAccounts(self):
        totalR = 0
        totalE = 0
        theList = [x.profit() for x in self.calendar.values()]

        for x in self.calendar.values():
            ret = x.profit()
            theList.append(ret)

            totalR += ret[1]
            totalE += ret[2]
        theList.append(["total",totalR,totalR,totalR-totalE])
        print(tabulate(theList, headers=["Month", "Revenue($)", "Expenses($)","Profit"],tablefmt="github"))


    def printMems(self,mo,meeting):
        for mem in self.calendar[mo].meetings[meeting].attendees:
            print(mem,end=' ')
        print('\n')


    def printMeetings(self):
        for mo in self.calendar:
            for me in self.calendar[mo].meetings:
                print("%s %d"%(mo,me),end = ' ')
            print('\n')
        print('\n')

    def addOrRemove(self):
        self.printMeetings()
        cond = True
        while cond:
            choice = input("Which meeting would you like to add to or remove from? ")
            choice = choice.split(' ')

            self.printMems(choice[0],int(choice[1]))
            cond2 = True
            while cond2:
                choice2 = int(input("Would you like to add or remove? Enter 1 to add/2 to remove: "))
                if choice2 == 1:
                    #add
                    choice3 = input("Enter the name of the person you would like to add: ")
                    self.calendar[choice[0]].meetings[int(choice[1])].addAttendee(self.members[choice3],1)
                    self.members[choice3].receiveMessage("You have been added to the following meeting: %s %d" % (choice[0],int(choice[1])))
                    self.instructor.receiveMessage("%s has been added to the following meeting: %s %d" % (choice3,choice[0],int(choice[1])))
                    #self.members[choice3].paidClasses.append("")
                    cond2 = False

                elif choice2 == 2:
                    print("Here is a list of all people currently in this meeting.")
                    self.calendar[choice[0]].meetings[int(choice[1])].getAttendees()

                    choice4 = input("Choose the name of the member who you would like to remove: ")
                    for i in self.calendar[choice[0]].meetings[int(choice[1])].attendees:
                        if i.name == choice4:
                            self.calendar[choice[0]].meetings[int(choice[1])].attendees.remove(i)
                    self.members[choice4].receiveMessage("You have been removed from the meeting on %s %d" % (choice[0],int(choice[1])))
                    self.instructor.receiveMessage("%s has been removed from the following meeting: %s %d" % (choice4,choice[0],int(choice[1])))
                    cond2 = False

                else:
                    print("Invalid Choice!")
            cond = False

    def payables(self):
        #prints people who paid for each month in advance
        for mo in self.calendar.values():
            theList = mo.upfronts()
            print("%s: " % mo.monthName,end = ' ')
            print (', '.join([x for x in theList]))

    def loop(self):

        cnd = True
        while cnd:
            print("\t\t\t\t*" * 12)
            print("\nManager/Treasurer Panel\n")
            print(
                "Please choose one of the following options or press any other integer to return to the main menu\n")

            choice = int(input(
                "\t1. To see profit\n\t2. To see unpaid debt\n\t3. To see people who paid in full per month\n\t4. To pay all debt\n\t5. Manage coach's list(add or remove members)\nYour choice: "))

            if choice == 1:
                self.seeAccounts()

            elif choice == 2:
                self.seeDebt()

            elif choice == 3:

                self.payables()

            elif choice == 4:
                choice = int(input(
                    "Would you like to clear debts for all months or certain months? Press 1 for all. Press any other integer otherwise"))
                if choice == 1:
                    self.payAllDebt()
                else:
                    self.payDebt()

            elif choice == 5:
                self.addOrRemove()

            else:
                cnd = False