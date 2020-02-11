import pymssql
import EformConfig 
conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
cursor = conn.cursor()
cursor.execute("SELECT booking FROM  BOK2_APPLICATION WHERE resource_id like 'B3VIP%' and booking is not null ORDER BY APPLICATION_ID")

EformDB = []

for row in cursor:
    EformDB.append(row[0])

print('bb7fb603-b733-4108-8e48-1404be9fe3142536' in EformDB)