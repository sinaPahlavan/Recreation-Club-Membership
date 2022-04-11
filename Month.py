from Meeting import Meeting

class Month:

    def __init__(self, name, *kwargs):
        self.monthName = name
        self.oneMonth = [] #list of people who have paid for this month in advance
        self.meetings = {w:Meeting(w) for w in kwargs}
        self.instructorPaid = False
        self.rentPaid = False

    def addOneMonth(self,other):
        self.oneMonth.append(other)


    def coachAttendance(self):
        tot = 0
        for meeting in self.meetings.values():
            if meeting.instructorAttends == True:
                tot += 1
        return tot

    def coachDebt(self):
        #hall expenses: 75 dollars
        #coach expenses: 20 dollars per attendance
        if self.instructorPaid == True:
            return 0
        return self.coachAttendance() * 25

    def rentDebt(self):
        if self.rentPaid == True:
            return 0
        return 75

    def expenses(self):
        return self.rentDebt() + self.coachDebt()

    def revenue(self):
        tot = 0
        for meeting in self.meetings.values():
            tot += meeting.balance
        tot += 40 * len(self.oneMonth)
        return tot

    def profit(self):
        return [self.monthName,self.revenue(),self.expenses(),self.revenue()-self.expenses()]

    def upfronts(self):
        #returns list of people who have paid upfront for classes this month
        return [x.name for x in self.oneMonth]