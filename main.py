#This will be the main file

#check if sorting lists returns correct list
from Member import Member
from Month import Month
from Instructor import Instructor
from Treasurer import Treasurer
from Meeting import Meeting
import unittest

calendar = {"January": Month("January",7,14,21,28),"February": Month("February",4,11,18,25),"March": Month("March",4,11,18,25),
            "April": Month("April",1,8,15,22,29),"May": Month("May",6,13,20,27),"June": Month("June",3,10,17,24),"July": Month("July",1,8,15,22,29),
            "August": Month("August",5,12,19,26),"September": Month("September",2,9,16,23,30),"October": Month("October",7,14,21,28),
            "November": Month("November",4,11,18,25),"December": Month("December",2,9,16,23,30)}

members = {"User1":Member("User1",111,"1 Main St",calendar),"User2":Member("User2",222,"2 Main St",calendar),"User3":Member("User3",333,"3 Main St",calendar),
           "User4":Member("User4",444,"4 Main St",calendar),"User5":Member("User5",555,"1 Main St",calendar),"User6":Member("User6",666,"6 Main St",calendar),
           "User7":Member("User7",777,"7 Main St",calendar),"User8":Member("User8",888,"8 Main St",calendar),"User9":Member("User9",999,"9 Main St",calendar),
           "User10":Member("User10",101010,"10 Main St",calendar)}

membersList = [member for member in members.values()]
instructor = Instructor(calendar,members)
treasurer = Treasurer(instructor,calendar,members)


def printMembers():
    print("\nList of Members\n")
    for member in members.values():
        member.print()

def sortByFrequency():
    #this function will sort members based on the number of classes they have attended
    membersList.sort(key=lambda x: len(x.attendedClasses), reverse=True)
    return membersList


def sortByPaid():
    #this fucntion will sort members by the number of classes they have paid for. A member not having skipped a payment for three months will receive a 10% discount
    membersList.sort(key=lambda x: len(x.paidClasses), reverse=True)
    return membersList

def sortByNotPaid():
    # this fucntion will sort members by the number of classes they have not paid for. A member having skipped at least one payment will receive a notice
    membersList.sort(key=lambda x: len(x.unpaidClasses), reverse=True)
    return membersList

#test cases
class Tests(unittest.TestCase):
    def testMonthUpfronts(self):
        #testing function upfronts() in class Month
        #testing function profit() in class Month
        mo = Month("name",1,2,3,4)
        user1 = Member("John",11,"1 John St",calendar)
        user2 = Member("Jane",22,"2 John St",calendar)
        mo.oneMonth.append(user1)
        mo.oneMonth.append(user2)
        self.assertEqual(mo.upfronts(),["John","Jane"]) #expect a list with the name of people who have paid for one month in advance
        self.assertEqual(mo.profit(),["name",80,75,5])

    def testMonthRentDebt(self):
        #testing function addOneMonth in class Month
        #testing to see if people who have paid in advance are added to a list keeping track of them
        mo = Month("name", 1, 2, 3, 4)
        self.assertEqual(mo.rentDebt(),75)

    def testMonthCoachDebt(self):
        #testing function coachDebt in class Month
        mo = Month("name", 1, 2, 3, 4)
        ins = Instructor(calendar,members)
        self.assertEqual(mo.coachDebt(), 0)
        mo.meetings[1].instructorAttends = True
        self.assertEqual(mo.coachDebt(),25)

    #testing functions of class Meeting
    def testMeeting(self):
        me = Meeting(1)
        user1 = Member("John", 11, "1 John St", calendar)
        user2 = Member("Jane", 22, "2 John St", calendar)
        # adding user 1 to the list of attendees who have paid, also added to the list of attendees )
        me.addAttendee(user1,1)
        # adding user 2 to the list of attendees who have not paid, also added to the list of attendees
        me.addAttendee(user2,0)
        me.instructorAttend()

        self.assertEqual(me.attendees,[user1,user2])
        self.assertEqual(me.paid,[user1])
        self.assertEqual(me.notpaid,[user2])
        self.assertEqual(me.instructorAttends, True)

    def testTreasurer(self):

        cal = {"mo1":Month("mo1",1,2),"mo2":Month("mo2",1,2)}
        john = Member("John", 1, "1 Main St", cal)
        mems = {"John":john}
        ins = Instructor(cal,mems)

        treas = Treasurer(ins,cal,mems)
        cal["mo1"].meetings[1].instructorAttends = True

        self.assertEqual(cal["mo1"].coachDebt(),25)
        treas.payAllDebt()
        self.assertEqual(cal["mo1"].coachDebt(),0)

    def testMember(self):
        cal = {"mo1":Month("mo1",1,3,4)}
        user1 = Member("User1",1,"1",cal)
        user1.signUp()  #when prompted, sign up for meeting mo1 1

        self.assertEqual(user1.getAttendance(),["mo1 1"])  #checks function getAttendance in Member

        user1.payOneMonth()  #when prompted, pay for meetings in mo1
        self.assertEqual(cal["mo1"].oneMonth, [user1]) #checks function payOneMonth() in Member

#main loop of the program
def mainLoop():
    cond = True
    while cond:

        print("\t+"*15)
        print("\n")
        print("\t\t\t\tMAIN MENU")
        print("\n")
        option = int(input("To use as a member please press 1\nTo use as treasurer press 2\nTo use as an instructor press 3\nTo see members log/sort members press 4\nYour choice: "))

        if option == 1:
            # This option is activated when the user is a club member
            newoption = int(input("Please enter 1 if you already have an account or 2 to sign up: "))

            if newoption == 1:

                name = input("Please enter your name: ")

                if name in members.keys():

                    members[name].loop()

                else:
                    print("Name not found")

            elif newoption == 2:
                name = input("Please enter your name to sign up: ")
                phone = int(input("Please enter your phone number: "))
                address = input("Please enter your address: ")
                members[name] = Member(name,phone,address,calendar)

        elif option == 2:
            #use as a treasurer
            treasurer.loop()

        elif option == 3:
            #This option is activated when the user is an instructor
            instructor.instructorLoop()

        elif option == 4:
            inp = int(input("To see the list of members press 1, to see the list of members sorted by the number of times they have paid press 2, to see the list of members by the number of times they haven't paid press 3, 4 to see full list of members: "))
            if inp == 1:
                #sort by frequency of attendance
                theList = sortByFrequency()
                i = 0
                for member in theList:
                    print("%s - Number of Attended Classes: %d" % (member.name, len(member.attendedClasses)))
                    if i < 10:
                        member.receiveMessage(
                            "You will receive 10% discount for one class because of your visit frequency. Congrats!")
                        member.getDiscount = True
                    i += 1
            elif inp == 2:
                #sort by number of times paid
                theList = sortByPaid()
                for member in theList:
                    if len(member.unpaidClasses):
                        member.receiveMessage("You will get a 10% discount since you have not missed a payment")
                    print("%s - Number of Classes Paid for: %d - Number of Classes Not Paid for: %d" % (
                    member.name, len(member.paidClasses), len(member.unpaidClasses)))

            elif inp == 3:
                #sort by number of times not paid
                theList = sortByNotPaid()
                for member in theList:

                    if len(member.unpaidClasses) > 0:
                        member.receiveMessage(
                            "You have %d unpaid classes. Please pay your debt off or you will be expelled from the group or incur penalty fees" % (
                                len(member.unpaidClasses)))
                    print("%s - Number of Classes Not Paid for: %d - Number of classes Paid for: %d" % (
                    member.name, len(member.unpaidClasses), len(member.paidClasses)))

            elif option == 4:
                printMembers()
            else:
                print("Wrong option")
        else :
            cond = False


# if __name__ == '__main__':
#     unittest.main()

mainLoop()