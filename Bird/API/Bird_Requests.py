import requests
from API.Bird_check import check_if_none


# catch bird's record
class Bird_Requests(object):

    def __init__(self):
        self.limit = 0  # 返回记录数目
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.150 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.birdreport.cn',
            'Referer': 'http://www.birdreport.cn/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def requests_bird(self, url):
        """

        :param headers:
        :param url: 放置请求的url网址
        :return: json对象
        """
        # 检查数据
        try:
            data = check_if_none()
        except Exception as e:
            raise e
        else:
            try:
                requests_bird1 = requests.post(url=url, data=data, headers=self.headers)
            except Exception as e:
                raise e
            else:
                data['limit'] = requests_bird1.json()['count'] # 返回记录数目
                return requests_bird1.json()
