# getLyric

获取歌曲歌词。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.musichallSong.PlayLyricInfo": {
    "method": "GetPlayLyricInfo",
    "module": "music.musichallSong.PlayLyricInfo",
    "param": {
      "songMid": "0039MnYb0qxYhV"
    }
  }
}
```

## 返回数据

```json
{
  "music.musichallSong.PlayLyricInfo": {
    "data": {
      "lyric": "[00:00.00]..."
    }
  }
}
```
