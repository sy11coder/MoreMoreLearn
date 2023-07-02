# -*- coding: utf-8 -*-            
# @Time : 2023/7/2
# @Author: sy
# @公众号: 逆向OneByOne
# @desc: 企业微信群报警; vsjyjy 注：CSDN交流
import json
import requests
from loguru import logger
logger.add('crawl_news.log', encoding='utf-8')
Robot_key = {"sy_robot": "c18541b3-7378-1dca-9821-21db8e68b100"}  # 企业微信机器人的key
Robot_user = {"all": ["@all"], "sy": ["18810011001"]}  # 手机号随意写的


class Monitor:
    @staticmethod
    def wechat_monitor_alarm(robot_key, user, text):
        """
        企业微信机器人报警
        """
        try:
            data = {
                "msgtype": "text",
                "text": {
                    "content": text,
                    "mentioned_mobile_list": Robot_user[user]
                }
            }
            url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={Robot_key[robot_key]}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
            res = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
            logger.info(f"{res.status_code}, {res.text}, 传送成功")
            return True
        except Exception as err:
            logger.warning(f"monitor alarm error happen: {err}")


Monitor.wechat_monitor_alarm("sy_robot", "all", "测试企业报警")

