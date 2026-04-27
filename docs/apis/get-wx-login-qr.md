# getWXLoginQR

获取微信登录二维码。

## 请求流程

### 1. 获取 uuid

- Method: `GET`
- URL: `https://open.weixin.qq.com/connect/qrconnect`

### 2. 获取二维码

- Method: `GET`
- URL: `https://open.weixin.qq.com/connect/qrcode/{uuid}`

## 返回数据

```json
{
  "data": "data:image/jpeg;base64,...",
  "identifier": "uuid",
  "type": "wx"
}
```
