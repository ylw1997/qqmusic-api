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

单独检查状态时返回原始轮询结果：

```json
{
  "status_code": 200,
  "raw": "window.wx_errcode=408;..."
}
```

完整微信扫码登录请使用 [wxLogin](wx-login.md)，成功后会返回：

```json
{
  "status": "success",
  "userInfo": {
    "musicid": "123456",
    "musickey": "W_X...",
    "nickname": ""
  }
}
```
