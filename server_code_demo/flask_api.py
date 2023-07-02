# -*- coding: utf-8 -*-            
# @Time : 2023/7/2
# @Author: sy
# @公众号: 逆向OneByOne
# @desc: 部署python flask的接口调用测试; vsjyjy 注：CSDN交流
from flask import Flask, request
from loguru import logger
logger.add('flask_api.log', encoding='utf-8')

app = Flask(__name__)


@app.route("/get_ip", methods=['get'])
def get_ip():
    ip = request.remote_addr
    logger.info(f"ip is {ip}")
    return f"your ip is {ip}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8444, debug=True)
