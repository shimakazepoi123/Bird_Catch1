import time, os
from base64 import decodebytes

try:
    from selenium import webdriver
except ImportError:
    raise ImportError
else:
    pass

SNAPSHOT_JS = """
    var ele = document.querySelector('div[_echarts_instance_]');
    var mychart = echarts.getInstanceByDom(ele);
    return mychart.getDataURL({
        type: '%s',
        pixelRatio: %s,
        excludeComponents: ['toolbox']
    });
"""


# convert canvas bytes to file
def turn_to_image(file_name, save_name):
    return save_image(data=base64_decode(_chrome_driver(file_name)), filename=save_name)


def save_image(data: bytes, filename: str):
    with open(filename, 'wb') as file:
        file.write(data)


def base64_decode(content: str) -> bytes:
    missing_padding = len(content) % 4
    if missing_padding != 0:
        content += "=" * (4 - missing_padding)
    return decodebytes(content.encode('utf-8'))


def _chrome_driver(file_name, browser='Chrome'):
    if browser == 'Chrome':
        chrome = chrome_driver()
        chrome.get('file://' + os.path.abspath(file_name))
        time.sleep(2)

        return chrome.execute_script(SNAPSHOT_JS % ('png', 2))

    elif browser == 'FireFox':
        firefox = firefox_driver()
        firefox.get('file://' + os.path.abspath(file_name))
        time.sleep(2)

        return firefox.execute_script(SNAPSHOT_JS % ('png', 2))


def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    return webdriver.Chrome(options=options)


def firefox_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('headless')

    return webdriver.Firefox(options=options)
