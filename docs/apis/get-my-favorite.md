# getMyFavorite

获取“我喜欢”的歌曲列表。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 是

## Body

```json
{
  "music.srfDissInfo.DissInfo": {
    "method": "CgiGetDiss",
    "module": "music.srfDissInfo.DissInfo",
    "param": {
      "disstid": 0,
      "dirid": 201,
      "song_begin": 0,
      "song_num": 30,
      "enc_host_uin": "encrypted uin"
    }
  }
}
```

## 返回数据

```json
{
  "music.srfDissInfo.DissInfo": {
    "data": {
      "total_song_num": 100,
      "songlist": []
    }
  }
}
```
