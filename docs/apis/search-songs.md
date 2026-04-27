# searchSongs

搜索歌曲。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.search.SearchCgiService": {
    "method": "DoSearchForQQMusicDesktop",
    "module": "music.search.SearchCgiService",
    "param": {
      "query": "周杰伦",
      "pageNum": 1,
      "numPerPage": 20,
      "search_type": 0
    }
  }
}
```

## 返回数据

```json
{
  "code": 0,
  "music.search.SearchCgiService": {
    "code": 0,
    "data": {
      "body": {
        "song": {
          "list": []
        }
      },
      "meta": {
        "curpage": 1,
        "query": "周杰伦"
      }
    }
  }
}
```
