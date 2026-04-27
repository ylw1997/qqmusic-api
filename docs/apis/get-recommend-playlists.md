# getRecommendPlaylists

获取推荐歌单。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.playlist.PlaylistSquare.GetRecommendFeed": {
    "module": "music.playlist.PlaylistSquare",
    "method": "GetRecommendFeed",
    "param": {
      "From": 0,
      "Size": 10
    }
  }
}
```

## 返回数据

```json
{
  "music.playlist.PlaylistSquare.GetRecommendFeed": {
    "data": {
      "List": [
        {
          "Playlist": {
            "basic": {
              "tid": 123,
              "title": "歌单标题",
              "song_cnt": 30,
              "play_cnt": 1000
            }
          }
        }
      ]
    }
  }
}
```
