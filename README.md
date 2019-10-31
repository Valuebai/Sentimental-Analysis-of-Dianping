# Sentimental-Analysis-of-Dianping
Sentimental-Analysis-of-Dianping-Comment，大众点评的情感细粒度分类，数据集合是大众点评公开给创新工厂的2018 AI全球挑战赛的数据集

![Languages](https://img.shields.io/badge/Languages-Python3.6-green)
![Build](https://img.shields.io/badge/Build-passing-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Contributions](https://img.shields.io/badge/Contributions-welcome-ff69b4.svg)

<p align="center">
  <!--快速在当前页面跳转的-->
  <a href="# Quick-start">Quick-start</a> 
  
  <a href="# Projects">Projects</a> ：•


  <a href="#deploy">Deploy</a> ：•
  <a href="## Requirements">Requirements</a>•
  <a href="## Ptyhon创建虚拟环境">Ptyhon创建虚拟环境</a> •
  
  <a href="# Linux相关">Linux相关：</a>•
  <a href="## linux部署指南">linux部署指南</a>•
  <a href="## linux上杀死gunicorn的进程">linux上杀死gunicorn的进程</a>•
  <a href="## linux根据端口号查找项目路径方法">linux根据端口号查找项目路径方法</a>•
  
</p>


# Quick-start


# Projects

Sentimental-Analysis-of-Dianping


# Deploy

## Requirements
- 生成指南：
- 第一步：安装包 pip install pipreqs
- 第二步：在对应路径cmd，输入命令生成 requirements.txt文件：pipreqs ./ --encoding=utf8 --force 避免中文路径报错
- 第三步：下载该代码后直接pip install -r requirements.txt
- 或者创建虚拟环境安装

## Ptyhon创建虚拟环境

### 方法一：自带命令
1. 进入文件夹目录
2. python -m venv -h 可查看帮助信息
3. 下面的
```
Linux运行命令行
$ 创建默认环境：python3 -m venv my_venv 
$ 创建指定环境：python3.6 -m venv  my_venv,  python2 -m venv  my_venv(添加到系统环境变量中)
$ 激活环境：. my_venv/bin/activate  (. 或者 source )
$ 退出环境：deactivate 

Windows系统运行cmd，使用 "py" Python 启动器命令配合 "-m" 开关选项:
$ 创建环境：py -3 -m venv my_venv (或者python -m venv my_venv)
$ 创建指定环境：py -3.6 -m venv my_venv,  py -3.7 -m venv my_venv (添加到系统环境变量中)
$ 激活环境：my_venv\Scripts\activate.bat
$ 退出环境：deactivate

执行后，会在目录前方出现<my_venv>表明已进入虚拟环境

安装项目:
$ pip install -r requirements.txt
```

### 方法二：Windows在PyCharm下创建虚拟环境
1. 安装并激活PyCharm
这个请自行安装
官方地址：https://www.jetbrains.com/pycharm/

2. 在PyCharm下创建虚拟环境
第一步：点击New Project
第二步：选择下图的New environment
第三步：点击create即可
pycharm会为新创建的项目自动建立一个虚拟环境


### 方法三：conda创建虚拟环境

[anaconda中的常用操作](https://blog.csdn.net/CampusAmour/article/details/83215524)


Linux下启动其终端命令行 
$ source ~/anaconda3/bin/activate root
$ anaconda-navigator

- 创建虚拟环境，conda create -n env_name python=3.6

- 同时安装必要的包，conda create -n env_name numpy matplotlib python=3.6

- 激活虚拟环境
  - Linux：source activate your_env_name(虚拟环境名称)
  - Windows：activate your_env_name(虚拟环境名称)

- 退出虚拟环境： 
  - Linux：source deactivate your_env_name(虚拟环境名称)
  - Windows：deactivate your_env_name(虚拟环境名称)

- 删除虚拟环境，conda remove -n your_env_name(虚拟环境名称) --all
- 删除包使用命令，conda remove --name $your_env_name  $package_name（包名)


conda常用命令
- 查看已安装的包，conda list
- 安装包，conda install package_name(包名)
- 查看当前存在的虚拟环境，conda env list 或 conda info -e
- 检查更新当前conda，conda update conda


# Linux相关


## linux部署指南
### 1. linux sh & nohup后台运行python脚本
  - 1）创建脚本vim run.sh
  - 2）填写内容并保存：nohup python3 -u  run.py > nohup.log 2>&1 &
  - 3）运行：sh run.sh 或者 . run.sh
  - 参考：[Linux sh、source和.命令执行.sh文件的区别](https://www.zengdongwu.com/article3.html) +
            [linux后台执行命令：&和nohup](https://blog.csdn.net/liuyanfeier/article/details/62422742)
```md
      - nohup : 就是不挂起的意思( no hang up)，可以在你退出帐户之后继续运行相应的进程
        - 使用&命令后，作业被提交到后台运行，当前控制台没有被占用，但是一但把当前控制台关掉(退出帐户时)，作业就会停止运行。nohup命令可以在你退出帐户之后继续运行相应的进程。
      - python3 -u  run.py : 执行py文件
      - -u的意思就是 uninterrupt不中断的意思，如果你的代码里边有sleep等线程沉睡相关的操作，如果你不-u的话 在后台 它就停住了
      - > nohup.log : 重定向保存日志到当前路径下的nohup.log
      - 2>&1 : 将标准出错也输出到nohup.log文件中
      - & : 最后一个&， 是让该命令在后台执行。
```

### 2. 使用gunicorn 部署flask服务 （个人项目推荐使用这个）
  - 1）创建脚本vim gunicorn.sh
  - 2）填写内容并保存：
    - conda activate just_do_it （在linux上创建好自己的环境，可选）
    - nohup gunicorn -w 4 -b 0.0.0.0:8001 run:app & （不带日志）
    - nohup gunicorn -w 4 -b 0.0.0.0:8001 run:app > gunicorn.log 2>&1 & （带日志）
    
  - 3）运行：sh gunicorn.sh 或者 . gunicorn.sh
  
```md
需要提前pip install gunicorn
简单地，gunicorn可以通过gunicorn -w 4 -b 0.0.0.0:8001 run:app启动一个Flask应用。其中,

-w 4是指预定义的工作进程数为4，
-b 127.0.0.1:4000指绑定地址和端口
run是flask的启动python文件，app则是flask应用程序实例

其中run.py中文件的可能形式是：
# run.py
from flask import Flask
app = Flask(__name__)

参考文章：
gunicorn部署Flask服务 https://www.jianshu.com/p/fecf15ad0c9a
https://www.cnblogs.com/gaidy/p/9784919.html
```

### 3. 使用screen命令部署
  - 第一步：screen -S yourname，新建一个叫yourname的session
  - 第二步：python run.py，运行代码，关闭shell连接后还会一直在linux上跑
  - 针对用户量小的情况，快速部署（本次使用这个）
  - 关于screen，详情见：https://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html 
```
    杀死所有命令的：ps aux|grep 你的进程名|grep -v grep | awk '{print $2}'|xargs kill -9
    
    https://www.hutuseng.com/article/how-to-kill-all-detached-screen-session-in-linux
```

### 4. 使用flask + nginx + uwsgi (不建议，因Flask 与 uWsgi 结合有许多难以处理的 bug)
  - 针对用户访问量大的情况，具体参考下面的文章
    - https://blog.csdn.net/spark_csdn/article/details/80790929
    - https://www.cnblogs.com/Ray-liang/p/4173923.html
    - https://blog.csdn.net/daniel_ustc/article/details/9070357

### 5. 使用flask + nginx + gunicorn （大项目推荐使用这个）
  - 生产环境很多大公司采用这个方式的，故推荐这个
  - 因Flask 与 uWsgi 结合有许多难以处理的 bug，故推荐这个
  - [Flask + Gunicorn + Nginx 部署](https://www.cnblogs.com/Ray-liang/p/4837850.html)


## linux上杀死gunicorn的进程
**方法一**
1. netstat -nltp | grep 8188
能看到类似下面的：
tcp        0      0 0.0.0.0:8188            0.0.0.0:*               LISTEN      23422/gunicorn: mas

2. kill -9 23422（换成你的）


**方法二**
1. 获取Gunicorn进程树 
```
pstree -ap|grep gunicorn

得到的结果如下

Python
| | |-grep,14519 --color=auto gunicorn
| -gunicorn,28097 /usr/local/bin/gunicorn query_site.wsgi:application -c ... 
| |-gunicorn,14226 /usr/local/bin/gunicorn query_site.wsgi:application -c ... 
| | |-{gunicorn},14229 
| | |-{gunicorn},14230 
...

```

2. 重启Gunicorn任务

kill -HUP 14226

3. 退出Gunicorn任务

kill -9 28097


## linux根据端口号查找项目路径方法
### 1. 只知道端口号
#### 方法一

**1. 根据端口号查询进程 ，比说6379**

```
netstat -lnp|grep 6379
```

**2. 根据进程号，查询寻程序路径**
```
ll /proc/2757
```
这样就找到了程序路径

#### 方法二
**1. 首先根据端口号查找进程**
```
netstat -nltp
或者
netstat -nltp | grep python
或者
netstat -apn |grep 10010
```
**2. 然后根据进程号去查找项目路径**
```
ps -ef |grep 8567
```
**3. 如果你第二步没有找到项目路径的话，尝试用**
```
lsof -p 8567
```
### 2. 如果知道项目部署在tomcat里
如果你的项目在linux 中是部署到tomcat容器里，可以输入下边的命令找到，如下:
```
ps anx|grep tomcat
```
