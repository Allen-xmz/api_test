import time
import hashlib
import base64

datatime = time.strftime("%Y%m%d%H%M%S",time.localtime())
#定义招商支付密钥
# merkey = "JIfjds78BHdio321"
merkey = 'Ntstzqzyyadmin10'

# 待签名的请求参数
# def jsonRequestData(sign="123456"):
#     jsonRequestData = {
#         "version": "1.0",
#         "charset": "UTF-8",
#         "sign": sign,
#         "signType": "SHA-256",
#         "reqData": {
#             "dateTime": datatime,
#             "branchNo": "0531",
#             "merchantNo": "000103",
#             "type": "B",
#             "date": "20190228",
#             "orderNo":"20190228t10417560700000000731373",
#             "operatorNo": "9999"
#         }
#     }
#     return jsonRequestData

def jsonRequestData(sign="123456"):
        jsonRequestData = {
            "version": "1.0",
            "charset": "UTF-8",
            "sign": sign,
            "signType": "SHA-256",
            "reqData":{
			    "dateTime": "20190423153839",
                "date": "20190423",
                "extendInfoEncrypType": "",
                "amount": "0.01",
                "orderNo": "20190423t10415383900000000772853",
                "payNoticePara": "witon",
                "riskLevel": "",
                "cardType": "",
                "mobile": "",
                "merchantSerialNo": "",
                "agrNo": "201809110990000000000000000721",
                "lon": "",
                "extendInfo": "",
                "userID": "28000000000000000082",
                "signNoticePara": "",
                "signNoticeUrl": "",
                "clientIP": "127.0.0.1",
                "expireTimeSpan": "",
                "payNoticeUrl": "http://112.85.122.75:8081/wpay/cmb/notify/p/147.do",
                "returnUrl": "https://web.witontek.com/eHospital2/auth/redirect/payment-payment-result?requestToken=02f68a7317ea4fbeb00bb85bac22834b&interfaceType=&hospital_id=ntstzqzyyadmin&trade_no=EHTS1904230000023655",
                "lat": "",
                "branchNo": "0513",
                "merchantNo": "000012"
            }
        }
        return jsonRequestData

# print(jsonRequestData())

#对字典进行排序
list1 = jsonRequestData()["reqData"].items()
dic = sorted(list1,key=lambda a:a[0],reverse=False)
# print(dic)
"""排序完成后按将所有键值对以“&”符号拼接"""
str1 = ""
for i in dic:
    a = "{}={}&".format(i[0],i[1])
    str1 +=a
str1+=merkey
print("-------:",str1)

"""进行sha256签名运算获得签名结果byte数组，将byte数组转换为16进制"""
# k = hashlib.sha256()
# k.update(str1.encode())
# print(k.digest())
# print("最终签名为:",base64.b16encode(k.digest()))

sign1 = hashlib.sha256(str1.encode()).digest()
sign1 = base64.b16encode(sign1)
print("最终签名为:",sign1)

print(jsonRequestData(sign=sign1))