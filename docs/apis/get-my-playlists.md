# getMyPlaylists

获取我的歌单列表。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 是

## Body

```json
{
  "music.musicasset.PlaylistBaseRead": {
    "method": "GetPlaylistByUin",
    "module": "music.musicasset.PlaylistBaseRead",
    "param": {
      "uin": "musicid"
    }
  }
}
```

## 返回数据

```json
{
  "music.musicasset.PlaylistBaseRead": {
    "data": {
      "v_playlist": [
        {
          "tid": 123,
          "dirId": 201,
          "dirName": "我喜欢",
          "songNum": 100
        }
      ]
    }
  }
}
```
