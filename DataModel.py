class BookingDetail:
    def __init__(self,ID,Booking,Resource_ID,START_DT,END_DT,APPLY_DT):
        super().__init__()
        self.ID = ID
        self.Booking = Booking
        self.Resource_ID = Resource_ID
        self.START_DT = START_DT
        self.END_DT = END_DT
        self.APPLY_DT = APPLY_DT
        self.FullName = "此時段已被借用" 
        self.USERID = "10612039"
        self.Review_Status = "A"

class CheckDoubleTime:
    def __init__(self,RoomID,Start_DT,End_DT,Booking,Today,Tomorrow):
        super().__init__()
        self.RoomID = RoomID
        self.Start_DT = Start_DT
        self.End_DT = End_DT
        self.Booking = Booking
        self.Today = Today
        self.Tomorrow = Tomorrow
        