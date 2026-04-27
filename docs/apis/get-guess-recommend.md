# getGuessRecommend

获取猜你喜欢/个性电台。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 通常不需要，登录后结果可能更个性化

## Body

```json
{
  "music.radioProxy.MbTrackRadioSvr": {
    "method": "get_radio_track",
    "module": "music.radioProxy.MbTrackRadioSvr",
    "param": {
      "id": 99,
      "num": 5,
      "from": 0,
      "scene": 0,
      "song_ids": [],
      "ext": {
        "bluetooth": ""
      },
      "should_count_down": 1
    }
  }
}
```

## 返回数据

```json
{
  "music.radioProxy.MbTrackRadioSvr": {
    "data": {}
  }
}
```
