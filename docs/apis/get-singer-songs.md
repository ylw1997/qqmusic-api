# getSingerSongs

获取歌手歌曲列表。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "musichall.song_list_server": {
    "method": "GetSingerSongList",
    "module": "musichall.song_list_server",
    "param": {
      "singerMid": "0025NhlN2yWrP4",
      "order": 1,
      "number": 20,
      "begin": 0
    }
  }
}
```

## 返回数据

```json
{
  "musichall.song_list_server": {
    "code": 0,
    "data": {
      "songList": [
        {
          "songInfo": {
            "mid": "0039MnYb0qxYhV",
            "name": "晴天",
            "singer": []
          }
        }
      ]
    }
  }
}
```
