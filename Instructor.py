import re
from Member import Member
class Instructor:
    def __init__(self,calendar,members):

        self.messages = []

        self.attendedClasses = []
        self.calendar = calendar
        self.members = members


    def receiveMessage(self,message):
        #receives messages
        if len(self.messages) > 0:
            self.messages.pop(0)
        self.messages.append(message)

    def viewMessages(self):
        #prints messages with the latest being at the top
        i = 0
        print("Your messages starting from the latest to the earliest")
        for message in self.messages:
            print("\t%d. %s" % (i + 1, message))
            i += 1

    def sendMessage(self):
        #can send messages to all or some members
        message = input("What the message: ")
        choice = int(input("Would you like to send this message to everyone or select members: "))
        if choice == 1:
            for i in self.members.values():
                i.receiveMessage(message)
        else:

            for i in self.members.keys():
                print(i,sep=", ")
            inputs = input("Enter the names of people who you would like to send messages to")
            listOfRecipients= re.split(", |,| , |, | ,| ", inputs)
            for i in listOfRecipients:
                self.members[i].receiveMessage(message)
    def printMeetings(self):
        for mo in self.calendar:
            for me in self.calendar[mo].meetings:
                print("%s %d"%(mo,me),end = ' ')
            print('\n')
        print('\n')

    def attend(self):
        #attend a meeting
        self.printMeetings()
        cond = True
        while cond:
            date = input("Enter the date of the class: ")
            datels = date.split(" ")
            day = int(datels[1])
            self.calendar[datels[0]].meetings[day].instructorAttends = True
            self.attendedClasses.append(date)
            cond = False

    def viewSchedule(self):
        for date in self.attendedClasses:
            datels = date.split(" ")
            mo = datels[0]
            me = int(datels[1])
            print("%s attended by: "% date,end = " ")
            for mem in self.calendar[mo].meetings[me].attendees:
                print("%s" %mem.name,end = ' ')
            print("\n")

    def printMems(self,mo,meeting):
        for mem in self.calendar[mo].meetings[meeting].attendees:
            print(mem,end=' ')
        print('\n')



    def addOrRemove(self):
        self.printMeetings()
        cond = True
        while cond:
            inp = input("Which meeting would you like to add to or remove from? ")
            choice = inp.split(' ')

            self.printMems(choice[0],int(choice[1]))
            cond2 = True
            while cond2:
                choice2 = int(input("Would you like to add or remove? Enter 1 to add/2 to remove: "))
                if choice2 == 1:
                    #add
                    choice3 = input("Enter the name of the person you would like to add: ")
                    self.calendar[choice[0]].meetings[int(choice[1])].addAttendee(self.members[choice3],1)
                    self.members[choice3].receiveMessage("You have been added to the following meeting: %s %d" % (choice[0],int(choice[1])))

                    #self.members[choice3].paidClasses.append("")
                    cond2 = False
                elif choice2 == 2:
                    print("Here is a list of all people currently in this meeting.")
                    self.calendar[choice[0]].meetings[int(choice[1])].getAttendees()
                    choice4 = input("Choose the name of the member who you would like to remove: ")
                    for i in self.calendar[choice[0]].meetings[int(choice[1])].attendees:
                        if i.name == choice4:
                            self.calendar[choice[0]].meetings[int(choice[1])].attendees.remove(i)
                    self.members[choice4].receiveMessage("You have been removed from the meeting on: %s %d" % (choice[0],int(choice[1])))
                    cond2 = False
                    pass
                else:
                    print("Invalid Choice!")
            cond = False

    def instructorLoop(self):
        cond = True
        while cond:
            print("Please choose one of the following options")
            print("\t1. to view your messages\n\t2. to attend a meeting\n\t3. to see your classes\n\t4. to exit ")
            newoption = int(input("Your choice: "))

            if newoption == 1:

                print(self.viewMessages())

            elif newoption == 2:
                self.attend()

            elif newoption == 3:
                self.viewSchedule()

            else:
                cond = False