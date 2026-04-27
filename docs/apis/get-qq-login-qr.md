# getQQLoginQR

获取 QQ 登录二维码。

## 请求

- Method: `GET`
- URL: `https://ssl.ptlogin2.qq.com/ptqrshow`
- 是否需要凭据: 否

## Query 参数

```json
{
  "appid": "716027609",
  "e": "2",
  "l": "M",
  "s": "3",
  "d": "72",
  "v": "4",
  "daid": "383",
  "pt_3rd_aid": "100497308"
}
```

## 返回数据

响应体是二维码图片。响应头 `set-cookie` 中包含 `qrsig`，用于轮询登录状态。

```json
{
  "data": "data:image/png;base64,...",
  "identifier": "qrsig",
  "type": "qq"
}
```
