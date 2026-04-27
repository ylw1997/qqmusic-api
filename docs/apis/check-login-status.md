# checkLoginStatus

检查 QQ 或微信二维码登录状态。

## QQ 请求

- Method: `GET`
- URL: `https://ssl.ptlogin2.qq.com/ptqrlogin`
- Cookie: `qrsig={identifier}`

核心参数：

```json
{
  "u1": "https://y.qq.com/",
  "ptqrtoken": "hash33(qrsig)",
  "aid": "716027609",
  "daid": "383",
  "pt_3rd_aid": "100497308"
}
```

## 微信请求

- Method: `GET`
- URL: `https://lp.open.weixin.qq.com/connect/l/qrconnect`
- Query: `uuid={identifier}`

## 返回数据

```json
{
  "status": "pending | scanning | success | failed | timeout",
  "userInfo": {
    "musicid": "",
    "musickey": "",
    "nickname": ""
  }
}
```
