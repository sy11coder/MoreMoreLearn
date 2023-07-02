import base64
import json
import random
import time
import urllib.parse
import cv2
import numpy as np
import requests
import logging
import socket
from urllib.parse import urlencode
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


class ShuMei:

    def __init__(self, organization='RlokQwRlVjUrTUlkIqOg'):
        self.organization = organization
        self.register_url = "https://captcha.fengkongcloud.cn/ca/v1/register"
        self.register_param = {
            "lang": "zh-cn",
            "callback": f"sm_{int(time.time()*1000)}",
            "sdkver": "1.1.3",
            "organization": organization,
            "data": "{}",
            "channel": "DEFAULT",
            "model": "slide",
            "appId": "default",
            "rversion": "1.0.3"
        }
        self.verify_url = "https://captcha.fengkongcloud.cn/ca/v2/fverify"
        self.verify_params = {
            "rversion": "1.0.3",
            "rid": "202204201553452dc06b60e69694bc28",
            "sdkver": "1.1.3",
            "ostype": "web",
            "act.os": "web_pc",
            "organization": organization,
            "callback": f"sm_{int(time.time() * 1000)}",
            "protocol": "154",
            "tf": "qc6EvlfWShKA+4WQjsBi+z9Q4t2bExTkoi6y9rxH9G1ne05joexoOPXI/WjtbftMcYAYC4cZ2BNH3OZBRvkSfYv1od20dvJ83SGlGS17/yJCwq3MLf23SXIzpoRIHFDykt+0gX67as83LYFCirjp+oj519GwqFlIwLPudSnVIfFZNoXaR8oU1XL/sOCw3N2vlB+7VRZQmj1ScL+fP98C2Jd23TNlIgcR2TXuEPQ381W/Fzfh+FCVOxLbohVYo0VI6ErscBJeJyL+wsk9RLc+QVIN+45FxUdr3pBdDS1nHq56baHLJ18dZwv9kMqiMEsC9Z4UjHgYmOclm04ql+kX5j557DQSKk/FnMHQKPHcluhPYZ/dCCQH03EqIFUGwH8FNTJK1hsiaw0IY8MSicGGKnR9NV8ATiQSzo/9Nsyr92JLJQq6QddoyeMrtDXU+2oh6Bb4ww5xZma72X9mv/2KRUyQ+ZRJaX2Ctyl2KzONeZYAWMpj0BbAeWhjHTJ6Leq1r6B4np0O0nkQy5Gsv5IXvZEez+mpgSMXjfUu+HCMHr4=",
            "hi": "3L1LBDxlVcI=",
            "zg": "ZMtxKT/17M0=",
            "ff": "78W89+G0ZGQ=",
            "xh": "4wMy5BxCR+Y=",
            "pt": "PYmzt6l+m1o=",
            "qn": "ySe92kXYlVfucrawVAXCnHZxTkg4Us4/",
            "se": "a5IA4TGudlM=",
            "ty": "hd2AxK/C79g=",
            "jv": "l2l4U7tvE2M=",
            "js": "Zgghk4+YhMA="
        }
        self.res = requests.session()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": "captcha.fengkongcloud.cn",
            "Pragma": "no-cache",
            "Referer": "https://www.ishumei.com/trial/captcha.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }
        self.img_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

    def url_requests(self, url, form_data=None, headers=None):
        for i in range(2):
            try:
                headers = headers if headers else self.headers
                if form_data:
                    resp = requests.post(url, headers=headers, data=form_data, timeout=10)
                else:
                    resp = requests.get(url, headers=headers, timeout=10)
                if resp.status_code != 200:
                    time.sleep(5)
                    raise Exception(f'{url} {resp.status_code}')
                resp.encoding = resp.apparent_encoding
            except socket.error as err:
                logging.warning(f"socket timeout {err} ")
            except Exception as _e:
                time.sleep(random.uniform(1, 2.5))
                logging.exception(f'requests_error:{_e}')
            else:
                if not resp:
                    continue
                return resp

    @staticmethod
    def get_trajectory(distance):
        ge = []
        y = 0
        v = 0
        t = 1
        current = 0
        mid = distance * 3 / 4
        exceed = 20
        z = t
        ge.append([0, 0, 1])
        while current < (distance + exceed):
            if current < mid / 2:
                a = 15
            elif current < mid:
                a = 20
            else:
                a = -30
            a /= 2
            v0 = v
            s = v0 * t + 0.5 * a * (t * t)
            current += int(s)
            v = v0 + a * t
            y += random.randint(-5, 5)
            z += 100 + random.randint(0, 10)
            ge.append([min(current, (distance + exceed)), y, z])
        while exceed > 0:
            exceed -= random.randint(0, 5)
            y += random.randint(-5, 5)
            z += 100 + random.randint(0, 10)
            ge.append([min(current, (distance + exceed)), y, z])
        return ge

    @staticmethod
    def get_trace(distance):
        ge = list()
        ge.append([0, 0, 0])
        for i in range(10):
            x = 0
            y = random.randint(-1, 1)
            t = 100 * (i + 1) + random.randint(0, 2)
            ge.append([x, y, t])
        for items in ge[1:-5]:
            items[0] = distance // 2
        for items in ge[-5:-1]:
            items[0] = distance + random.randint(1, 4)
        ge[-1][0] = distance
        return ge

    @staticmethod
    def des_encrypt(text, key):
        """des ecb 加密"""
        des_obj = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        encrypt_text = des_obj.encrypt(pad(str(text).encode('utf-8'), DES.block_size, style='x923')[:-1] + bytes([0]))
        return base64.b64encode(encrypt_text).decode('utf-8')

    def tongcheng_register(self):
        url = "https://jpebook.ly.com/suppliersharing/Account/Login"
        headers = {
            "Host": "jpebook.ly.com",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
            "Origin": "https://jpebook.ly.com",
            "Referer": "https://jpebook.ly.com/suppliersharing/Account/Login",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        data = {
            "type": 0,
            "loginName": "18778232132131",
            "password": "572e634ed953cab490d880129a469ba9",
            "checkPassword": "",
            "validCode": "",
            "codeResponse": self.verify_params['rid'],
            "codeType": "sm"
        }
        print(data)
        res = self.url_requests(url, json.dumps(data), headers=headers)
        print(f"同程结果： {res.text}")

    def verify_captcha(self, distance):
        """校验验证码"""
        # 滑动轨迹
        trace = self.get_trajectory(distance/2)
        print(f"滑块验证码的识别轨迹是: {trace}")
        self.verify_params.update({
            "protocol": "154",  # 版本号
            "qn": self.des_encrypt(distance / 2 / 300, 'd1a34ee5'),  # 距离识别 211  滑块长度300 密钥与版本js相关  7
            "tf": self.des_encrypt(trace, "1c4e7292"),  # 轨迹加密  密钥  9
            "se": self.des_encrypt(trace[-1][1] + random.randint(20, 100), 'e34f1f2e'),  # 滑动时长  密钥与版本js相关  2
            "js": self.des_encrypt(300, 'ef96fa60'),  # 滑块长度  密钥与版本js相关  10
            "pt": self.des_encrypt(150, '0c661344'),  # 滑块宽度  密钥与版本js相关  6
            "jv": self.des_encrypt(1, '1a72a3c8'),  # .console  密钥与版本js相关  3
            "zg": self.des_encrypt(0, "141de9de"),  # runBotDetection  密钥与版本js相关
            "xh": self.des_encrypt(-1, '01176adf'),  # 密钥与版本js相关  5
            "ty": self.des_encrypt('default', "6237dbfd"),  # "hd2AxK/C79g=",
            "ff": self.des_encrypt('DEFAULT', '8f91d85a'),  # "78W89+G0ZGQ=",  1
            "hi": self.des_encrypt('zh-cn', 'd9514b1e'),  # "3L1LBDxlVcI=",  8
        })
        url = f"{self.verify_url}?{urlencode(self.verify_params)}"
        res = self.url_requests(url)
        print(f"校验验证码: {res.text}")
        if json.loads(res.text[17:-1])["riskLevel"] == "PASS":
            return True

    def get_captcha(self):
        """请求验证码"""
        url = f"{self.register_url}?{urlencode(self.register_param)}"
        response = self.url_requests(url)
        print(f"请求验证码{response.text}")
        sm_json = json.loads(response.text[17:-1])
        bg = sm_json["detail"]["bg"]
        fg = sm_json["detail"]["fg"]
        bg_url = urllib.parse.urljoin("https://castatic.fengkongcloud.cn/", bg)
        fg_url = urllib.parse.urljoin("https://castatic.fengkongcloud.cn/", fg)
        rid = sm_json["detail"]["rid"]
        self.verify_params.update({"rid": rid})
        print(f"滑块验证码url {rid} bg_url: {bg_url} fg_url: {fg_url}")
        fg_content = self.url_requests(fg_url, headers=self.img_headers).content
        bg_content = self.url_requests(bg_url, headers=self.img_headers).content
        target = cv2.imdecode(np.asarray(bytearray(fg_content), dtype=np.uint8), 0)
        template = cv2.imdecode(np.asarray(bytearray(bg_content), dtype=np.uint8), 0)
        result = cv2.matchTemplate(target, template, cv2.TM_CCORR_NORMED)
        _, distance = np.unravel_index(result.argmax(), result.shape)
        return distance

    def process(self):
        # print(self.get_trace(213))
        # print(self.get_trajectory(213))
        # 请求验证码
        distance = self.get_captcha()
        print(f"滑块验证码的识别距离是: {distance}")
        # 校验验证码
        flag = self.verify_captcha(distance)
        # 同程校验
        if flag:
            self.tongcheng_register()


if __name__ == '__main__':
    # # 官网
    # _obj = ShuMei("RlokQwRlVjUrTUlkIqOg")
    # _obj.process()

    # 官网
    _obj = ShuMei("xQsKB7v2qSFLFxnvmjdO")
    _obj.process()



























