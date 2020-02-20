import pymssql
from config import EformConfig
from datetime import datetime,date
import LogtoFile

Today = str(date.today())
print(Today)
def GetEformData(Today):
    conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
    cursor = conn.cursor()
    # cursor.execute("SELECT UPPER(booking) FROM  BOK2_APPLICATION WHERE resource_id like 'B3VIP%' and booking is not null ORDER BY APPLICATION_ID")
    cursor.execute("select UPPER(booking) from BOK2_APPLICATION where  booking <> '' and START_DT > '"+Today+"'")
    EformDB = []

    for row in cursor:
        EformDB.append(row[0])
    # LogtoFile.LoggingMSG("================================================================")
    # LogtoFile.LoggingMSG(EformDB)
    # LogtoFile.LoggingMSG("================================================================")

    return EformDB

def InsertMissingData(Data):
    conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
    cursor = conn.cursor()
    concatData =''
    # Get max application ID
    cursor.execute(
        "SELECT "+
        "MAX(CONVERT(INT,APPLICATION_ID)) "+
        "FROM BOK2_APPLICATION "
        )
    maxid = cursor.fetchone()
    ID = maxid[0]
    LogtoFile.LoggingMSG("MAX ID = "+str(ID))
    # LogtoFile.LoggingMSG("===========================================")
    for a in range(len(Data)):
        Data[a].ID = ID+1+a
        
        # concatData = "\'"+str(Data[a].ID)+"','"+Data[a].Resource_ID+"','"+Data[a].USERID+"','"+Data[a].START_DT+"','"+Data[a].END_DT+"','"+Data[a].APPLY_DT+"','"+Data[a].FullName+"','"+str(Data[a].Booking)+","+Data[a].Review_Status+"\'"
        # if a != (len(Data)-1):
        #     concatData = concatData + "," 
        cursor.execute("INSERT INTO [WHQMeetingRoom2].[dbo].[BOK2_APPLICATION] ([APPLICATION_ID] , [RESOURCE_ID]     , [USERID]          , [START_DT]        , [END_DT]          , [APPLY_DT]        , [REVIEW_STATUS]   , [FullName]        , [Booking])         VALUES ('"+str(Data[a].ID)+"','"+Data[a].Resource_ID+"','"+Data[a].USERID+"','"+Data[a].START_DT+"','"+Data[a].END_DT+"','"+Data[a].APPLY_DT+"','"+Data[a].Review_Status+"','"+Data[a].FullName+"','"+str(Data[a].Booking)+"')")     
        conn.commit()
        LogtoFile.LoggingMSG(str(Data[a].Booking)+" insert succefully")
        
        