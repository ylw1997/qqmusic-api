# searchSingers

搜索歌手。

## 请求

- Method: `GET`
- URL: `https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg`
- 是否需要凭据: 否

## Query 参数

```json
{
  "key": "周杰伦"
}
```

## 返回数据

```json
{
  "code": 0,
  "data": {
    "singer": {
      "itemlist": [
        {
          "id": "4558",
          "mid": "0025NhlN2yWrP4",
          "name": "周杰伦"
        }
      ]
    }
  }
}
```
