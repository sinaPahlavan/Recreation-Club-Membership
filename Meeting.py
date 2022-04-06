class Meeting:
    def __init__(self,title,instructorAttends,status):
        self.__title = title
        self.__instructorAttends = instructorAttends #1 instructor is attending and 0
        #change 1 and 0 to true and false
        self.__attendees = []
        self.__status = status #passed or upcoming

    def addAttendee(self,memberObj):
        self.__attendees.append(memberObj)
    def getStatus(self):
        return self.__status