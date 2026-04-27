# getRadarRecommend

获取雷达推荐列表。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 通常不需要，登录后结果可能更个性化

## Body

```json
{
  "music.recommend.TrackRelationServer": {
    "method": "GetRadarSong",
    "module": "music.recommend.TrackRelationServer",
    "param": {
      "Page": 1,
      "ReqType": 0,
      "FavSongs": [],
      "EntranceSongs": []
    }
  }
}
```

## 返回数据

```json
{
  "music.recommend.TrackRelationServer": {
    "data": {}
  }
}
```
