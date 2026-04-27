# getSongDetail

获取歌曲详情。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.pf_song_detail_svr": {
    "method": "get_song_detail_yqq",
    "module": "music.pf_song_detail_svr",
    "param": {
      "song_mid": "0039MnYb0qxYhV"
    }
  }
}
```

## 返回数据

```json
{
  "music.pf_song_detail_svr": {
    "data": {
      "track_info": {
        "mid": "0039MnYb0qxYhV",
        "name": "晴天",
        "singer": [],
        "album": {},
        "interval": 269
      }
    }
  }
}
```
