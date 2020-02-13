import pymssql
import AccessConfig,DataModel
from datetime import date,timedelta

def GetAccessData():
    conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
    cursor = conn.cursor()
    Today = date.today()
    Yesterday = Today - timedelta(days=1)

    strYesterday = Yesterday.strftime("%Y-%m-%d")
    strToday = Today.strftime("%Y-%m-%d")

    # cursor.execute("select  B.t_Room,  B.t_BeginDate,  B.t_EndDate,  B.t_BeginTime,  B.t_EndTime,  E.t_CreateDate from WistronMRBooking B inner join OGEmp E on B.t_PK = E.t_PK order by t_CreateDate desc")
    cursor.execute("SELECT  convert(nvarchar(50), B.t_PK) FROM WistronMRBooking B INNER JOIN OGEmp E  ON B.t_PK = E.t_PK  where t_CreateDate >'"+strYesterday+"'  and t_CreateDate < '"+strToday+"' ORDER BY t_CreateDate DESC;")
    # cursor.execute("select convert(nvarchar(50), t_PK) from WistronMRBooking where t_PK = '67162FEB-8AC4-4DD0-AB54-709DE8EEC05E'")
    AccessDB = []

    for row in cursor:
        AccessDB.append(row[0])
    # print("================================================================")
    # print(AccessDB)
    # print("================================================================")

    return AccessDB

def GetMissingData(NotExit):
    strNotExit = '\',\''.join(NotExit)
    strNotExit = "'"+strNotExit+"'"

    conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
    cursor = conn.cursor()
    InsertData = []
    cursor.execute("select  t_Room,  t_BeginDate,  t_EndDate,  t_BeginTime,  t_EndTime from WistronMRBooking where t_PK in ("+strNotExit+")")
    for data in cursor:
        a = DataModel.BookingDetail(0,data[0],data[1],data[2],data[3],data[4])
        InsertData.append(a)
    return InsertData
