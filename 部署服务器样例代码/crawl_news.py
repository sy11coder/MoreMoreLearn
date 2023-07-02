# -*- coding: utf-8 -*-            
# @Time : 2023/7/2
# @Author: sy
# @公众号: 逆向OneByOne
# @url: http://ybj.beijing.gov.cn/zwgk/2020_zcjd/
# @desc: 部署定时爬虫脚本，学习案例，请勿并发攻击网站; 每日定时爬取; vsjyjy 注：CSDN交流
import requests
from loguru import logger
from lxml import etree
from urllib import parse
from apscheduler.schedulers.blocking import BlockingScheduler
logger.add('crawl_news.log', encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
ses = requests.session()


def _requests(url, data=None):
    if data:
        res = ses.post(url, headers=headers, data=data, timeout=10)
    else:
        res = ses.get(url, headers=headers, timeout=10)
    logger.debug(f">>>requests {url}")
    logger.success(f">>>status_code 【{res.status_code}】 res.cookies {res.cookies}")
    if res.status_code in [521, 412, 202, 200]:
        return res


def list_main():
    url = "http://ybj.beijing.gov.cn/zwgk/2020_zcjd/"
    resp = _requests(url)
    html = etree.HTML(resp.text)
    for tag in html.xpath('//ul[@class="text_list"]//li/a'):
        title = tag.xpath("string(.)").strip()
        href = parse.urljoin(url, tag.attrib['href'])
        logger.info(f">>>detail_title {title} detail_url {href}")


list_main()
# 每天2点半定时执行
scheduler = BlockingScheduler(timezone='Asia/Shanghai')
scheduler.add_job(list_main, 'cron', hour=2, minute=30, args=(), max_instances=100, misfire_grace_time=360)
scheduler.start()
