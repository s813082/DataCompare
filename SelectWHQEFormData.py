import pymssql
import EformConfig 

def GetEformData():
    conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT UPPER(booking) FROM  BOK2_APPLICATION WHERE resource_id like 'B3VIP%' and booking is not null ORDER BY APPLICATION_ID")
    # cursor.execute("select UPPER(booking) from BOK2_APPLICATION where   booking = '67162FEB-8AC4-4DD0-AB54-709DE8EEC05E'")
    EformDB = []

    for row in cursor:
        EformDB.append(row[0])
    # print("================================================================")
    # print(EformDB)
    # print("================================================================")

    return EformDB

def InsertMissingData(Data):
    conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
    cursor = conn.cursor()
    concatData =''
    # Get max application ID
    cursor.execute(
        "SELECT "+
        "MAX(APPLICATION_ID) "+
        "FROM BOK2_APPLICATION "+
        "WHERE APPLY_DT = (SELECT MAX(APPLY_DT) FROM BOK2_APPLICATION)"
        )
    maxid = cursor.fetchone()
    ID = maxid[0]

    print("MAX ID",ID)
    print("===========================================")
    for a in range(len(Data)):
        Data[a].ID = int(ID)+1+a
        
        # concatData = "\'"+str(Data[a].ID)+"','"+Data[a].Resource_ID+"','"+Data[a].USERID+"','"+Data[a].START_DT+"','"+Data[a].END_DT+"','"+Data[a].APPLY_DT+"','"+Data[a].FullName+"','"+str(Data[a].Booking)+","+Data[a].Review_Status+"\'"
        # if a != (len(Data)-1):
        #     concatData = concatData + "," 
        cursor.execute("INSERT INTO [WHQMeetingRoom2].[dbo].[BOK2_APPLICATION] ([APPLICATION_ID] , [RESOURCE_ID]     , [USERID]          , [START_DT]        , [END_DT]          , [APPLY_DT]        , [REVIEW_STATUS]   , [FullName]        , [Booking])         VALUES ('"+str(Data[a].ID)+"','"+Data[a].Resource_ID+"','"+Data[a].USERID+"','"+Data[a].START_DT+"','"+Data[a].END_DT+"','"+Data[a].APPLY_DT+"','"+Data[a].Review_Status+"','"+Data[a].FullName+"','"+str(Data[a].Booking)+"')")     
        conn.commit()
        print(str(Data[a].Booking)+" insert succefully")
        print("===========================================")
        
    print()