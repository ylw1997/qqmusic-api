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
  "identifier": "uuid",
  "type": "wx",
  "image_path": "responses/wx-login-qr.jpg",
  "opened": true,
  "image_base64_prefix": "/9j/4AAQSk..."
}
```

脚本命令 `python tests/qqmusic_api_test.py wx-login-qr` 会把二维码保存成图片，方便直接扫码。
