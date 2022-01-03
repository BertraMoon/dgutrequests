# dgut-requests
[![dugt-requests](https://img.shields.io/pypi/v/dgut-requests?color=blue)](https://pypi.org/project/dgut-requests)
[![Build Status](https://travis-ci.org/BertraMoon/dgut-requests.svg?branch=master)](https://travis-ci.org/BertraMoon/dgut-requests)
[![README](https://img.shields.io/badge/README-Chinese-brightgreen)](https://github.com/BertraMoon/dgut-requests/blob/master/README.md)
[![GitHub](https://img.shields.io/github/license/bertramoon/dgut-requests)](https://github.com/BertraMoon/dgut-requests/blob/master/LICENSE)  


# 0. 前言

dgut-requests是一款适用于东莞理工学院系统的Python库（要求Python3.7及以上版本），是对基本请求库进行再抽象并实现所需功能，采用面向切面编程(AOP)，目前基于该库已做出勤工俭学自动考勤、疫情防控自动打卡、出入校快速申请等小应用。 

这是一篇面向编程新手的帮助文档，我会通过例子向你展示这个库的功能。如果你不熟悉dgut-requests库，请从头开始完整阅读本文档，并在自己的电脑上尝试运行一下（PS：演示所使用的操作系统是windows 10）。如果你有编程基础，并且对Python语言比较熟悉，那可以直接阅读[说明文档](#4-说明文档)。 

# 1. 安装
请先确保自己已经安装了pip。如果你不确定是否安装了pip，请打开cmd命令窗口并输入`pip`，如果像下面这样，说明你已安装pip。  
```
C:\Users\bertr>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                              WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                              (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any
                              HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```

如果你已安装pip，请跳到1.2.

## 1.1. 安装pip
安装方法可以参考这篇博客：[windows下 python安装pip 简易教程](https://blog.csdn.net/qq_37176126/article/details/72824404)。如果环境变量不知道怎么设置的话，可以重新[下载Python](https://www.python.org/downloads/)，并在安装时勾选添加Python到PATH变量。  


## 1.2. 更新pip
还是打开cmd命令窗口，输入`pip install --upgrade pip`  
```
C:\Users\bertr>pip install --upgrade pip
```

## 1.3. 安装dgut-requests
打开cmd命令窗口，输入`pip install dgut-requests`  
```
C:\Users\bertr\Desktop>pip install dgut-requests
Looking in indexes: https://pypi.org/simple/
Collecting dgut-requests
  Using cached dgut_requests-0.1.0-py3-none-any.whl (6.6 kB)
Collecting requests
  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)
Collecting lxml
  Using cached lxml-4.6.3-cp38-cp38-win_amd64.whl (3.5 MB)
Collecting idna<3,>=2.5
  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
Collecting chardet<5,>=3.0.2
  Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
Installing collected packages: urllib3, idna, chardet, certifi, requests, lxml, dgut-requests
Successfully installed certifi-2020.12.5 chardet-4.0.0 dgut-requests-0.1.0 idna-2.10 lxml-4.6.3 requests-2.25.1 urllib3-1.26.4
```
最后面是Successfully installed...说明安装成功。  
如果安装得很慢，甚至报错的话，很可能是网速问题，这时候可以使用镜像源进行下载。我个人比较推荐的镜像源是清华镜像源，我们可以将上面的cmd命令改成这样：  
```
pip install -i "https://pypi.tuna.tsinghua.edu.cn/simple/" dgut-requests
```

## 1.4. 确认成功安装
在Python交互界面环境下，输入`import dgut_requests`没有报错即成功安装了dgut-requests库。  
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import dgut_requests
>>>
```

# 2. 基本用法
## 2.1. 导入
```
>>> from dgut_requests import dgut
>>> dgut
<class 'dgut_requests.dgut'>
>>> dgut.dgutUser
<class 'dgut_requests.dgut.dgutUser'>
>>> dgut.dgutXgxt
<class 'dgut_requests.dgut.dgutXgxt'>
>>> dgut.dgutIllness
<class 'dgut_requests.dgut.dgutIllness'>
>>>
```
但是更建议这样
```
>>> from dgut_requests.dgut import dgutUser, dgutXgxt, dgutIllness
>>> dgutUser
<class 'dgut_requests.dgut.dgutUser'>
>>> dgutXgxt
<class 'dgut_requests.dgut.dgutXgxt'>
>>> dgutIllness
<class 'dgut_requests.dgut.dgutIllness'>
>>>
```
如果想要更加方便的话，可以这样
```
>>> from dgut_requests.dgut *
>>> dgutUser
<class 'dgut_requests.dgut.dgutUser'>
>>> dgutXgxt
<class 'dgut_requests.dgut.dgutXgxt'>
>>> dgutIllness
<class 'dgut_requests.dgut.dgutIllness'>
>>>
```

## 2.2. 构建账号，实现登录
```python
from dgut_requests.dgut import dgutUser


u = dgutUser("201841416100", "123456") # dgutUser(username, password)
print(u)

response = u.signin("https://cas.dgut.edu.cn/home/Oauth/getToken/appid/xgxtt.html") # 登录学工系统, signin(login_url: str)
print(response)
print(response.text)
print("-"*30)

response = u.session.get("http://stu.dgut.edu.cn/student/basicinfo/basicInfo.jsp")
print(response)
print(response.text)
```

输出结果

```
<dgut_requests.dgut.dgutUser object at 0x0000012546350850>
<Response [200]>



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
<html>
<head>
<title>学生信息管理系统</title>
<meta http-equiv="refresh" content="0;URL=homepage.jsp">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body>
正在进入首页
</body>
</html>
------------------------------
<Response [200]>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">






<html>





<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>学生基本信息</title>
<link href="/css/main.css" rel="stylesheet" type="text/css">
<script type="text/javascript">
function submitTo(formId, url) {
        var form = document.getElementById("" + formId);
        form.action = url;
        form.submit();
}
function SubmitToBlank(formId, url) {
        var form = document.getElementById("" + formId);
        form.action = url;
        form.target = "_blank";
        form.submit();
        form.action = '';
        form.target = "_self";
}
</script>
</head>
<body>
……
```

通过上面的例子我们可以学习到，使用`dgutUser(username, password)`构建DGUT账号，然后使用`signin(login_url: str)`方法进行登录即可实现模拟登录。


## 2.3. 获取考勤职位信息 & 学工系统考勤
```python
from dgut_requests.dgut import dgutXgxt


u = dgutXgxt("201841416100", "123456") # dgutUser(username, password)

# get_workAssignment()方法获取考勤职位信息，返回一个包含二元组的列表，每一个二元组包含考勤职位ID和考勤职位名。当你没有任何职位时，返回空列表[]
print(u.get_workAssignment())
print("-"*30)

# attendance(flag: int, workAssignmentId: int = None)
# flag=1表示签到，flag=2表示签退
# workAssignmentId为None或者缺省时，表示调用get_workAssignment()方法并获取第一个职位信息的ID作为该参数
# 当你有多个职位时，你就需要指定workAssignmentId，否则可能进行签到的职位与你想的不同
# 当你没有任何职位且没有指定workAssignmentId时，会抛出异常ValueError("没有可考勤的职位")
print(u.attendance(1))
print(u.attendance(2))
print("-"*30)

print(u.attendance(1, 9001))
print(u.attendance(2, 9001))
```

输出结果
```
[('9000', 'XXX学生助理'), ('9001', 'xxx办公室助理')]
------------------------------
{'message': '签到成功', 'code': 1, 'info': {'data': {'action_name': 'beginWork', 'modifying': 'true', 'salaryInfoId': '', 'session_token': 'token_key_1619157009355', 'backUrl': '', 'workAssignmentId': '9000'}, 'time': datetime.datetime(2021, 4, 23, 13, 50, 9, 542232)}}
{'message': '签退成功', 'code': 1, 'info': {'data': {'action_name': 'endWork', 'modifying': 'true', 'salaryInfoId': '', 'session_token': 'token_key_1619157045726', 'backUrl': '', 'workAssignmentId': '9000'}, 'time': datetime.datetime(2021, 4, 23, 13, 50, 45, 960229)}}
------------------------------
{'message': '签到成功', 'code': 1, 'info': {'data': {'action_name': 'beginWork', 'modifying': 'true', 'salaryInfoId': '', 'session_token': 'token_key_1619157089460', 'backUrl': '', 'workAssignmentId': '9001'}, 'time': datetime.datetime(2021, 4, 23, 13, 51, 29, 618113)}}
{'message': '签退成功', 'code': 1, 'info': {'data': {'action_name': 'endWork', 'modifying': 'true', 'salaryInfoId': '', 'session_token': 'token_key_1619157094360', 'backUrl': '', 'workAssignmentId': '9001'}, 'time': datetime.datetime(2021, 4, 23, 13, 51, 34, 492294)}}
```

细心的读者可能已经发现了，上面的代码中，构建账号后并没有调用`signin(login_url: str)`方法，而是直接调用两个功能方法。  
这是因为dgutXgxt类中使用python的装饰函数实现AOP面向切面编程，在调用`get_workAssignment()`和`attendance(flag: int, workAssignmentId: int = None)`方法时会自动先调用`signin(login_url: str)`方法。同时，这种编程思维也使得代码变得更加简洁且便于维护。


## 2.4. 实现每日疫情打卡
```python
from dgut_requests.dgut import dgutIllness

u = dgutIllness("201841416100", "123456")
print(u.report())
print(u.report())
```

输出结果
```
{'message': '您今天已打卡成功！已连续打卡688天！'}
{'message': '您今天已打卡成功！已连续打卡688天！'}
```

与前面一样，先构造一个`dgutIllness`对象，然后调用`report()`方法即可完成打卡。该功能仅用于爬虫学习及防止忘记打卡，疫情期间切勿轻视打卡。

## 2.5. 获取个人成绩
```python
from dgut_requests.dgut import dgutJwxt

u = dgutJwxt("201841416100", "123456")
# 现在是2021年4月，即2020-2021学年第二学期
print(f"获取本学期的原始成绩")
for i, item in enumerate(u.get_score(), 1):
    print(i, *item)
print("-"*30)

print("获取2020-2021学年第一学期的原始成绩")
# xn=2020代表2020-2021学年
# xq=1代表第一学期，xq=2代表第二学期
for i, item in enumerate(u.get_score(xn=2020, xq=1), 1):
    print(i, *item)
print("-"*30)

print("获取2020-2021学年第一学期的有效成绩")
for i, item in enumerate(u.get_score(score_type=2, xn=2020, xq=1), 1):
    print(i, *item)
print("-"*30)

print("获取2020-2021学年第一学期的主修课程的有效成绩")
for i, item in enumerate(u.get_score(score_type=2, course_type=1, xn=2020, xq=1), 1):
    print(i, *item)
print("-"*30)

print("获取2019-2020学年的原始成绩")
# time_range=2代表按学年查询（1：入学以来 | 2：按学年 | 3：按学期）
# xn=2019代表2019-2020学年
for i, item in enumerate(u.get_score(time_range=2, xn=2019), 1):
    print(i, *item)
print("-"*30)

print("获取入学以来的有效成绩")
for i, item in enumerate(u.get_score(time_range=1, score_type=2), 1):
    print(i, *item)
print("-"*30)

# get_score(score_type: int = 1, course_type: int = 3, time_range: int = 3, **kwargs)
# score_type: 成绩类型: 1=>原始成绩（默认） | 2=>有效成绩
# course_type: 课程类型: 1=>主修 | 2=>辅修 | 3=>主修和辅修（默认）
# time_range: 时间范围选择: 1=>入学以来 | 2=>学年 | 3=>学期（默认）
# **kwargs: 补充参数，有xn和xq两个参数，都是int类型
    # xn: 学年: [1970, 9999]
    # xq: 学期: 1 | 2
```

输出结果
```
获取本学期的原始成绩
共有0个结果
------------------------------
获取2020-2021学年第一学期的原始成绩
1 [0710007]形势与政策5 0.0 公共课/必修课 初修 考试 初修取得 xx
2 [1310006]体育5 0.5 公共课/必修课 初修 考试 初修取得 xx
3 [0410084]PHP程序设计 3.0 专业课/任选课 初修 考查 初修取得 xx
4 [0410090]网络攻防技术 3.0 专业课/必修课 初修 考查 初修取得 xx
5 [0410091]操作系统安全 3.0 专业课/限选课 初修 考查 初修取得 xx
6 [0410226]身份认证与访问控制 2.0 专业课/必修课 初修 考查 初修取得 xx
7 [0410241]NISP认证体系 2.0 专业课/必修课 初修 考查 初修取得 xx
------------------------------
获取2020-2021学年第一学期的有效成绩
1 [0710007]形势与政策5 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
2 [1310006]体育5 0.5 公共课/必修课 初修 考试 xx 0.5 xx xx
3 [0410084]PHP程序设计 3.0 专业课/任选课 初修 考查 xx 3.0 xx xx
4 [0410090]网络攻防技术 3.0 专业课/必修课 初修 考查 xx 3.0 xx xx
5 [0410091]操作系统安全 3.0 专业课/限选课 初修 考查 xx 3.0 xx xx
6 [0410226]身份认证与访问控制 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
7 [0410241]NISP认证体系 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
------------------------------
获取2020-2021学年第一学期的主修课程的有效成绩
1 [0710007]形势与政策5 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
2 [1310006]体育5 0.5 公共课/必修课 初修 考试 xx 0.5 xx xx
3 [0410084]PHP程序设计 3.0 专业课/任选课 初修 考查 xx 3.0 xx xx
4 [0410090]网络攻防技术 3.0 专业课/必修课 初修 考查 xx 3.0 xx xx
5 [0410091]操作系统安全 3.0 专业课/限选课 初修 考查 xx 3.0 xx xx
6 [0410226]身份认证与访问控制 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
7 [0410241]NISP认证体系 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
------------------------------
获取2019-2020学年的原始成绩
1 [14510300]计算机组成原理 4.0 专业基础课/必修课 初修 考试 初修取得 xx
2 [14540011]JAVA语言程序设计 3.0 专业基础课/必修课 初修 考试 初修取得 xx
3 [048774]离散数学 4.0 专业基础课/必修课 初修 考试 初修取得 xx
4 [24010004](公选)书法 1.5 公共课/任选课 初修 考查 初修取得 xx
5 [253375](网络公选)书法鉴赏 1.5 公共课/任选课 初修 考试 初修取得 xx
6 [0710002]马克思主义基本原理 3.0 公共课/必修课 初修 考试 初修取得 xx
7 [0710005]形势与政策3 0.0 公共课/必修课 初修 考试 初修取得 xx
8 [1010005]应用英语A 2.0 公共课/必修课 初修 考试 初修取得 xx
9 [1310004]体育3 0.5 公共课/必修课 初修 考查 初修取得 xx
10 [0410032]概率论与数理统计 3.5 专业基础课/必修课 初修 考试 初修取得 xx
11 [379925]算法与数据结构 5.0 专业基础课/必修课 初修 考试 初修取得 xx
12 [2510038](网络公选)影响力从语言开始 1.0 公共课/任选课 初修 考试 初修取得 xx
1 [19510041]毛泽东思想和中国特色社会主义理论体系概论 4.0 公共课/必修课 初修 考试 初修取得 xx
2 [078643]“思政课”社会实践2 1.0 公共课/必修课 初修 初修取得 xx
3 [0710006]形势与政策4 0.0 公共课/必修课 初修 考试 初修取得 xx
4 [1310005]体育4 0.5 公共课/必修课 初修 考查 初修取得 xx
5 [0410074]网络空间安全法律法规 2.0 专业课/必修课 初修 考查 初修取得 xx
6 [0410076]现代密码学 3.0 专业课/必修课 初修 考试 初修取得 xx
7 [2510014](网络公选)《三国志》导读 1.5 公共课/任选课 初修 考试 初修取得 xx
8 [201901052](网络公选)基因与人 1.0 公共课/任选课 初修 考试 初修取得 xx
9 [4100082]算法与数据结构实践专题 1.0 专业基础课/必修课 初修 考查 初修取得 xx
10 [4100084]操作系统 4.0 专业基础课/必修课 初修 考试 初修取得 xx
11 [4100085]数据库系统原理 4.0 专业基础课/必修课 初修 考试 初修取得 xx
12 [4100086]计算机网络 4.0 专业基础课/必修课 初修 考试 初修取得 xx
------------------------------
获取入学以来的有效成绩
1 [19510070]中国近现代史纲要 2.0 公共课/必修课 初修 考试 xx 2.0 xx xx
2 [0710003]形势与政策1 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
3 [1010001]大学英语1 3.0 公共课/必修课 初修 考试 xx 3.0 xx xx
4 [1010003]英语口语1 1.0 公共课/必修课 初修 考试 xx 1.0 xx xx
5 [0810001]管理学概论 2.0 公共课/必修课 初修 考查 xx 2.0 xx xx
6 [1310001]大学生心理健康教育 1.0 公共课/必修课 初修 考查 xx 1.0 xx xx
7 [1310002]体育1 1.0 公共课/必修课 初修 考查 xx 1.0 xx xx
8 [1710001]军事训练与教育 3.0 军训 初修 xx 3.0 xx xx
9 [0410029]高等数学C(I) 5.0 专业基础课/必修课 初修 考试 xx 5.0 xx xx
10 [0410069]网络空间安全专业导论与职业生涯规划 1.0 专业基础课/必修课 初修 考查 xx 1.0 xx xx
11 [0410073]程序设计基础 5.0 专业基础课/必修课 初修 考试 xx 5.0 xx xx
1 [0710001]思想道德修养与法律基础 3.0 公共课/必修课 初修 考试 xx 3.0 xx xx
2 [0710004]形势与政策2 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
3 [078645]“思政课”社会实践1 1.0 社会实践 初修 xx 1.0 xx xx
4 [1010002]大学英语2 3.0 公共课/必修课 初修 考试 xx 3.0 xx xx
5 [1010004]英语口语2 1.0 公共课/必修课 初修 考试 xx 1.0 xx xx
6 [0810003]创业基础 2.0 公共课/必修课 初修 考查 xx 2.0 xx xx
7 [1310003]体育2 1.0 公共课/必修课 初修 考查 xx 1.0 xx xx
8 [0410030]高等数学C(II) 6.0 专业基础课/必修课 初修 考试 xx 6.0 xx xx
9 [0410031]线性代数 2.5 专业基础课/必修课 初修 考试 xx 2.5 xx xx
10 [0310005]大学物理C 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
11 [379924]面向对象程序设计（C++） 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
12 [379926]程序设计基础实践 1.0 专业基础课/必修课 初修 考查 xx 1.0 xx xx
13 [0110298](公选)计算机建模分析及其在材料科学中的应用 1.5 公共课/任选课 初修 考查 xx 1.5 xx xx
1 [14510300]计算机组成原理 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
2 [14540011]JAVA语言程序设计 3.0 专业基础课/必修课 初修 考试 xx 3.0 xx xx
3 [048774]离散数学 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
4 [24010004](公选)书法 1.5 公共课/任选课 初修 考查 xx 1.5 xx xx
5 [253375](网络公选)书法鉴赏 1.5 公共课/任选课 初修 考试 xx 1.5 xx xx
6 [0710002]马克思主义基本原理 3.0 公共课/必修课 初修 考试 xx 3.0 xx xx
7 [0710005]形势与政策3 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
8 [1010005]应用英语A 2.0 公共课/必修课 初修 考试 xx 2.0 xx xx
9 [1310004]体育3 0.5 公共课/必修课 初修 考查 xx 0.5 xx xx
10 [0410032]概率论与数理统计 3.5 专业基础课/必修课 初修 考试 xx 3.5 xx xx
11 [379925]算法与数据结构 5.0 专业基础课/必修课 初修 考试 xx 5.0 xx xx
12 [2510038](网络公选)影响力从语言开始 1.0 公共课/任选课 初修 考试 xx 1.0 xx xx
1 [19510041]毛泽东思想和中国特色社会主义理论体系概论 4.0 公共课/必修课 初修 考试 xx 4.0 xx xx
2 [078643]“思政课”社会实践2 1.0 公共课/必修课 初修 xx 1.0 xx xx
3 [0710006]形势与政策4 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
4 [1310005]体育4 0.5 公共课/必修课 初修 考查 xx 0.5 xx xx
5 [0410074]网络空间安全法律法规 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
6 [0410076]现代密码学 3.0 专业课/必修课 初修 考试 xx 3.0 xx xx
7 [2510014](网络公选)《三国志》导读 1.5 公共课/任选课 初修 考试 xx 1.5 xx xx
8 [201901052](网络公选)基因与人 1.0 公共课/任选课 初修 考试 xx 1.0 xx xx
9 [4100082]算法与数据结构实践专题 1.0 专业基础课/必修课 初修 考查 xx 1.0 xx xx
10 [4100084]操作系统 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
11 [4100085]数据库系统原理 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
12 [4100086]计算机网络 4.0 专业基础课/必修课 初修 考试 xx 4.0 xx xx
1 [0710007]形势与政策5 0.0 公共课/必修课 初修 考试 xx 0.0 xx xx
2 [1310006]体育5 0.5 公共课/必修课 初修 考试 xx 0.5 xx xx
3 [0410084]PHP程序设计 3.0 专业课/任选课 初修 考查 xx 3.0 xx xx
4 [0410090]网络攻防技术 3.0 专业课/必修课 初修 考查 xx 3.0 xx xx
5 [0410091]操作系统安全 3.0 专业课/限选课 初修 考查 xx 3.0 xx xx
6 [0410226]身份认证与访问控制 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
7 [0410241]NISP认证体系 2.0 专业课/必修课 初修 考查 xx 2.0 xx xx
------------------------------
```
首先创建一个`dgutJwxt`对象，然后调用`get_score`方法返回一个成绩结果的生成器，该生成器的每个元素对应着一条记录。  
有兴趣的朋友可以研究一下openpyxl库，制作一个生成学年综测excel表格的脚本。

# 3. 高级用法

## 3.1. session会话管理
`dgutUser`类及其子类(`dgutXgxt`、`dgutIllness`)的构造函数中定义了一个`requests.Session()`对象session进行会话管理，它会自动保存cookies信息，并且每次发起http请求都会使用该对象的headers和cookies属性作为http包的头部。因此，我们使用其来发起请求，可以更加轻松方便。

```python
from dgut_requests.dgut import dgutUser


u = dgutUser("201841416100", "123456") # dgutUser(username, password)
u.signin("https://cas.dgut.edu.cn/home/Oauth/getToken/appid/xgxtt.html")

# 使用session进行会话管理
print("对象u的cookies有：")
for key, value in u.session.cookies.items():
    print(f"{key}={value}")
print("-"*30)

# 我们再登录一下教务服务平台试试，并查看登录之后cookies有什么变化
print("对象u当前的cookies有：")
u.session.get("https://cas.dgut.edu.cn/home/Oauth/getToken/appid/jwyd.html")
for key, value in u.session.cookies.items():
    print(f"{key}={value}")
```

输出结果

```
对象u的cookies有：
PHPSESSID=osn41bs02hp4ie5m6dkem7u5p1
last_oauth_appid=xgxtt
JSESSIONID=27E4DED5E514BEABFDF32BC9A7F16984.sms9021
------------------------------
对象u当前的cookies有：
PHPSESSID=osn41bs02hp4ie5m6dkem7u5p1
last_oauth_appid=jwyd
JSESSIONID=F3993F30B0E5DE820496D67C3A917171
JSESSIONID=27E4DED5E514BEABFDF32BC9A7F16984.sms9021
```

## 3.2. 使用cookies进行管理
当账号很多并且操作很多的时候，如果每一次都需要进行登录，那么效率就会很低。此外，如果短时间内需要重复登录的话，可能需要重复输入账号密码。  
有一个比较好的方案就是可以使用cookies。cookies一般会有一定时长的有效期，在有效期内我们可以把账号密码置空，直接将cookies信息添加到空账号中。这样，当我们模拟访问网页的时候也可以畅行无阻。

```python
from dgut_requests.dgut import *
import re
import os
import json
import requests

path = 'cookies.json'

def cookies_is_expires(path: str, url: str, pattern: re.compile):
    '''
    判断cookies是否过期（过期或不存在该文件都视为过期）
    '''
    if not os.path.exists(path):
        return True
    with open(path, 'r') as f:
        cookie = json.loads(f.read())
    x = requests.Session()
    requests.utils.add_dict_to_cookiejar(x.cookies, cookie)
    response = x.get(url)
    if pattern.search(response.text, re.S):
        return True
    return False


if not os.path.exists(path) or cookies_is_expires(path, "http://stu.dgut.edu.cn/homepage.jsp", re.compile(r'token = ".*?"')):
    u = dgut.dgutXgxt("201841416100", "123456")
    print(u.get_workAssignment())
    cookie = requests.utils.dict_from_cookiejar(u.session.cookies)
    print(cookie)
    with open(path, 'w') as f:
        f.write(json.dumps(cookie))
else:
    print("has cookies")
    with open(path, 'r') as f:
        cookies = json.loads(f.read())
    u = dgut.dgutXgxt('', '')
    requests.utils.add_dict_to_cookiejar(u.session.cookies, cookie)
    print(u.session.cookies)
    print(u.get_workAssignment())
```

第一次输出结果
```
[('9000', 'xxx学生助理')]
{'JSESSIONID': '92B8A8D7ECC0BC02CD01E16050AB46D8.sms9015', 'PHPSESSID': 'o9tglciva8vujgi3l91iqm1ff2', 'last_oauth_appid': 'xgxtt'}
```

第二次输出结果
```
has cookies
<RequestsCookieJar[<Cookie JSESSIONID=92B8A8D7ECC0BC02CD01E16050AB46D8.sms9015 for />, <Cookie PHPSESSID=o9tglciva8vujgi3l91iqm1ff2 for />, <Cookie last_oauth_appid=xgxtt for />]>
[('9000', 'xxx学生助理')]
```

## 3.3. 基于`dgutUser`开发新系统，基于现有系统开发新功能
开发者可基于`dgutUser`及其子类进行新功能的开发，继承`dugtUser`及其子类，然后用装饰函数`decorator_signin`装饰新功能函数。这样，开发者只需要关心功能的实现而不需要关心登录功能。

# 4. 说明文档
## 4.1. `class AuthError`
认证错误类，在认证失败时会抛出该异常。
```python
from dgut_requests.dgut import *

try:
    u = dgutUser('123', '456')
    u.signin(xgxt_login)
except AuthError as e:
    print(e)
```

## 4.2. `class dgutUser`
### 4.2.1. 属性(`attribute`)
|       name |           type            | means            |
| ---------: | :-----------------------: | :--------------- |
|   username |            str            | DGUT中央认证账号 |
| __password |            str            | DGUT中央认证密码 |
|    session | requests.sessions.Session | 会话             |

### 4.2.2. 方法(`method`)
|                                           name | params                                                     |                      return | means                  |
| ---------------------------------------------: | :--------------------------------------------------------- | --------------------------: | :--------------------- |
| `__init__(self, username: str, password: str)` | username: DGUT中央认证账号<br>__password: DGUT中央认证密码 |                  not return | 构造函数               |
|                 `signin(self, login_url: str)` | login_url: 登录url，以http://或https://开头                | response: requests.Response | 登录函数，返回结果响应 |


## 4.3. `class dgutXgxt`
### 4.3.1. 属性(`attribute`)
同[4.2.1](#421-属性attribute)

### 4.3.2. 方法(`method`)
|                                                        name | params                                                                                                                                                                         | return | means                          |
| ----------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -----: | :----------------------------- |
|                                  `get_workAssignment(self)` |                                                                                                                                                                                |   list | 获取考勤职位信息，返回一个列表 |
| `attendance(self, flag: int, workAssignmentId: int = None)` | flag: 1表示签到，2表示签退<br>workAssignmentId: 考勤职位ID，缺省或None时自动调用`get_workAssignment(self)`获取第一个职位信息作为参数，若没有任何职位信息则抛出`ValueError`异常 |   dict | 考勤函数，返回一个字典结果     |

其他方法同[4.2.2](#422-方法method)

## 4.4. `class dgutIllness`
### 4.4.1. 属性(`attribute`)
同[4.2.1](#421-属性attribute)

### 4.4.2. 方法(`method`)
|                                                                     name | params                            | return | means                          |
| -----------------------------------------------------------------------: | :-------------------------------- | -----: | :----------------------------- |
| `report(self)` | - |   dict | 进行疫情防控每日打卡，返回结果 |

其他方法同[4.2.2](#422-方法method)

## 4.5. `class dgutJwxt`
### 4.5.1. 属性(`attribute`)
同[4.2.1](#421-属性attribute)

### 4.5.2. 方法(`method`)
|                                                                                        name | params                                                                                                                                                                                                                                                                                                 |    return | means                        |
| ------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------: | :--------------------------- |
| `get_score(self, score_type: int = 1, course_type: int = 3, time_range: int = 3, **kwargs)` | sscore_type: 成绩类型: 1=>原始成绩（默认） / 2=>有效成绩<br>course_type: 课程类型: 1=>主修 / 2=>辅修 / 3=>主修和辅修（默认）<br>time_range: 时间范围选择: 1=>入学以来 / 2=>学年 / 3=>学期（默认）<br>**kwargs: 补充参数，有xn和xq两个参数，都是int类型。xn: 学年，取值[1970, 9999]; xq: 学期，取值1或2 | generator | 查询成绩，返回一个生成器对象 |

其他方法同[4.2.2](#422-方法method)

## 4.6. 其他属性/变量
|                           name | type  | means                 |
| -----------------------------: | :---: | :-------------------- |
|        xgxt_login/学工系统登录 |  str  | 学工系统的登录url     |
| illness_login/疫情防控系统登录 |  str  | 疫情防控系统的登录url |
|        jwxt_login/教务系统登录 |  str  | 教务系统的登录url     |


## 4.7. 其他方法
|                    name | params       |   return | means                                                                                                                         |
| ----------------------: | :----------- | -------: | :---------------------------------------------------------------------------------------------------------------------------- |
| `decorator_signin(url)` | url: 登录url | function | `signin`方法的装饰函数，在功能函数前面输入`@decorator_signin(url)`，就可以实现调用功能函数前会先验证登录，是AOP编程的具体实现 |

# 5. 相比0.0.x版本的改动

## 5.1. 代码重构，简洁易维护
- 对0.0.x版本的代码进行了重构，代码量缩减50%
- 将`dgutLogin.py`和`dgutXgxtt.py`合并为`dgut.py`
- classdgutLogin重命名为class dgutUser，classdgutXgxtt重命名为class dgutXgxt
- 使用装饰函数实现AOP编程，分离出登录功能，便于维护代码和开发新功能

## 5.2. 只抛出异常，不处理异常
- 将异常的处理权交给开发者，一方面减少开发者学习错误码的时间成本，另一方面也符合轻量级的定位

## 5.3. 增加疫情防控系统类`class dgutIllness`和教务系统类`class dgutJwxt`
- 增加`class dgutIllness`，实现疫情防控打卡功能
- 增加`class dgutJwxt`，实现成绩信息的获取
- 仅用于爬虫学习和防止忘记打卡，切勿依赖自动执行而轻视打卡

## 5.4. 形成轻量级的功能开发框架
- 对于使用者来说，简单易懂
- 对于开发者来说，可以减少大量开发时间，代码复用性强，仅实现功能业务逻辑即可。若基于dgutUser进行开发，不需要管理登录模块。若基于其他类进行开发，则不仅不需要管理登录模块，同时还可以调用已有的功能函数进行开发，随用随取，简单明了。



# 6. 目前已有的项目示例
- 勤工俭学自动考勤助手  
  - [github仓库](https://github.com/bertramoon/Auto_Attendance)  
  - [gitee仓库](https://gitee.com/bertramoon/Auto_Attendance)  

- 疫情防控自动打卡  
  - [github仓库](https://github.com/bertramoon/Auto_Report)  
  - [gitee仓库](https://gitee.com/bertramoon/dgut-autoreport-configure)  
  
- 出入校快速申请
  - 目前基于QT5和dgut-requests开发了PC端的GUI程序，具有记住账号密码和表单的功能，可用于快速申请，[gitee仓库地址](https://gitee.com/bertramoon/dgut-leave-application)  

- 有需求或技术方面的问题请联系作者Email：bertramoon@126.com


# 7. 更新日志

## v1.2 - 2022-1-4

- `dgutIllness`的`report`方法有点小问题，在提交数据前不小心删除了最后一次核酸检测时间选项，本次是修复该小bug

## v1.1 - 2021-12-22

- `dgutIllness`的`report`方法代码微修改

## v1.0 - 2021-12-21

- 疫情防控打卡系统更新。注意，因接口改变，`dgutIllness`的`report`方法有所变化，不再接收任何参数
- 随着版本更新，将版本号正式定为1.0，此后每次小的迭代增加0.1，大的更新向上取整

## v0.1.5 - 2021-12-18

- 疫情防控打卡时会检测是否已打卡，已打卡则返回打卡成功的信息`{'code': 400, 'message': message, 'info': []}`，减少无故提交次数，避免被检测

## v0.1.4 - 2021-9-5

- 将返回成绩结果改为生成器
- 修正了部分注释
- 稍微修改了一下代码中不够简洁的部分

## v0.1.3 - 2021-7-1
修复了显示`{'code': 400, 'message': '选定的 核酸检测结果 是无效的', 'info': []}`的问题

## v0.1.2 - 2021-5-19
修改了上次更新时代码错误产生的无法正常打卡的问题，并更新了README.md。

## v0.1.1 - 2021-5-16
主要解决了调用dgutIllness中report()方法出现提交异常的情况。此外，对READEME.md文档也进行了部分更新。

## v0.1.0 - 2021-4-24
重大更新，重构代码。具体请查看`5. 相比0.0.x版本的改动`