class Meeting:
    def __init__(self,title):
        self.title = title

        #change 1 and 0 to true and false
        self.attendees = []
        self.paid = []
        self.notpaid = []
        self.instructorAttends = False
        self.balance = 0

    def addAttendee(self,memberObj,payment):
        if payment == 1:
            self.paid.append(memberObj)
        else:
            self.notpaid.append(memberObj)
        self.attendees.append(memberObj)

    def getAttendees(self):
        for i in self.attendees:
            print(i,end=" ")
        print("\n")

    def instructorAttend(self):
        self.instructorAttends = True