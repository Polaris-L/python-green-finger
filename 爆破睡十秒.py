import requests
import json
#请求api地址

#请求参数
url='http://192.168.37.182/110/asset/public/get_danger_ports'
op='login'   #op='register'
username='polaris-ljj%40qq.com' #需要爆破的用户名
#name='zhuyingye' 
#name字段随意设定
csrfmiddlewaretoken='uAwJNvkPa6i8t8bCLR6B0v0e6Zsy0Mi9'

payload = {
        'csrfmiddlewaretoken':csrfmiddlewaretoken
        'url':url
        'username':username
    }
ret = requests.post(url, data=payload)


print(ret.text)