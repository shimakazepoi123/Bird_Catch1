## 使用说明

<img src="https://img.shields.io/badge/Python-3.6%2F3.7%2F3.8-Red" >


## 项目用途

用于对鸟种及报告次数的统计和词云生成

## 安装

备注：本项目支持Python3.6+

将Bird文件夹Git到(或者下载到)你的电脑上

之后切换到Bird目录,运行如下代码进行安装即可:

```python
pip install -r requirements.txt
```

## 使用

运行如下命令:

```python
python main.py -r
```

但在使用前需在config.json文件中修改对应配置等

config.json文件内容如下:

```json
{
    "page": "1",  # 指定抓取页数,必需项
    "limit": "5000", # 指定抓取的报告数,必需项
    "taxonid": "", # 指定抓取的鸟种id,非必需
    "startTime": "2021-01-15", # 指定报告起始时间,必需项
    "endTime": "2021-01-20", # 指定报告截止时间,必需项
    "province": "广东省", # 报告的省份,必需项
    "city": "",
    "district": "",
    "pointname": "",
    "username": "",
    "serial_id": "",
    "ctime": "",
    "taxonname": ""
}
```

最后会根据提供的数据,自动生成鸟类词云.

## 最后

如果遇到什么问题,可以发送邮件到a761711385@hotmail.com或在issue中与本人交流

