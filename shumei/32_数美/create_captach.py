import requests
import os


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}


def get_file(url, file_name):
    print(f"search url now {url}")
    res = requests.get(url, headers=headers, timeout=10)
    if res.status_code == 404:
        print(f"{file_name} is not found")
        return
    with open(file_name, "wb") as f:
        f.write(res.content)


def jy3_full_alarm(base_path):
    """
    https://static.geetest.com/static/js/fullpage.9.0.9.js
    """
    for num in range(600, 950):
        a, b, c = list(str(num))
        file = f"{a}.{b}.{c}.js"
        get_file(f"https://static.geetest.com/static/js/fullpage.{file}", os.path.join(base_path, file))


def jy3_slide_alarm(base_path):
    """
    https://static.geetest.com/static/js/slide.7.8.6.js
    """
    for num in range(600, 800):
        a, b, c = list(str(num))
        file = f"{a}.{b}.{c}.js"
        get_file(f"https://static.geetest.com/static/js/slide.{file}", os.path.join(base_path, file))


def jy3_click_alarm(base_path):
    """
    https://static.geetest.com/static/js/click.3.0.4.js
    """
    for num in range(100, 310):
        a, b, c = list(str(num))
        file = f"{a}.{b}.{c}.js"
        get_file(f"https://static.geetest.com/static/js/click.{file}", os.path.join(base_path, file))


def yidun_alarm(base_path):
    """
    http://cstaticdun.126.net/2.17.4/core.v2.17.4.min.js
    """
    for num in range(100, 200):
        a, b, c = list(str(num))
        file = f"2.{a}{b}.{c}"
        get_file(f"http://cstaticdun.126.net/{file}/core.v{file}.min.js", os.path.join(base_path, file + ".js"))


def shumei_alarm(base_path):
    """
    https://castatic.fengkongcloud.cn/pr/auto-build/v1.0.3-154/captcha-sdk.min.js
    """
    for num in range(100, 155):
        file = f"v1.0.3-{num}.js"
        get_file(f"https://castatic.fengkongcloud.cn/pr/auto-build/v1.0.3-{num}/captcha-sdk.min.js", os.path.join(base_path, file))


# jy3_full_alarm(r"E:\captcha_js\jy3\jy3_fullpage")
# jy3_full_alarm(r"E:\captcha_js\jy3\jy3_slider")
# jy3_click_alarm(r"E:\captcha_js\jy3\jy3_click")
# yidun_alarm(r"E:\captcha_js\yidun")
shumei_alarm(r"E:\captcha_js\shumei")




