requests是python实现的简单易用的HTTP库，使用起来比urllib简洁很多

因为是第三方库，所以使用前需要cmd安装

pip install requests

安装完成后import一下，正常则说明可以开始使用了。

基本用法：

requests.get()用于请求目标网站，类型是一个HTTPresponse类型

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests

response = requests.get('http://www.baidu.com')print(response.status_code)  # 打印状态码print(response.url)          # 打印请求urlprint(response.headers)      # 打印头信息print(response.cookies)      # 打印cookie信息
print(response.text)  #以文本形式打印网页源码print(response.content) #以字节流形式打印
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

运行结果：

状态码：200

url：www.baidu.com

headers信息

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122134110461-359500425.png)

 

 

 各种请求方式：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests

requests.get('http://httpbin.org/get')
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

基本的get请求

```
import requests

response = requests.get('http://httpbin.org/get')
print(response.text)
```

结果

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122134009618-465552772.png)

 

 

 

带参数的GET请求：

第一种直接将参数放在url内

```
import requests

response = requests.get(http://httpbin.org/get?name=gemey&age=22)
print(response.text)
```

结果

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122133803524-838504475.png)

另一种先将参数填写在dict中，发起请求时params参数指定为dict

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests

data = {
    'name': 'tom',
    'age': 20
}

response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

结果同上

 

解析json

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests

response = requests.get('http://httpbin.org/get')
print(response.text)
print(response.json())  #response.json()方法同json.loads(response.text)
print(type(response.json()))
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

结果

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122134451555-536605552.png)

 

简单保存一个二进制文件

二进制内容为response.content

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests

response = requests.get('http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-002.jpg')
b = response.content
with open('F://fengjing.jpg','wb') as f:
    f.write(b)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

为你的请求添加头信息

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests
heads = {}heads['User-Agent'] = 'Mozilla/5.0 ' \                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
 response = requests.get('http://www.baidu.com',headers=headers)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

使用代理

同添加headers方法，代理参数也要是一个dict

这里使用requests库爬取了IP代理网站的IP与端口和类型

因为是免费的，使用的代理地址很快就失效了。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests
import re

def get_html(url):
    proxy = {
        'http': '120.25.253.234:812',
        'https' '163.125.222.244:8123'
    }
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req = requests.get(url, headers=heads,proxies=proxy)
    html = req.text
    return html

def get_ipport(html):
    regex = r'<td data-title="IP">(.+)</td>'
    iplist = re.findall(regex, html)
    regex2 = '<td data-title="PORT">(.+)</td>'
    portlist = re.findall(regex2, html)
    regex3 = r'<td data-title="类型">(.+)</td>'
    typelist = re.findall(regex3, html)
    sumray = []
    for i in iplist:
        for p in portlist:
            for t in typelist:
                pass
            pass
        a = t+','+i + ':' + p
        sumray.append(a)
    print('高匿代理')
    print(sumray)


if __name__ == '__main__':
    url = 'http://www.kuaidaili.com/free/'
    get_ipport(get_html(url))
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

结果：

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122194541774-1887967160.png)

 

 

基本POST请求：

```
import requests

data = {'name':'tom','age':'22'}

response = requests.post('http://httpbin.org/post', data=data)
```

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122210429102-116304094.png)

 

 获取cookie

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#获取cookie
import requests

response = requests.get('http://www.baidu.com')
print(response.cookies)
print(type(response.cookies))
for k,v in response.cookies.items():
    print(k+':'+v)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

结果：

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122210629868-4158822.png)

 

 

会话维持

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests

session = requests.Session()
session.get('http://httpbin.org/cookies/set/number/12345')
response = session.get('http://httpbin.org/cookies')
print(response.text)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

结果：

![img](https://images2017.cnblogs.com/blog/1245324/201711/1245324-20171122211010696-895794942.png)

 

证书验证设置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests
from requests.packages import urllib3

urllib3.disable_warnings()  #从urllib3中消除警告
response = requests.get('https://www.12306.cn',verify=False)  #证书验证设为FALSE
print(response.status_code)打印结果：200
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

超时异常捕获

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests
from requests.exceptions import ReadTimeout

try:
    res = requests.get('http://httpbin.org', timeout=0.1)
    print(res.status_code)
except ReadTimeout:
    print(timeout)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

异常处理

在你不确定会发生什么错误时，尽量使用try...except来捕获异常

所有的requests exception：

## [Exceptions](http://www.python-requests.org/en/master/api/#exceptions)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

try:
    response = requests.get('http://www.baidu.com',timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('timeout')
except HTTPError:
    print('httperror')
except RequestException:
    print('reqerror')
```