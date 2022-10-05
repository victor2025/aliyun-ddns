from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
import json
from loader.domainLoader import DomainInfo
from handler import ipHandler

class DdnsHandler:

    def __init__(self, id, secret, region='cn-hangzhou'):
        self.__client = AcsClient(id, secret, region)
        self.__ipv4 = None
        self.__ipv6 = None

    # ddns for batch domain
    def batchDdns(self, domainList: list):
        for info in domainList:
            self.ddns(info)

    # ddns for single domain
    def ddns(self, info: DomainInfo):
        # parse __ipv4
        if (info.ipv4 == 1):
            # 获取ip地址
            if (self.__ipv4 == None):
                self.__ipv4 = ipHandler.getIpv4()
            # parse
            self.ddnsIpv4(info)
        # parse __ipv6
        if (info.ipv6 == 1):
            if (self.__ipv6 == None):
                self.__ipv6 = ipHandler.getIpv6()
            # parse
            self.ddnsIpv6(info)

    def ddnsIpv4(self, info: DomainInfo):
        domain = info.domain
        name_ipv4 = info.name_ipv4

        for sub_name_ipv4 in name_ipv4:
            request = DescribeSubDomainRecordsRequest()
            request.set_accept_format('json')
            request.set_DomainName(domain)
            request.set_SubDomain(sub_name_ipv4 + '.' + domain)
            response = self.__client.do_action_with_exception(request)  # 获取域名解析记录列表
            domain_list = json.loads(response)  # 将返回的JSON数据转化为Python能识别的
            whole_name = sub_name_ipv4+"."+domain

            if domain_list['TotalCount'] == 0:
                self.add(domain, sub_name_ipv4, "A", self.__ipv4)
                print("新建域名解析成功(%s)" % whole_name)
            elif domain_list['TotalCount'] == 1:
                if domain_list['DomainRecords']['Record'][0]['Value'].strip() != self.__ipv4.strip():
                    self.update(domain_list['DomainRecords']['Record'][0]['RecordId'], sub_name_ipv4, "A", self.__ipv4)
                    print("修改域名解析成功(%s)" % whole_name)
                else:
                    print("IPv4地址未发生变化(%s)" % whole_name)
            elif domain_list['TotalCount'] > 1:
                from aliyunsdkalidns.request.v20150109.DeleteSubDomainRecordsRequest import DeleteSubDomainRecordsRequest

                request = DeleteSubDomainRecordsRequest()
                request.set_accept_format('json')
                request.set_DomainName(domain)  # https://www.kaikaiclub.top
                request.set_RR(sub_name_ipv4)
                response = self.__client.do_action_with_exception(request)
                self.add(domain, sub_name_ipv4, "A", self.__ipv4)
                print("修改域名解析成功(%s)" % whole_name)

    def ddnsIpv6(self, info: DomainInfo):
        domain = info.domain
        name_ipv6 = info.name_ipv6

        for sub_name_ipv6 in name_ipv6:
            request = DescribeSubDomainRecordsRequest()
            request.set_accept_format('json')
            request.set_DomainName(domain)
            request.set_SubDomain(sub_name_ipv6 + '.' + domain)
            response = self.__client.do_action_with_exception(request)  # 获取域名解析记录列表
            domain_list = json.loads(response)  # 将返回的JSON数据转化为Python能识别的
            whole_name = sub_name_ipv6+"."+domain

            if domain_list['TotalCount'] == 0:
                self.add(domain, sub_name_ipv6, "AAAA", self.__ipv6)
                print("新建域名解析成功(%s)" % whole_name)
            elif domain_list['TotalCount'] == 1:
                if domain_list['DomainRecords']['Record'][0]['Value'].strip() != self.__ipv6.strip():
                    self.update(domain_list['DomainRecords']['Record'][0]['RecordId'], sub_name_ipv6, "AAAA", self.__ipv6)
                    print("修改域名解析成功(%s)" % whole_name)
                else:
                    print("IPv6地址未发生变化(%s)" % whole_name)
            elif domain_list['TotalCount'] > 1:
                from aliyunsdkalidns.request.v20150109.DeleteSubDomainRecordsRequest import \
                    DeleteSubDomainRecordsRequest

                request = DeleteSubDomainRecordsRequest()
                request.set_accept_format('json')
                request.set_DomainName(domain)
                request.set_RR(sub_name_ipv6)  # https://blog.zeruns.tech
                response = self.__client.do_action_with_exception(request)
                self.add(domain, sub_name_ipv6, "AAAA", self.__ipv6)
                print("修改域名解析成功(%s)" % whole_name)

    def update(self, RecordId, RR, Type, Value):  # 修改域名解析记录
        from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
        request = UpdateDomainRecordRequest()
        request.set_accept_format('json')
        request.set_RecordId(RecordId)
        request.set_RR(RR)
        request.set_Type(Type)
        request.set_Value(Value)
        response = self.__client.do_action_with_exception(request)

    def add(self, DomainName, RR, Type, Value):  # 添加新的域名解析记录
        from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
        request = AddDomainRecordRequest()
        request.set_accept_format('json')
        request.set_DomainName(DomainName)
        request.set_RR(RR)
        request.set_Type(Type)
        request.set_Value(Value)
        response = self.__client.do_action_with_exception(request)
