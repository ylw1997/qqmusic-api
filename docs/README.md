# QQ 音乐 API 文档

## 通用约定

- `musicu.fcg`: `https://u.y.qq.com/cgi-bin/musicu.fcg`
- `musics.fcg`: `https://u.y.qq.com/cgi-bin/musics.fcg`
- 老搜索接口：`https://c.y.qq.com/...`
- 登录凭据：`musicid` 和 `musickey`
- Cookie 常用字段：`uin`、`qqmusic_key`、`qm_keyst`、`tmeLoginType`

## 当前接口

- [searchSongs 搜索歌曲](apis/search-songs.md)
- [searchSingers 搜索歌手](apis/search-singers.md)
- [getSingerInfo 获取歌手信息](apis/get-singer-info.md)
- [getSingerSongs 获取歌手歌曲](apis/get-singer-songs.md)
- [getSongUrl 获取播放链接](apis/get-song-url.md)
- [getSongDetail 获取歌曲详情](apis/get-song-detail.md)
- [getLyric 获取歌词](apis/get-lyric.md)
- [getRecommendPlaylists 推荐歌单](apis/get-recommend-playlists.md)
- [getPlaylistDetail 歌单详情](apis/get-playlist-detail.md)
- [getRankLists 排行榜列表](apis/get-rank-lists.md)
- [getRankDetail 排行榜详情](apis/get-rank-detail.md)
- [getQQLoginQR 获取 QQ 登录二维码](apis/get-qq-login-qr.md)
- [getWXLoginQR 获取微信登录二维码](apis/get-wx-login-qr.md)
- [checkLoginStatus 检查登录状态](apis/check-login-status.md)
- [getEuin 获取加密 uin](apis/get-euin.md)
- [getUserInfo 获取用户信息](apis/get-user-info.md)
- [getMyFavorite 获取我喜欢](apis/get-my-favorite.md)
- [getMyPlaylists 获取我的歌单](apis/get-my-playlists.md)
- [addSongsToPlaylist 添加歌曲到歌单](apis/add-songs-to-playlist.md)
- [removeSongsFromPlaylist 从歌单删除歌曲](apis/remove-songs-from-playlist.md)
- [getRadarRecommend 雷达推荐](apis/get-radar-recommend.md)
- [getGuessRecommend 猜你喜欢](apis/get-guess-recommend.md)
