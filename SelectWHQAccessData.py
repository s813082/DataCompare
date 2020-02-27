import pymssql
import DataModel
from config import AccessConfig
from datetime import date,timedelta
import LogtoFile

def GetAccessData(Today,Yesterday):
    conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
    cursor = conn.cursor()

    # cursor.execute("select  B.t_Room,  B.t_BeginDate,  B.t_EndDate,  B.t_BeginTime,  B.t_EndTime,  E.t_CreateDate from WistronMRBooking B inner join OGEmp E on B.t_PK = E.t_PK order by t_CreateDate desc")
    # cursor.execute("SELECT  convert(nvarchar(50), B.t_PK) FROM WistronMRBooking B INNER JOIN OGEmp E  ON B.t_PK = E.t_PK  where t_CreateDate >'"+Yesterday+"'  and t_CreateDate < '"+Today+"' and t_FinishTime is not null ORDER BY t_CreateDate DESC;")
    cursor.execute("SELECT  convert(nvarchar(50), B.t_PK) FROM WistronMRBooking B INNER JOIN OGEmp E  ON B.t_PK = E.t_PK and t_FinishTime is  null and b.t_begindate > '"+Today+"' ORDER BY t_CreateDate DESC;")

    AccessDB = []

    for row in cursor:
        AccessDB.append(row[0])
    # LogtoFile.LoggingMSG("================================================================")
    # LogtoFile.LoggingMSG(AccessDB)
    # LogtoFile.LoggingMSG("================================================================")

    return AccessDB

def GetMissingData(NotExit):
    strNotExit = '\',\''.join(NotExit)
    strNotExit = "'"+strNotExit+"'"

    conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
    cursor = conn.cursor()
    InsertData = []
    cursor.execute(
        "select B.t_PK as Booking, B.t_Room as RESOURCE_ID , concat(B.t_BeginDate,' ',B.t_BeginTime) as START_DT,  concat(B.t_EndDate,' ',B.t_EndTime) as END_DT,  CONVERT(VARCHAR,E.t_CreateDate,121) as APPLY_DT , SUBSTRING(t_MailContent,5,6) as FullName from WistronMRBooking B ,OGEmp E  where B.t_pk = E.t_pk and B.t_PK in ("+strNotExit+")")
    for data in cursor:
        a = DataModel.BookingDetail(0,data[0],data[1],data[2],data[3],data[4],data[5])
        InsertData.append(a)
    return InsertData
