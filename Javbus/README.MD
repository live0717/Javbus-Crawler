###Python 爬取javus所有的番号作品

[javbus]https://www.javbus.com/ 或者 https://www.javbus.com/

#####爬取有码，无码以及无码分类下的所有作品，以及磁力链，存入mongodb

#####需要安装mongodb，所用到的库只有pymongo和scrapy

安装方式： pip install pymongo(scrpay)
pip install scrapy(scrapy在windows下安装可以自行百度，因为需要安装额外库的依赖)

使用方式：

在settings.py设置你自己的mongodb库，因为不可抗力原因所以在windows下需要富强上网，需要打开设置里的DOWNLOADER_MIDDLEWARES

![图片](https://i.loli.net/2018/12/16/5c163c0d6a0dd.jpg)


###2019-1-10更新爬取**短视频信息

爬取具体信息到mongodb以及爬取视频到本地，mongodb信息如下图：

![图片2](https://i.loli.net/2019/01/11/5c376ea7ac969.png)

需要更改的地方主要是：run文件和settings文件，根据爬取内容打开相应的pipelines，具体看settings文件中的pipelines













