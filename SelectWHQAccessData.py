import pymssql
import AccessConfig 
from datetime import date,timedelta

def GetAccessData():
    conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
    cursor = conn.cursor()
    Today = date.today()
    Yesterday = Today - timedelta(days=1)

    strYesterday = Yesterday.strftime("%Y-%m-%d")
    strToday = Today.strftime("%Y-%m-%d")

    #cursor.execute("select  B.t_Room,  B.t_BeginDate,  B.t_EndDate,  B.t_BeginTime,  B.t_EndTime,  E.t_CreateDate from WistronMRBooking B inner join OGEmp E on B.t_PK = E.t_PK order by t_CreateDate desc")
    cursor.execute("SELECT  convert(nvarchar(50), B.t_PK) FROM WistronMRBooking B INNER JOIN OGEmp E  ON B.t_PK = E.t_PK  where t_CreateDate >'"+strYesterday+"'  and t_CreateDate < '"+strToday+"' ORDER BY t_CreateDate DESC;")

    AccessDB = []

    for row in cursor:
        AccessDB.append(row[0])
    print("================================================================")
    print(AccessDB)
    print("================================================================")

