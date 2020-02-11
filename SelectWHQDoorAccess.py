import pymssql
import AccessConfig 
conn = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
cursor = conn.cursor()
cursor.execute("select B.*, E.t_Number, E.t_Name, E.t_CreateDate from WistronMRBooking B inner join OGEmp E on B.t_PK = E.t_PK order by t_CreateDate desc")

print(row)
