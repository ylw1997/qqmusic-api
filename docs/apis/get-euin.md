# getEuin

根据 `musicid` 获取加密 `uin`，用于访问“我喜欢”等个人歌单。

## 请求

- Method: `GET`
- URL: `https://c6.y.qq.com/rsc/fcgi-bin/fcg_get_profile_homepage.fcg`
- 是否需要凭据: 通常不需要，但需要有效 `musicid`

## Query 参数

```json
{
  "ct": 20,
  "cv": 4747474,
  "cid": 205360838,
  "userid": "musicid"
}
```

## 返回数据

```json
{
  "data": {
    "creator": {
      "encrypt_uin": "..."
    }
  }
}
```
