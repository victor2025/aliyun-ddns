# 主程序，用于阿里云DDNS
from loader.keyLoader import KeyLoader
from loader.domainLoader import DomainLoader
from handler.aliDdnsHandler import DdnsHandler
if __name__=="__main__":
    # 载入配置
    keyLoader = KeyLoader()
    domainLoader = DomainLoader()
    # 开始ddns
    # 初始化handler
    ddnsHandler = DdnsHandler(keyLoader.getId(),keyLoader.getSecret())
    # 开始ddns
    ddnsHandler.batchDdns(domainLoader.getDomainList())
    print("程序执行完毕")
