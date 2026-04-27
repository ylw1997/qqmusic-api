# getRankDetail

获取排行榜详情。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.musicToplist.Toplist.GetDetail": {
    "module": "music.musicToplist.Toplist",
    "method": "GetDetail",
    "param": {
      "topId": 4,
      "offset": 0,
      "num": 30,
      "withTags": false
    }
  }
}
```

## 返回数据

```json
{
  "music.musicToplist.Toplist.GetDetail": {
    "data": {
      "topId": 4,
      "title": "流行指数榜",
      "songInfoList": []
    }
  }
}
```
