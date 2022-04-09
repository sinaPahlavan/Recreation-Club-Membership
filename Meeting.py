class Meeting:
    def __init__(self,title):
        self.__title = title

        #change 1 and 0 to true and false
        self.__attendees = []


    def addAttendee(self,memberObj):
        self.__attendees.append(memberObj)

