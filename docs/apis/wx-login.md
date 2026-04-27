# wxLogin

微信扫码登录并返回 QQ 音乐凭据。

## 脚本命令

```powershell
python tests/qqmusic_api_test.py wx-login
```

脚本会：

- 请求微信登录二维码
- 保存二维码到 `responses/wx-login-qr.jpg`
- 默认打开二维码图片
- 轮询扫码状态
- 扫码确认后用 `wx_code` 换取 `musicid` 和 `musickey`

## 请求流程

### 1. 获取二维码

见 [getWXLoginQR](get-wx-login-qr.md)。

### 2. 轮询微信扫码状态

- Method: `GET`
- URL: `https://lp.open.weixin.qq.com/connect/l/qrconnect`
- Query: `uuid={identifier}`

扫码确认后响应里会出现 `window.wx_code`。

### 3. 换取 QQ 音乐凭据

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`

请求体核心字段：

```json
{
  "comm": {
    "tmeLoginType": "1"
  },
  "music.login.LoginServer.Login": {
    "module": "music.login.LoginServer",
    "method": "Login",
    "param": {
      "code": "微信扫码返回的 wx_code",
      "strAppid": "wx48db31d50e334801"
    }
  }
}
```

## 返回数据

```json
{
  "status": "success",
  "qr": {
    "identifier": "uuid",
    "type": "wx",
    "image_path": "responses/wx-login-qr.jpg",
    "opened": true
  },
  "userInfo": {
    "musicid": "123456",
    "musickey": "W_X...",
    "refresh_key": "",
    "refresh_token": "",
    "nickname": ""
  }
}
```
