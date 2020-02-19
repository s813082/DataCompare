import logging
from datetime import date

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# FileName = 'log/'+str(date.today())+'.log'
FileName = str(date.today())
logging.basicConfig(level=logging.DEBUG, filemode='a', filename=FileName, format=FORMAT, datefmt=DATE_FORMAT )

def LoggingMSG(Messsage):
    logging.info(Messsage)
    print(Messsage)

def WarningMSG(Message):
    logging.warning(Message)
    print(Message)