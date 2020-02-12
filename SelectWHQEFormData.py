import pymssql
import EformConfig 

def GetEformData():
    conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT booking FROM  BOK2_APPLICATION WHERE resource_id like 'B3VIP%' and booking is not null ORDER BY APPLICATION_ID")

    EformDB = []

    for row in cursor:
        EformDB.append(row[0])
    print("================================================================")
    print(EformDB)
    print("================================================================")
