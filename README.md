# qqmusicapi

QQ 音乐 API 文档和测试仓库。

## 内容

- `docs/apis/*.md`: 每个 API 一份 Markdown 文档
- `tests/qqmusic_api_test.py`: Python 测试客户端
- `.github/workflows/check.yml`: 基础语法校验

## 凭据

公开读接口不需要凭据。用户相关、VIP 播放链接、我的歌单等接口需要：

```powershell
$env:QQMUSIC_MUSICID="你的 musicid"
$env:QQMUSIC_MUSICKEY="你的 musickey"
```

脚本不会把凭据写入文件。

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
