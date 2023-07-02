# -*- coding: utf-8 -*-            
# @Time : 2023/7/2
# @Author: sy
# @公众号: 逆向OneByOne
# @desc: express接口调用案例; vsjyjy 注：CSDN交流
import requests
from loguru import logger
logger.add('express_api.log', encoding='utf-8')

lat_lng = {
    "lng": 120.5811424828,
    "lat": 31.3010678543,
    "Se": "inner",
    "num": 12
}
url = f"http://127.0.0.1:8444/lj_enc"
# url = f"http://101.37.149.41:8444/lj_enc"
resp = requests.post(url, data=lat_lng, timeout=10)
logger.success(f"req_response {resp.text}")

# 最终输出结果如下
# {'maxLatitude': 31.532069843198276, 'minLatitude': 31.069492306296034, 'maxLongitude': 120.91171891047182, 'minLongitude': 120.25056605512805}
