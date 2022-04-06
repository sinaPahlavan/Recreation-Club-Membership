from Member import Member
from Instructor import Instructor
from Meeting import Meeting
class Club:
    def __init__(self):
        self.__memberList = {}
        self.__meetingList = {}
        self.__balance = 0
        self.instructor = Instructor()
    def addMember(self,name):
        self.__memberList[name] = Member(name)

    def memberExists(self,name):
        if name in self.__memberList:
            return True
        return False

    def getBalance(self):
        return self.__balance

    def sendBalanceNotice(self):
        #sends outstanding balance notices to members
        for key,value in self.__memberList.items():
            if value.hasDebt() == True:
                value.receiveMessage("Your currently have %d dollars in outstanding debt to the club" % value.getDebt())

    def sendMeetingReminders(self,meetingTitle):
        if meetingTitle in self.__meetingList.keys():
            if self.__meetingList[meetingTitle].getStatus() == "passed":
                print("The meeting with title %s has already taken place. You can't send reminders about this meeting" % meetingTitle)
            else:
                for value in self.__memberList.values():
                    value.receiveMessage("Don't forget to attend meeting %s" % meetingTitle)
        else:
            print("Meeting %s not found" % meetingTitle)

    def payInstructor(self):
        if (self.instructor.getAttendance()>0):
            self.__balance -= 100 * self.instructor.getAttendance()
            self.instructor.receiveMessage("Congrats! You have been paid for the %d classes you supervised." % self.instructor.getAttendance())
        else:
            print("The instructor has not attended any classes")


    def mainLoop(self):
        cond = False
        while not cond:

            option = int(input("To use as a member please press 1\nTo use as club manager press 2\nTo use as an instructor press 3\nYour choice: "))

            if option == 1:
                # This option is activated when the user is a club member
                newoption = int(input("Pleas enter 1 if you already have an account or 2 to sign up: "))

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
                #This option is activated when the user is a club manager/treasurer

                print("Please choose one of the following options.")

                choice = int(input("\t1. To notify members with debt\n\t2. To schedule a meeting\n\t3. To send reminders about a meeting\n\t4. To start a meeting\nYour choice: "))
                if choice == 1:
                    self.sendBalanceNotice()

                elif choice == 2:

                    title = input("What's the title of the meeting to schedule? ")
                    instructorAttends = int(input("Will the instructor attend this meeting? Enter 1 for yes or 0 for no: "))
                    if instructorAttends == 1:
                        self.instructor.attends()
                        self.__meetingList[title] = Meeting(title,1,"Upcoming")
                    else:
                        self.__meetingList[title] = Meeting(title, 0, "Upcoming")

                elif choice == 3:
                    title = input("What's the title of the meeting you would like to send reminders about? ")
                    self.sendMeetingReminders(title)
                else:
                    print(self.__meetingList)



            elif option == 3:
                # This option is activated when the user is an instructor
                newoption3 = int(input("Press 1 to view your messages: "))

                if newoption3 == 1:
                    self.payInstructor()
                    print(self.instructor.viewMessage())

            else :
                cond = True

