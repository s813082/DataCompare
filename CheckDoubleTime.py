from config import AccessConfig , EformConfig
from datetime import date
import pymssql
import DataModel

# get AccessData
conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
cursor = conn.cursor()
cursor.execute("select t_room, CONCAT(t_begindate,' ',t_begintime) as START_DT, CONCAT(t_enddate,' ',t_EndTime)as END_DT from WistronMRBooking  where t_PK in ('6218D8B6-C625-42EE-AAAB-EAA175F6B322','B9A2EF07-FA63-40EA-AC57-591454601845','406B80B4-63F6-456E-A6AA-BBDC0EA2FA2C','9687D4FD-8DDD-4D34-9F24-FEC1E6332B21','4DBFBC1C-EB5E-4E04-9511-6098A98F2C47','E0A1A2E2-3C7A-4150-B475-3F28A0939CDA','D9230D3F-48C5-4277-9CB8-06BD2E206D18','D0B2C0CB-0B1C-48A9-9930-30B3DECE9631')")
# Access = dict()
# rawdata = cursor.fetchall()

for row in cursor:
    print(row)

# for row in rawdata:
#     if row[0] in Access:
#         Access[row[0]] = Access[row[0]] + "|" +row[1]
#     else:
#         Access[row[0]] = row[1]

# for RoomID in Access:
#     Access[RoomID] = Access[RoomID].split('|')


# get EformData
conn = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
cursor = conn.cursor()
cursor.execute("select resource_id,start_dt , end_dt from[BOK2_APPLICATION] where resource_id like  'B3VIP%' and start_dt > '2020-02-19' order by start_dt desc ")




# Compare two data