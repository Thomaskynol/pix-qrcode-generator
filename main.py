# Imports
import crcmod
import qrcode

# Functions
class payload():
    def __init__(self, name, key, city, value, txtId):
        self.name = name
        self.key = key
        self.city = city
        self.value = value
        self.txtId = txtId
        
        self.nameLen = len(self.name)
        self.keyLen = len(self.key)
        self.cityLen = len(self.city)
        self.valueLen = len(str(self.value))
        self.txtIdLen = len(self.txtId)
        
        #00 id | 14 len | BR.GOV.BCB.PIX value ++ 01 id | keyLen len | key value
        self.merchantAcountInfo = f'0014BR.GOV.BCB.PIX01{self.keyLen}{self.key}'
        self.merchantAcountLen = len(self.merchantAcountInfo)
        
        self.transactionAmountLen = len(str(self.value))
        if self.transactionAmountLen < 10:
            self.transactionAmountLen = f'0{self.transactionAmountLen}'
        
        self.txtIdLen = len(self.txtId)
        if self.txtIdLen < 10:
            self.txtIdLen = f'0{self.txtIdLen}'
            
        #62 id | len -> | id | len | txtId
        self.txtIdInfo = f'05{self.txtIdLen}{self.txtId}'
        self.txtIdInfoLen = len(self.txtIdInfo)
        if self.txtIdInfoLen < 10:
            self.txtIdInfoLen = f'0{self.txtIdInfoLen}'
        
        # id | len | value
        self.payloadFormat = '000201' # ID 00 | len 02 | value 01
        self.merchantAcount = f'26{self.merchantAcountLen}{self.merchantAcountInfo}' # ID 26 | merchantAcountLen | merchantAcountInfo
        self.merchantCategCode = '52040000' # ID 52 | len 04 | value 0000
        self.transactionCurrency = '5303986' # ID 53 | len 03 | value 986 (BRL)
        self.transactionAmount = f'54{self.transactionAmountLen}{self.value}' # ID 54 | transactionAmountLen | value
        self.contryCode = '5802BR' # ID 58 | len 02 | value BR
        self.merchantName = f'59{self.nameLen}{self.name}' # ID 59 | nameLen | name
        self.merchantCity = f'60{self.cityLen}{self.city}' # ID 60 | cityLen | city
        self.addDataField = f'62{self.txtIdInfoLen}{self.txtIdInfo}' # ID 62 | txtIdInfoLen | txtIdInfo --> | id | len | txtId
        self.crc16 = '6304' # ID 63 | len 04 | value CRC16
        
    def generatePayLoadCode(self):
        payloadInfos = f'{self.payloadFormat}{self.merchantAcount}{self.merchantCategCode}{self.transactionCurrency}{self.transactionAmount}{self.contryCode}{self.merchantName}{self.merchantCity}{self.addDataField}{self.crc16}'
        
        crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        self.crc16Code = hex(crc16(str(payloadInfos).encode('utf-8'))).replace('0x', '').upper()
        
        self.payloadCode = f'{payloadInfos}{self.crc16Code}'
        print(self.payloadCode)
        
        print(f'Pix Copy and Paste::\n{self.payloadCode}')
        self.generateQrCode(self.payloadCode)
        
    def generateQrCode(self, code):
        self.qrcode = qrcode.make(code)
        self.qrcode.save("pix_qr_code.png")
        print("QR Code generated and saved as 'pix_qr_code.png")
        

# callin the class:

#                          name                       key                  city     value     txtId
payloadCool = payload('Michael Jackson', 'michaeljackson123@gmail.com', 'NEW YORK', 10.00, 'division')
payloadCool.generatePayLoadCode()