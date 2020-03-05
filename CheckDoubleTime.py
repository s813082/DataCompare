from config import AccessConfig , EformConfig
from datetime import date , datetime ,timedelta
import pymssql,LogtoFile
import DataModel

# get AccessData
# CompareData = '6218D8B6-C625-42EE-AAAB-EAA175F6B322','B9A2EF07-FA63-40EA-AC57-591454601845','406B80B4-63F6-456E-A6AA-BBDC0EA2FA2C','9687D4FD-8DDD-4D34-9F24-FEC1E6332B21','4DBFBC1C-EB5E-4E04-9511-6098A98F2C47','E0A1A2E2-3C7A-4150-B475-3F28A0939CDA','D9230D3F-48C5-4277-9CB8-06BD2E206D18','D0B2C0CB-0B1C-48A9-9930-30B3DECE9631'

def CompareIfExit(CompareDataList):

    CompareData = tuple(CompareDataList)
    start =  datetime.now()
    # TESTDATA = 'd9230d3f-48c5-4277-9cb8-06bd2e206d18','0677fb97-52fb-4204-9a1a-0a2c36648034','7dfcb2d2-6f59-4f35-95bf-0af8db16a231','fa1ed9e7-9713-41e6-a436-0ce5ca04bef4','bd67ad30-d2fd-437e-807d-1cfc7ca16f43','a362b6f9-6203-4fe9-a041-1d8e63ce19d3','7701b752-f82c-449d-97c6-1ed99d5a324d','e6834911-1fa5-4839-99b1-2071d835dee7','e27f521f-5ebf-4959-bd3a-2550f7e86f57','75ed694a-29d0-466a-aecc-2645653bc84b','fb6f4784-719c-4fb5-b9f1-26f99deb8816','4f5ad0d7-0ff7-4603-8cff-2d44d4835ada','d0b2c0cb-0b1c-48a9-9930-30b3dece9631','4d50ad05-58b1-4046-8c5b-366d46ebe427','b5f13d8e-80b6-4792-9b6e-3767c7bec7c9','e0a1a2e2-3c7a-4150-b475-3f28a0939cda','ea8ad5ea-53d4-48fe-a3ec-44b62c1c85f4','e9ce62e2-ee1f-46b1-9737-4660fa85c6d9','641260cf-53cb-433c-a4ad-4a0fdc441dbc','0aea0d32-0eae-47c1-8996-4a97a2d96951','ab045ba1-4df0-4a3d-ba64-4cab4ab1fe3f','76b65bc3-7358-4d80-a7e4-4e305929f9f7','d544ae7e-4491-411e-85a0-536c2f354b0f','21f0cb51-54fd-4937-ab4c-57565ece1627','8a484bd7-2bdf-474f-a466-5c1ad4cf943f','4dbfbc1c-eb5e-4e04-9511-6098a98f2c47','0dce4a78-36ad-4c19-8622-6ae1fcc8efd0','efc43a76-93fe-413b-a0c0-6aeb7771da28','8ad4aea9-0599-48ea-ac03-6eb8ffbf337e','f808821f-468b-433b-88f9-6f0265854dd9','107930a7-f43f-4209-8ce0-743e0d546d0f','6d51e6ac-2d8d-4869-8e5d-77a35a5f1d1f','2fc123da-0f88-4176-9769-7da238e8ff6f','95b254a7-fc0b-42f6-b4d3-81810529fc1e','53919051-17c9-46cd-8608-8326fbaba7cc','d91c5894-7cee-4044-97ac-856cc10216b0','be1a6556-799b-4eeb-8fd3-857207593c59','119bfe10-1727-4e1e-8297-859bf1097be1','550f64c9-889a-40c1-a5eb-8762edaa9e6f','ad1eba77-1710-4c48-a57b-88786cee1e4e','7a52d9aa-8c3f-4cc4-9792-8a6753617dfa','a74c7086-762a-46ee-855a-8d2c9494ab36','4115319b-a68c-4b8b-bea2-8dc17f0dc164','794af9dd-35cb-4736-a840-909d043fe7dd','e36c7de6-b7eb-4b83-91a1-94dab517ebd3','208f8e29-fe34-4d0f-84fb-96618e3b7f4d','e89dcb63-9577-4c31-bd45-96c2f634ddbe','48aa4aa1-4a0d-4bd1-8564-9916d63359c9','65176168-0144-4c4e-8469-99ff72f30e51','43355e2b-7110-4bcb-b133-9fc3f906eef6','c9df6f06-68a7-4174-8185-a08aab14fcff','3333dc60-602d-4850-b91e-a0e0cd3b705e','755d97c7-b760-40a9-ba23-a4dd92cbe216','ad6aff6f-5c3a-4143-8a25-a579bb3e8d92','874fd852-e727-4403-af02-abcb4fad5514','0f770889-c0c6-4aaf-a39b-ada16b9cd5fd','84447d84-ebbc-4ccd-8e01-b6b2fc80b1b9','42da4314-4f1c-4346-bc4b-b6d99932beea','f0453d76-85fc-45dd-b839-bb5883fd41e0','45ce3d73-4ba0-4264-8d97-c2ebf94ddb3e','99a07d3a-ecad-4bc3-8c6a-c8e0aad4fc04','cbf691bd-bb47-4655-a52c-cc779ea5304c','cfddfe22-71ee-4ec3-8311-cfc04585a25a','f626e45c-2ffd-4d1f-a835-d65e4b089988','db782168-f029-4f75-9419-d849ead76454','805e5f56-b162-487f-847a-d86038b680e4','3ef5c31c-08aa-4a49-872e-daf21ec3e763','fe129d1c-d502-4619-a69e-db5dfdb9c0f0','86997c8c-9152-4386-afed-df6be71ae462','fecef3f2-ff8c-4781-ba7b-e544648d48cd','d6c02c92-37b5-4e92-a627-e8530fed530b','ee069f7a-b0e9-4f60-9de1-e8ac49f5da91','a0c14c7c-1cdc-413f-8e63-eedaa54dbe29','85cec105-ecb4-4ded-b152-efdf0d714bdd','1d86462d-7368-41d8-b930-f1606ce4b672','d0758872-6444-4856-ad51-f44839d84b10','87ef798c-44c6-4313-98b9-f517ab93be65','cef29334-56b3-4370-89c0-fc3aedaaa871','30eb127c-2712-45b5-a646-fcb01f7658cd'
    connAccess = pymssql.connect(AccessConfig.SERVER,AccessConfig.UID, AccessConfig.PWD, AccessConfig.DATABASE)
    cursorAccess = connAccess.cursor()
    cursorAccess.execute("select t_room, CONCAT(t_begindate,' ',t_begintime) as START_DT, CONCAT(t_enddate,' ',t_EndTime)as END_DT , t_PK , t_BeginDate as Today , DateAdd(day,1,t_BeginDate) as Tomorrow from WistronMRBooking  where t_PK in "+str(CompareData)+"")

    connEform = pymssql.connect(EformConfig.SERVER,EformConfig.UID, EformConfig.PWD, EformConfig.DATABASE)
    cursorEform = connEform.cursor()

    ListData = list(CompareData)

    for row in cursorAccess:
        a = DataModel.CheckDoubleTime(row[0],row[1],row[2],str(row[3]),row[4],row[5])
        # cursorEform.execute("SELECT * FROM [BOK2_APPLICATION] WHERE resource_id = '"+a.RoomID+"' AND START_DT BETWEEN '"+a.Today+"' AND'"+a.Tomorrow+"' AND ((start_dt BETWEEN '"+a.Start_DT+"' AND '"+a.End_DT+"' OR end_dt BETWEEN '"+a.Start_DT+"' AND '"+a.End_DT+"') OR (START_DT < '"+a.Start_DT+"' OR END_DT >'"+a.End_DT+"'))")
        # SELECT_SQL = "SELECT * FROM [BOK2_APPLICATION] WHERE resource_id = '"+a.RoomID+"' and ((end_dt > '"+a.Start_DT+"' and end_dt < '"+a.End_DT+"') or (start_dt > '"+a.Start_DT+"' and start_dt< '"+a.End_DT+"') or (start_dt <= '"+a.Start_DT+"' and end_dt >='"+a.End_DT+"'))"
        # LogtoFile.LoggingMSG(SELECT_SQL)
        cursorEform.execute("SELECT * FROM [BOK2_APPLICATION] WHERE resource_id = '"+a.RoomID+"' and ((end_dt > '"+a.Start_DT+"' and end_dt < '"+a.End_DT+"') or (start_dt > '"+a.Start_DT+"' and start_dt< '"+a.End_DT+"') or (start_dt <= '"+a.Start_DT+"' and end_dt >='"+a.End_DT+"'))")
        count = cursorEform.fetchall()
        if len(count) > 0:
            ListData.remove(a.Booking.upper())
            
    end = datetime.now()       
    print(start)
    print(end)
    return ListData