# 获取ip地址
from urllib.request import urlopen

IPV4_API = "https://api-ipv4.ip.sb/ip"
IPV6_API = "https://api-ipv6.ip.sb/ip"

def getIpv4():
    ip = urlopen(IPV4_API).read()  # 使用IP.SB的接口获取ipv4地址
    ipv4 = str(ip, encoding='utf-8').strip()
    print("获取到IPv4地址：%s" % ipv4)
    return ipv4

def getIpv6():
    ip = urlopen(IPV6_API).read()  # 使用IP.SB的接口获取ipv6地址
    ipv6 = str(ip, encoding='utf-8').strip()
    print("获取到IPv6地址:%s" % ipv6)
    return ipv6