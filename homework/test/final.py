import requests
from bs4 import BeautifulSoup
import sqlite3
import requests.packages.urllib3
import matplotlib.pyplot as plt
requests.packages.urllib3.disable_warnings()

#連接資料庫位置
conn = sqlite3.connect('C:\\Users\\hk416\\Desktop\\110810403蘇彥華.db')
c = conn.cursor()

#從金門航空站爬蟲
url = 'https://www.kma.gov.tw/BulletinBoard/StatPassenger.aspx?1=1&MenuID=423'
res = requests.get(url,verify=False)
sp = BeautifulSoup(res.text,'lxml')
datas = sp.find("table",{"class":"TableList"})
datab = datas.find_all("tr")

datab.pop(0)

#將歷年旅客人數統計存入資料庫
for data3 in datab:
    values1 = list(data3.stripped_strings)
    
    c.execute('insert into count_table(年度,一月,二月,三月,四月,五月,六月,七月,八月,九月,十月,十一月,十二月,統計) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',values1)
    print(values1)

conn.commit()
conn.close()
