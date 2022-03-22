import requests,base64,logging,time,json
import sys
import argparse
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}



def main(apiurl,output_file):
    apiurl = apiurl + "&size=10000"
    r = requests.get(apiurl,timeout=10)
    r_se = r.text
    result = json.loads(r_se)
    print(result)
    iplist = result['results']
    
    for i in iplist:
        with open(output_file,"a") as a:    #设置文件对象
            str = a.write(i[0] + "\n")
    



if __name__ == "__main__":
    
    Apiurl = str(input("IP url here >>>>>>>"))
    output_file=str(input("filename >>>>>>>"))
    main(Apiurl,output_file)
