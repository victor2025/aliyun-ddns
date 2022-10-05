# Python实现阿里云域名DDNS支持ipv4和ipv6

## 依赖安装

#### 需要安装的依赖
````commandline
pip install aliyun-python-sdk-core-v3
pip install aliyun-python-sdk-domain
pip install aliyun-python-sdk-alidns
pip install requests
````
#### 导出依赖列表
````commandline
pipreqs . encoding=utf-8 --force
````

#### 安装依赖
````commandline
pip install -r requirements.txt
````

## 配置文件
程序运行需要两个配置文件
#### AccessKey.csv 访问密钥
````csv
AccessKey ID,AccessKey Secret
your id,your secret
````

#### Domains.csv 解析地址
````csv
domain,ipv4,ipv6,name_ipv4,name_ipv6
your domain,(0/1),(0/1),sub domains,sub domains
````