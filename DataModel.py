class BookingDetail:
    def __init__(self,ID,RoomID,BeginDate,EndDate,BeginTime,EndTime):
        super().__init__()
        self.ID = ID
        self.RoomID = RoomID
        self.BeginDate = BeginDate
        self.EndDate = EndDate
        self.BeginTime = BeginTime
        self.EndTime = EndTime
        self.FullName = "此單由系統填上"    