import SelectWHQAccessData
import SelectWHQEFormData
    
NotExit = []

print("Program start...")
print("===========================================")
print("Get Access Data")
AccessDB = SelectWHQAccessData.GetAccessData()
print("Get EForm Data")
EfromDB = SelectWHQEFormData.GetEformData()

print("===========================================")
print("Start check if QRCODE is exit in EFormDB")

for check in AccessDB:
    response = check in EfromDB
    if response == False:
        print("QRCode {"+check+"} is not exit in EForm database")
        NotExit.append(check)

print("Finish check Here is ",len(NotExit)," data not in EForm")
print("===========================================")
print("beginning to get missing data")
InsertData = SelectWHQAccessData.GetMissingData(NotExit)
print("Try Insert missing data")
SelectWHQEFormData.InsertMissingData(InsertData)
