var express = require('express');
var dayjs = require("dayjs");
var bodyParser = require('body-parser');
var winston=require('winston'); // https://www.cnblogs.com/maxiaocang/p/16377933.html
var Ljresp = require('./express_demo_lj.js');

// 日志设置
const colors = {error: "red", info: "green"};
const timezone = () => {return dayjs().format("YYYY-MM-DDTHH:mm:ss.SSS");};
const formatter = winston.format.printf((info) => {return `[${info.timestamp}] [${info.level}] - ${info.message} `;});
var logger = winston.createLogger({
    transports: [
        new (winston.transports.Console)(),
        new (winston.transports.File)({
            filename: '/data/logs/eea.log',
            timestamp:'true',
            maxsize: 1048576*2, //日志文件的大小 2M
            maxFiles: 2,
            level: 'info' // info文件内会记录info级别的log和比info级别高的log，比如error
        }),
        new (winston.transports.File)({
            filename: '/data/logs/eeb.log',
            timestamp:'true',
            maxsize: 10485760*3, // 3M
            maxFiles: 2,
            level: 'error'  // error级别比info要高，error.log文件只会记录error日志
        }),
    ],
    format: winston.format.combine(
        winston.format.colorize(),
        winston.format.timestamp({ format: timezone }),
        formatter
    )
});

// 获取客户端真实ip
function getClientIp(req, count_flag) {
    var cur_ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress ||req.socket.remoteAddress || req.connection.socket.remoteAddress;
    var cur_ip = cur_ip+"";
    var cur_ip = cur_ip.split(":");
    var req_ip = cur_ip[cur_ip.length-1];
    logger.info('>>>req_ip===='+req_ip);
    return req_ip
};


// express接口
var app = express();
app.use(bodyParser.json({limit: '2mb'}));
app.use(bodyParser.urlencoded({limit: '2mb', extended: true}));
// http://127.0.0.1:8444/jkip
app.get("/jkip", async (req, res) =>{
    try {
        var req_ip = getClientIp(req, false);
        res.send("your ip is " + req_ip);
    } catch (err) {
        logger.error(err);
        res.status(500).send('Internal Server Error');
  }
});
// lat_lng的js文件请求： http://127.0.0.1:8444/lj_enc
app.post("/lj_enc", async (req, res) =>{
    try {
        var lant =  req.body;
        logger.info('>>>req_lant===='+lant);
        res.status(200).send(Ljresp(lant))
    } catch (err) {
        logger.error(err);
        res.status(500).send('Internal Server Error');
  }
});


const server = app.listen(8444);
console.log("server start...")
