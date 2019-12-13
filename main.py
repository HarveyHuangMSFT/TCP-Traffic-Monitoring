# you have to install 'py -m pip install ip2geotools'
# you have to install 'py -m pip install scapy'

from scapy.all import *
from ip2geotools.databases.noncommercial import DbIpCity
print("this program will take a few minutes to run")
print("please try reloading a web-page for it to load faster")

fob = open("IP.txt","w")

def ip_dst(pkt):
        fob.write(pkt[IP].dst+'\n')

sniff(filter='ip',count=100,prn=ip_dst)
fob.close()


myfile = open("IP.txt", "r")
ip_list = myfile.readlines()


for ip in ip_list:
    new_ip = ip.replace("\n","")
    print(new_ip)
    try:
        response = DbIpCity.get(new_ip,api_key="free")
        print(response.city)
        print(response.country)

    except Exception as e: print("This IP does not have a location")
