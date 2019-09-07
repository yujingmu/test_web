# test_web
安装python环境。
博文：https://www.cnblogs.com/Simple-Small/p/9179061.html


web自动化：实现代码驱动浏览器进行点点点的操作。即 代码  与  浏览器之间进行交互。

但是，代码不能够直接与浏览器进行交互，需要中间桥梁来实现二者互通。这个中间桥梁就是浏览器的驱动程序。

于是变成了   代码 == 浏览器驱动程序 == 浏览器

目前主流的浏览器有：ie，firefox，chrome，safari等。

每一个浏览器，都有对应的驱动程序或者插件。建立浏览器与代码之间沟通的桥梁。

根据以上内容，chrome浏览器中的 web环境安装步骤分以下三步：

1、安新selenium

   cmd命令行安装。使用以下命令安装selenium:   pip install -U selenium

2、安装chrome浏览器

      常用软件安装，就不描述了。

3、下载chromedriver，并放在python的安装根目录下。

       注意：chromedriver要与chrome版本匹配才可以。

     chromedriver下载地址： http://npm.taobao.org/mirrors/chromedriver/

     在此地址中，有非常多的chromedriver版本。需要找到能够支持你当前安装的chrome版本的驱动。

有windows、linux、mac三个平台的驱动。除此之外，有notes.txt文件。打开这个文件，可以看到当前2.44版本的chromedriver支持哪些版本的chrome.

  比如当前的chrome浏览器版本为71，那么chromedriver v2.44是支持此版本的。

  若是windows平台，无论是32位还是64位，都下载 chromedriver_win32.zip.

  将其解压到 python 安装目录下面即可。

    至此环境安装完成。

    如果是ie，firefox，只需要将驱动程序换成ieserverdriver，或者 geckodriver即可。其它的步骤都完全 一样。

检测环境是否成功

   打开pycharm,新建一个python文件，在其中输入以下代码并运行：

1 from selenium import webdriver
2 
3 #打开谷歌浏览器
4 driver = webdriver.Chrome()
5 #访问百度首页
6 driver.get("http://www.baidu.com")
 
 若能够成功打开谷歌浏览器，并访问百度首页成功。那恭喜你，环境安装成功了！！
 

附上  浏览器驱动下载地址汇总：

Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads  .       
国内镜像地址：http://npm.taobao.org/mirrors/chromedriver/

Edge:  https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:  https://github.com/mozilla/geckodriver/releases

Safari:  https://webkit.org/blog/6900/webdriver-support-in-safari-10/

https://www.cnblogs.com/Simple-Small/p/10065674.html
