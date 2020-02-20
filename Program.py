import SelectWHQAccessData
import SelectWHQEFormData
import CheckDoubleTime
import LogtoFile,sys
import decimal
from os import system
from datetime import datetime,date,timedelta

ProgramStartTime = datetime.now()


LogtoFile.LoggingMSG("========="+str(ProgramStartTime)+"========")
LogtoFile.LoggingMSG("Program start...")
# LogtoFile.LoggingMSG("===========================================")
NotExit = []
Today = date.today()
Yesterday = Today - timedelta(days=1)

strYesterday = Yesterday.strftime("%Y-%m-%d")
strToday = Today.strftime("%Y-%m-%d")
try:
    LogtoFile.LoggingMSG("Get Access Data")
    AccessDB = SelectWHQAccessData.GetAccessData(strToday,strYesterday)
    LogtoFile.LoggingMSG("Get EForm Data")
    EfromDB = SelectWHQEFormData.GetEformData(strToday)
except Exception as GetData:
    LogtoFile.WarningMSG("Get Data Fail : "+str(GetData))
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

    NotExit = CheckDoubleTime.CompareIfExit(NotExit)        
    LogtoFile.LoggingMSG("Finish check Here is "+str(len(NotExit))+" data not in EForm")
except Exception as CompareData:
    LogtoFile.WarningMSG("CompareData Fail : "+str(CompareData))
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
    LogtoFile.WarningMSG("InsertData Fail : "+str(InsertData))
    ErrorStop = datetime.now()
    LogtoFile.LoggingMSG("========="+str(ErrorStop)+"========")
    sys.exit(0)


# system('pause')

