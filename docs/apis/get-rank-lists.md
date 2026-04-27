# getRankLists

获取排行榜列表。

## 请求

- Method: `POST`
- URL: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- 是否需要凭据: 否

## Body

```json
{
  "music.musicToplist.Toplist.GetAll": {
    "module": "music.musicToplist.Toplist",
    "method": "GetAll",
    "param": {}
  }
}
```

## 返回数据

```json
{
  "music.musicToplist.Toplist.GetAll": {
    "data": {
      "group": [
        {
          "toplist": [
            {
              "topId": 4,
              "title": "流行指数榜",
              "headPicUrl": "https://...",
              "update_key": "..."
            }
          ]
        }
      ]
    }
  }
}
```
