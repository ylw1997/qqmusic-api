# addSongsToPlaylist

添加歌曲到歌单。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 是
- 是否写入: 是

## Body

```json
{
  "music.musicasset.PlaylistDetailWrite": {
    "method": "AddSonglist",
    "module": "music.musicasset.PlaylistDetailWrite",
    "param": {
      "dirId": 201,
      "v_songInfo": [
        {
          "songType": 0,
          "songId": 97773
        }
      ]
    }
  }
}
```

## 返回数据

```json
{
  "music.musicasset.PlaylistDetailWrite": {
    "data": {
      "result": {
        "updateTime": 1710000000
      }
    }
  }
}
```
