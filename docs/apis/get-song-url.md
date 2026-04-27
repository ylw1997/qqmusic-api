# getSongUrl

获取歌曲播放链接。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 部分歌曲、VIP 音质需要

## Body

```json
{
  "comm": {
    "ct": "19"
  },
  "music.vkey.GetVkey.UrlGetVkey": {
    "method": "UrlGetVkey",
    "module": "music.vkey.GetVkey",
    "param": {
      "filename": ["M5000039MnYb0qxYhV0039MnYb0qxYhV.mp3"],
      "guid": "32 hex chars",
      "songmid": ["0039MnYb0qxYhV"],
      "songtype": [0]
    }
  }
}
```

## 返回数据

```json
{
  "music.vkey.GetVkey.UrlGetVkey": {
    "data": {
      "midurlinfo": [
        {
          "purl": "C400....m4a?...",
          "pneedbuy": 0,
          "uiAlert": 0
        }
      ]
    }
  }
}
```

最终播放 URL 为：`https://isure.stream.qqmusic.qq.com/{purl}`。
