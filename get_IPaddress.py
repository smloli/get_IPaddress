# Author:52loli
# Time:2020.10.06
import requests
import json

class Ip():
    def __init__(self):
        self.ip_url = 'https://www.toolnb.com/Tools/Api/IP.html'
        self.ipInfo_url = 'https://www.toolnb.com/Tools/Api/ipgetareainfo.html'
        self.headers = {
            'cookie':'PHPSESSID=q8e8vhzg8nsarisdwsbmxb1g72',
            'referer':'https://www.toolnb.com/tools/ipgetareainfo.html',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4183.121 Safari/537.36'
        }
    def get_ip(self):
        self.tmp = requests.post(self.ip_url,headers=self.headers)
        self.result = json.loads(self.tmp.text)
        return self.result['data']['ip']
    def get_IPaddress(self):
        self.data = {'ip': self.get_ip()}
        self.tmp = requests.post(self.ipInfo_url,data = self.data,headers=self.headers)
        self.res = json.loads(self.tmp.text)
        print(self.res['data']['area'])

ip = Ip()
ip.get_IPaddress()
