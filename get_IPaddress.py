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
        tmp = requests.post(self.ip_url,headers=self.headers)
        result = json.loads(tmp.text)
        return result['data']['ip']

    def get_IPaddress(self):
        data = {'ip': self.get_ip()}
        tmp = requests.post(self.ipInfo_url,data = data,headers=self.headers)
        res = json.loads(tmp.text)
        print(res['data']['area'])
if __name__ == '__main__':
    ip = Ip()
    ip.get_IPaddress()
