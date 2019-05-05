import time
import hashlib
import base64


datatime = time.strftime("%Y%m%d%H%M%S",time.localtime())

key = "key=123456"

JS = {
    "hospital_id":"jnyxyfsyyyzyqadmin",
    "trade_no":"EH2354768979098",
    "biz_id":"201710191231233",
    "order_amount":"0.01",
    "ty":""
    }

#对字典进行排序
list1 = JS.items()
dic = sorted(list1,key=lambda a:a[0],reverse=False)
print(dic)
"""排序完成后按将所有键值对以“&”符号拼接"""
str1 = ""
for i in dic:
    a = "{}={}&".format(i[0],i[1])
    if i[1] == "":
        continue
    else:
        str1 +=a
str1+=key
print(str1)
#创建 MD5对象
h = hashlib.md5()
#更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
# md5_obj=hashlib.md5(str1.encode("utf-8")) 效果一样
h.update(str1.encode("utf-8"))
print("sign为：",h.hexdigest().upper())










# """进行sha256签名运算获得签名结果byte数组，将byte数组转换为16进制"""
# # k = hashlib.sha256()
# # k.update(str1.encode())
# # print(k.digest())
# # print("最终签名为:",base64.b16encode(k.digest()))

# sign1 = hashlib.sha256(str1.encode()).digest()
# sign1 = base64.b16encode(sign1)
# print("最终签名为:",sign1)