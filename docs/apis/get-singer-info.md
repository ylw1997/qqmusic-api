# getSingerInfo

获取歌手基本信息。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "comm": {},
  "music.UnifiedHomepage.UnifiedHomepageSrv": {
    "method": "GetHomepageHeader",
    "module": "music.UnifiedHomepage.UnifiedHomepageSrv",
    "param": {
      "SingerMid": "0025NhlN2yWrP4"
    }
  }
}
```

## 返回数据

```json
{
  "music.UnifiedHomepage.UnifiedHomepageSrv": {
    "code": 0,
    "data": {
      "Singer": {
        "SingerName": "周杰伦",
        "SingerMid": "0025NhlN2yWrP4"
      }
    }
  }
}
```
