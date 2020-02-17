import SelectWHQAccessData
import SelectWHQEFormData
import LogtoFile,sys
from datetime import datetime

ProgramStartTime = datetime.now()

NotExit = []
LogtoFile.LoggingMSG("========="+str(ProgramStartTime)+"========")
LogtoFile.LoggingMSG("Program start...")
# LogtoFile.LoggingMSG("===========================================")
try:
    LogtoFile.LoggingMSG("Get Access Data")
    AccessDB = SelectWHQAccessData.GetAccessData()
    LogtoFile.LoggingMSG("Get EForm Data")
    EfromDB = SelectWHQEFormData.GetEformData()
except Exception as GetData:
    LogtoFile.LoggingMSG("Get Data Fail : "+str(GetData))
    ErrorStop = datetime.now()
    LogtoFile.LoggingMSG("========="+str(ErrorStop)+"========")
    sys.exit(0)

# LogtoFile.LoggingMSG("===========================================")
LogtoFile.LoggingMSG("Start check if QRCODE is exit in EFormDB")

try:
    for check in AccessDB:
        response = check in EfromDB
        if response == False:
            LogtoFile.LoggingMSG("QRCode {"+check+"} is not exit in EForm database")
            NotExit.append(check)

    LogtoFile.LoggingMSG("Finish check Here is "+str(len(NotExit))+" data not in EForm")
except Exception as CompareData:
    LogtoFile.LoggingMSG("CompareData Fail : "+str(CompareData))
    ErrorStop = datetime.now()
    LogtoFile.LoggingMSG("========="+str(ErrorStop)+"========")
    sys.exit(0)

# LogtoFile.LoggingMSG("===========================================")
try:
    LogtoFile.LoggingMSG("beginning to get missing data")

    if len(NotExit) != 0:
        InsertData = SelectWHQAccessData.GetMissingData(NotExit)
        LogtoFile.LoggingMSG("Try Insert missing data")
        SelectWHQEFormData.InsertMissingData(InsertData)
        InsertFinishTime = datetime.now()
        LogtoFile.LoggingMSG("========="+str(InsertFinishTime)+"========")
    else:
        NoDataEndTime = datetime.now()
        LogtoFile.LoggingMSG("There is no missing data~~")
        LogtoFile.LoggingMSG("========="+str(NoDataEndTime)+"========")

except Exception as InsertData:
    LogtoFile.LoggingMSG("InsertData Fail : "+str(InsertData))
    ErrorStop = datetime.now()
    LogtoFile.LoggingMSG("========="+str(ErrorStop)+"========")
    sys.exit(0)


