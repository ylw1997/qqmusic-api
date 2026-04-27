# getPlaylistDetail

获取歌单详情。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.srfDissInfo.DissInfo": {
    "method": "CgiGetDiss",
    "module": "music.srfDissInfo.DissInfo",
    "param": {
      "disstid": 123,
      "dirid": 0,
      "tag": true,
      "song_begin": 0,
      "song_num": 30,
      "userinfo": true,
      "orderlist": true,
      "onlysonglist": false
    }
  }
}
```

## 返回数据

```json
{
  "music.srfDissInfo.DissInfo": {
    "data": {
      "dirinfo": {
        "id": 123,
        "title": "歌单标题",
        "picurl": "https://..."
      },
      "total_song_num": 30,
      "songlist": []
    }
  }
}
```
