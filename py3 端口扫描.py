#依赖python-nmap,openpyxl包 
import json
import time
from multiprocessing import Pool as ThreadPool

import IPy
import nmap
import openpyxl
import requests

#通过调用api接口来获取需要扫描的ip地址，并将其储存为字典r_dict
url_ip = 'http://192.168.37.182/110/asset/public/get_idc_ip'

apikey = 'ce0baa1a417a7f76f449db63895a29dd31758na5'

for i in range(1,12):
    payload_ip = {
        'apikey':apikey,
        'idc':i
    }
    ipj = requests.post(url_ip,data=payload_ip)
    ipj_dict=json.loads(ipj.text, strict=False)
    #字典中key为message的值是我们需要的参数，提取出来并保存
    ip=ipj_dict['message']
#在通过另一个接口获取需要扫描的端口号，也将其储存为字典形式port_dict

#请求api地址

#请求参数
url_port='http://192.168.37.182/110/asset/public/get_danger_ports'
payload_port = {
        'apikey':apikey
    }
portj = requests.post(url_port, data=payload_port)
portj_dict=json.loads(portj.text, strict=False)
#字典中key为message的值是我们需要的参数，提取出来并保存
port=portj_dict['message']

expath='' 
th=20 
#扫描端口 #port='1521,1158,2100,3306,1433,1434,5000,5432,27017,6379,11211,80,8080,443,8000,8081,7001,9080,9090,22,23,10027,3389,5631,111,6000,135,445,139,21,25,110,69,161,162,53,5901,5902,2601-2609 ' 
#默认命令 
arg='-Pn -T4' 


    # 返回url列表 
        #获得地址段 
        #url=eachline.rsplit()[0] 
        # add=IPy.IP(url)#地址段列表 
        # for u in add: 
        #     ip=u.__str__(); 
        #     urlList.append(ip)

def scan(info): 
    ip=info['ip'] 
    port=info['port'] 
    print(ip+'扫描开始') 
    scanner=nmap.PortScanner()
    
    ret=scanner.scan(hosts=ip,ports=port,arguments=arg) 
    state=scanner[ip].state() 
    tcp_ports=scanner[ip].all_tcp() 
    print(ip+' '+state) 
    for ports in tcp_ports: 
        if scanner[ip]['tcp'][ports]['state'] =='open' : 
            st=ip+' '+str(ports)+' '+scanner[ip]['tcp'][ports]['name']+' '+scanner[ip]['tcp'][ports]['state']+'\n'  
            print(st) 
    # print(res) 
    
if __name__ == '__main__': 
    print('----------------扫描开始-------------------') 
    start=time.time() 
    pool = ThreadPool(th)  
    pool.map(scan,ip) 
    pool.close() 
    pool.join() 
    finish=time.time() 
    print('----------------扫描完成-------------------') 
    t=finish-start 
    print('用时 %f'%t)

    
    # makeEx() 
    # info={[ip':'135.233.115.55','port':'22,23,21,80,3389,5901,5902','arg':'-Pn -sV -T4'}me+' '+str(ports)+' '+scanner[ip]['tcp'][ports]['name']+' '+scanner[hostNam
