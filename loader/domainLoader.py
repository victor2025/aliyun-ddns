# 加载domain
import csv
import logging

# 域名加载器
class DomainLoader:

    def __init__(self, filename="Domains.csv"):
        self.__filename = filename
        self.__domain_list = []
        self.load()

    def load(self):
        try:
            with open(self.__filename, "rt") as file:
                csvFile = csv.DictReader(file)
                for row in csvFile:
                    info = DomainInfo()
                    info.domain = row[DomainInfo.DOMAIN]
                    info.ipv4 = int(row[DomainInfo.IPV4])
                    info.ipv6 = int(row[DomainInfo.IPV6])
                    info.name_ipv4 = row[DomainInfo.NAME_IPV4].split(" ")
                    info.name_ipv6 = row[DomainInfo.NAME_IPV6].split(" ")
                    self.__domain_list.append(info)
        except:
            logging.error("{} error!!!".format(self.__filename))
            exit(0)

    def getDomainList(self):
        return self.__domain_list


class DomainInfo:
    DOMAIN = "domain"
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    NAME_IPV4 = "name_ipv4"
    NAME_IPV6 = "name_ipv6"

    def __init__(self):
        self.domain = ""
        self.ipv4 = 1
        self.ipv6 = 1
        self.name_ipv4 = []
        self.name_ipv6 = []