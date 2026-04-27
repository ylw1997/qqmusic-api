# qqmusicapi

QQ 音乐 API 文档和测试仓库。

## 内容

- `docs/apis/*.md`: 每个 API 一份 Markdown 文档
- `tests/qqmusic_api_test.py`: Python 测试客户端
- `.github/workflows/check.yml`: 基础语法校验

## 当前支持接口

- [search-songs 搜索歌曲](docs/apis/search-songs.md)
- [search-singers 搜索歌手](docs/apis/search-singers.md)
- [singer-info 获取歌手信息](docs/apis/get-singer-info.md)
- [singer-songs 获取歌手歌曲列表](docs/apis/get-singer-songs.md)
- [song-url 获取歌曲播放链接](docs/apis/get-song-url.md)
- [song-detail 获取歌曲详情](docs/apis/get-song-detail.md)
- [lyric 获取歌词](docs/apis/get-lyric.md)
- [recommend-playlists 获取推荐歌单](docs/apis/get-recommend-playlists.md)
- [playlist-detail 获取歌单详情](docs/apis/get-playlist-detail.md)
- [rank-lists 获取排行榜列表](docs/apis/get-rank-lists.md)
- [rank-detail 获取排行榜详情](docs/apis/get-rank-detail.md)
- [wx-login 微信扫码登录并返回 musicid/musickey](docs/apis/wx-login.md)
- [qq-login-qr 获取 QQ 扫码登录二维码](docs/apis/get-qq-login-qr.md)
- [wx-login-qr 获取微信扫码登录二维码](docs/apis/get-wx-login-qr.md)
- [check-login 轮询扫码登录状态](docs/apis/check-login-status.md)
- [euin 获取加密 uin](docs/apis/get-euin.md)
- [user-info 获取当前登录用户信息](docs/apis/get-user-info.md)
- [my-favorite 获取“我喜欢”的歌曲](docs/apis/get-my-favorite.md)
- [my-playlists 获取我的歌单列表](docs/apis/get-my-playlists.md)
- [add-songs 添加歌曲到歌单](docs/apis/add-songs-to-playlist.md)
- [remove-songs 从歌单删除歌曲](docs/apis/remove-songs-from-playlist.md)
- [radar-recommend 获取雷达推荐](docs/apis/get-radar-recommend.md)
- [guess-recommend 获取猜你喜欢](docs/apis/get-guess-recommend.md)

## 凭据

公开读接口不需要凭据。用户相关、VIP 播放链接、我的歌单等接口需要：

```powershell
$env:QQMUSIC_MUSICID="你的 musicid"
$env:QQMUSIC_MUSICKEY="你的 musickey"
```

脚本不会把凭据写入文件。

## 扫码登录

支持微信扫码登录。脚本会保存并打开二维码图片，扫码确认后自动轮询并输出 `userInfo.musicid` 和 `userInfo.musickey`，之后可以把它们设置为环境变量调用用户相关接口。

```powershell
python tests/qqmusic_api_test.py wx-login
```

只获取二维码，不自动轮询：

```powershell
python tests/qqmusic_api_test.py wx-login-qr
python tests/qqmusic_api_test.py qq-login-qr
```

拿到凭据后：

```powershell
$env:QQMUSIC_MUSICID="扫码返回的 musicid"
$env:QQMUSIC_MUSICKEY="扫码返回的 musickey"
python tests/qqmusic_api_test.py user-info
```

## 测试

```powershell
cd APIS/qqmusicapi
python tests/qqmusic_api_test.py all
```

单独测试：

```powershell
python tests/qqmusic_api_test.py search-songs --keyword "周杰伦"
python tests/qqmusic_api_test.py song-detail --mid 0039MnYb0qxYhV
python tests/qqmusic_api_test.py lyric --mid 0039MnYb0qxYhV
python tests/qqmusic_api_test.py rank-lists
```

写入类接口默认 dry-run，必须显式加 `--execute` 才会真实调用：

```powershell
python tests/qqmusic_api_test.py add-songs --dirid 201 --song-id 123 --execute
```

## 文档

见 [docs/README.md](docs/README.md)。
