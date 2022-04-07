from Member import Member
from Instructor import Instructor
from Meeting import Meeting
import re
class Club:
    def __init__(self):
        self.__memberList = {}
        self.__meetingList = {}
        self.__balance = 0
        self.instructor = Instructor()
    def addMember(self,name):
        self.__memberList[name] = Member(name)

    def memberExists(self,name):
        if name in self.__memberList.keys():
            return True
        return False

    def getBalance(self):
        return self.__balance

    def sendBalanceNotice(self):
        # sends outstanding balance notices to members
        for key,value in self.__memberList.items():

            if value.hasDebt():
                if value.getDebt() <= 20:
                    value.receiveMessage("Your currently have %d dollars in outstanding debt to the club. Please use the member panel to clear your balance. Thank you!" % value.getDebt())
                else:
                    value.receiveMessage("You currently have %d dollars in outstanding fees. If you don't pay your debt, you will be removed from the club!" % value.getDebt())

    def sendMeetingReminders(self,meetingTitle):
        if meetingTitle in self.__meetingList.keys():
            if self.__meetingList[meetingTitle].getStatus() == "passed":
                print("The meeting with title %s has already taken place. You can't send reminders about this meeting" % meetingTitle)
            else:
                for value in self.__memberList.values():
                    if self.__meetingList[meetingTitle].instructorAttends() == 1:
                        value.receiveMessage("Don't forget to attend %s meeting. The instructor will be there!" % meetingTitle)
                    else:
                        value.receiveMessage(
                            "Don't forget to attend %s meeting. The instructor will not be there however!" % meetingTitle)

        else:
            print("Meeting %s not found" % meetingTitle)

    def payInstructor(self):

        numofclasses = len(self.__meetingList)
        if numofclasses % 2 != 0:

            if (self.instructor.getAttendance()>0):
                wage = 100 * self.instructor.getAttendance()
                self.__balance -= wage
                self.instructor.receiveMessage("Congrats! You have been paid %d dollars for the %d classes you supervised." % (wage, self.instructor.getAttendance()))
                self.instructor.reset()

            else:
                print("The instructor has not attended any classes")
        else:
            print("The instructor can only be paid biweekly or monthly")

    def startMeeting(self,meetingTitle):
        print("\n****************************************************\n")
        print("\tHere is a list of all members in the club. Please indicate who attended this meeting.\n\tYou can do so by entering comma separated values. eg. Jane, John")

        for key in self.__memberList.keys():
            print("%s"%key,sep=", ")
        print("\n")

        instructorAttends = int(input("Enter 1 if the instructor is present. Enter any other integer if they are not: "))

        if instructorAttends == 1:
            self.instructor.attends()
        inputs = input("Enter the names of participants in this class: ")

        listOfParticipants = re.split(", |,| , |, | ,| ",inputs)
        for name in listOfParticipants:

            if self.memberExists(name):
                member = self.__memberList[name]
                print("Did %s pay for this meeting? " % name,end="")
                payment = int(input("Enter 1 for yes or 0 for no: "))

                if payment == 1:
                    member.attend(meetingTitle,1)
                    if member.hasPaidLumpSum():
                        member.receiveMessage("You have received 20 percent discount on %s fee because you previously paid for a month in advance!" % meetingTitle)
                        member.addDebt(8)
                    else:
                        if member.getDebt() == 0:
                            member.receiveMessage(
                                "You have received 10 percent discount the on %s fee because your balance is clear!" % meetingTitle)
                            member.addDebt(9)
                        else:
                            member.addDebt(10)


                else:
                    self.__memberList[name].attend(meetingTitle, 0)
                    member.addDebt(10)
            else:
                print("No member found named %s"%name)


    def clubLoop(self):
        cnd = True
        while cnd:
            print("\t\t\t\t*"*12)
            print("\nManager/Treasurer Panel\n")
            print("Please choose one of the following options or press any other integer to return to the main menu\n")

            choice = int(input(
                "\t1. To notify members with debt\n\t2. To schedule a meeting\n\t3. To send reminders about a meeting\n\t4. To start a meeting\n\t5. To pay the instructor\nYour choice: "))
            if choice == 1:
                self.sendBalanceNotice()

            elif choice == 2:

                title = input("What's the title of the meeting to schedule? ")
                instructorAttends = int(input("Will the instructor attend this meeting? Enter 1 for yes or 0 for no: "))
                if instructorAttends == 1:
                    self.instructor.attends()
                    self.__meetingList[title] = Meeting(title, 1, "Upcoming")
                else:
                    self.__meetingList[title] = Meeting(title, 0, "Upcoming")

            elif choice == 3:
                title = input("What's the title of the meeting you would like to send reminders about? ")
                self.sendMeetingReminders(title)

            elif choice == 4:

                title = input("What's the title of the meeting you would like to start? ")
                self.startMeeting(title)

            elif choice == 5:
                self.payInstructor()

            else:
                cnd = False

    def mainLoop(self):
        cond = False
        while not cond:

            print("\t+"*15)
            print("\n")
            print("\t\t\t\tMAIN MENU")
            print("\n")
            option = int(input("To use as a member please press 1\nTo use as treasurer press 2\nTo use as an instructor press 3\nYour choice: "))

            if option == 1:
                # This option is activated when the user is a club member
                newoption = int(input("Please enter 1 if you already have an account or 2 to sign up: "))

                if newoption == 1:

                    name = input("Please enter your name: ")

                    if name in self.__memberList:

                        self.__memberList[name].loop()

                    else:
                        print("Name not found")
                elif newoption == 2:
                    name = input("Please enter your name to sign up: ")
                    self.addMember(name)

            elif option == 2:

                self.clubLoop()

            elif option == 3:
                #This option is activated when the user is an instructor
                cond2 = True
                while cond2:
                    newoption3 = int(input("Press 1 to view your messages: "))

                    if newoption3 == 1:
                        self.payInstructor()
                        print(self.instructor.viewMessage())
                    else:
                        cond2 = False

            else :
                cond = True

