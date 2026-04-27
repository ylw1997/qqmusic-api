# getUserInfo

获取当前登录用户信息。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 是

## Body

```json
{
  "music.UserInfo.userInfoServer": {
    "method": "GetLoginUserInfo",
    "module": "music.UserInfo.userInfoServer",
    "param": {}
  }
}
```

## 返回数据

```json
{
  "music.UserInfo.userInfoServer": {
    "data": {
      "info": {
        "nick": "昵称",
        "logo": "https://..."
      }
    }
  }
}
```
