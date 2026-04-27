import argparse
import base64
import hashlib
import json
import os
import random
import re
import string
import sys
import time
from typing import Any

import requests


BASE_URL = "https://u.y.qq.com/cgi-bin/musicu.fcg"
VERSION_CODE = 13020508
DEFAULT_SONG_MID = "0039MnYb0qxYhV"
DEFAULT_SINGER_MID = "0025NhlN2yWrP4"
DEFAULT_TOP_ID = 4


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2)[:8000])


def guid() -> str:
    return "".join(random.choice("0123456789abcdef") for _ in range(32))


def headers(extra: dict[str, str] | None = None) -> dict[str, str]:
    value = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://y.qq.com/",
        "Origin": "https://y.qq.com",
    }
    if extra:
        value.update(extra)
    return value


def common_params(credential: dict[str, str] | None = None, ct: str = "11") -> dict[str, Any]:
    comm = {
        "cv": VERSION_CODE,
        "v": VERSION_CODE,
        "ct": ct,
        "tmeAppID": "qqmusic",
        "format": "json",
        "inCharset": "utf-8",
        "outCharset": "utf-8",
        "uid": "0",
    }
    if credential:
        musicid = credential["musicid"]
        musickey = credential["musickey"]
        login_type = "1" if musickey.startswith("W_X") else "2"
        comm.update(
            {
                "uid": musicid,
                "qq": musicid,
                "authst": musickey,
                "tmeLoginType": login_type,
                "loginUin": musicid,
                "tmeAppID": "qqmusic",
            }
        )
    return comm


def credential_from_env() -> dict[str, str] | None:
    musicid = os.getenv("QQMUSIC_MUSICID")
    musickey = os.getenv("QQMUSIC_MUSICKEY")
    if musicid and musickey:
        return {"musicid": musicid, "musickey": musickey}
    return None


def cookie_for(credential: dict[str, str] | None) -> str:
    if not credential:
        return ""
    musicid = credential["musicid"]
    musickey = credential["musickey"]
    login_type = "1" if musickey.startswith("W_X") else "2"
    cookie = f"uin={musicid}; qqmusic_key={musickey}; qm_keyst={musickey}; tmeLoginType={login_type};"
    if login_type == "1":
        cookie += f" wxuin={musicid};"
    return cookie


def post_musicu(payload: dict[str, Any], credential: dict[str, str] | None = None) -> dict[str, Any]:
    body = dict(payload)
    body["comm"] = {**common_params(credential), **body.get("comm", {})}
    req_headers = headers()
    cookie = cookie_for(credential)
    if cookie:
        req_headers["Cookie"] = cookie
    response = requests.post(BASE_URL, json=body, headers=req_headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    if data.get("code") not in (0, None):
        raise RuntimeError(data.get("msg") or f"musicu code={data.get('code')}")
    return data


def hash33(value: str) -> int:
    result = 0
    for ch in value:
        result += (result << 5) + ord(ch)
    return result & 2147483647


def summarize(name: str, func) -> dict[str, Any]:
    try:
        data = func()
        return {"api": name, "ok": True, "summary": summarize_value(data)}
    except Exception as error:
        return {"api": name, "ok": False, "error": str(error)}


def summarize_value(data: Any) -> Any:
    if isinstance(data, dict):
        keys = list(data.keys())
        return {"type": "object", "keys": keys[:10]}
    if isinstance(data, list):
        return {"type": "array", "length": len(data)}
    if isinstance(data, str):
        return {"type": "string", "length": len(data)}
    return {"type": type(data).__name__}


class QQMusicClient:
    def __init__(self) -> None:
        self.credential = credential_from_env()
        self.session = requests.Session()

    def search_songs(self, keyword: str, page: int = 1, num: int = 20) -> Any:
        return post_musicu(
            {
                "music.search.SearchCgiService": {
                    "method": "DoSearchForQQMusicDesktop",
                    "module": "music.search.SearchCgiService",
                    "param": {
                        "query": keyword,
                        "pageNum": page,
                        "numPerPage": num,
                        "search_type": 0,
                    },
                }
            },
            self.credential,
        )

    def search_singers(self, keyword: str) -> Any:
        response = self.session.get(
            "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg",
            params={"key": keyword},
            headers=headers(),
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def song_url(self, mid: str, quality: int = 128) -> Any:
        file_type, ext = ("M500", ".mp3")
        if quality == 320:
            file_type, ext = ("M800", ".mp3")
        elif quality == 999:
            file_type, ext = ("F000", ".flac")
        filename = f"{file_type}{mid}{mid}{ext}"
        return post_musicu(
            {
                "comm": {"ct": "19"},
                "music.vkey.GetVkey.UrlGetVkey": {
                    "method": "UrlGetVkey",
                    "module": "music.vkey.GetVkey",
                    "param": {
                        "filename": [filename],
                        "guid": guid(),
                        "songmid": [mid],
                        "songtype": [0],
                    },
                },
            },
            self.credential,
        )

    def song_detail(self, mid: str) -> Any:
        return post_musicu(
            {
                "music.pf_song_detail_svr": {
                    "method": "get_song_detail_yqq",
                    "module": "music.pf_song_detail_svr",
                    "param": {"song_mid": mid},
                }
            },
            self.credential,
        )

    def lyric(self, mid: str) -> Any:
        return post_musicu(
            {
                "music.musichallSong.PlayLyricInfo": {
                    "method": "GetPlayLyricInfo",
                    "module": "music.musichallSong.PlayLyricInfo",
                    "param": {"songMid": mid},
                }
            },
            self.credential,
        )

    def recommend_playlists(self, num: int = 10) -> Any:
        return post_musicu(
            {
                "music.playlist.PlaylistSquare.GetRecommendFeed": {
                    "module": "music.playlist.PlaylistSquare",
                    "method": "GetRecommendFeed",
                    "param": {"From": 0, "Size": num},
                }
            },
            self.credential,
        )

    def playlist_detail(self, dissid: int, page: int = 1, num: int = 30) -> Any:
        return post_musicu(
            {
                "music.srfDissInfo.DissInfo": {
                    "method": "CgiGetDiss",
                    "module": "music.srfDissInfo.DissInfo",
                    "param": {
                        "disstid": dissid,
                        "dirid": 0,
                        "tag": True,
                        "song_begin": (page - 1) * num,
                        "song_num": num,
                        "userinfo": True,
                        "orderlist": True,
                        "onlysonglist": False,
                    },
                }
            },
            self.credential,
        )

    def rank_lists(self) -> Any:
        return post_musicu(
            {
                "music.musicToplist.Toplist.GetAll": {
                    "module": "music.musicToplist.Toplist",
                    "method": "GetAll",
                    "param": {},
                }
            },
            self.credential,
        )

    def rank_detail(self, top_id: int = DEFAULT_TOP_ID, page: int = 1, num: int = 30) -> Any:
        return post_musicu(
            {
                "music.musicToplist.Toplist.GetDetail": {
                    "module": "music.musicToplist.Toplist",
                    "method": "GetDetail",
                    "param": {
                        "topId": top_id,
                        "offset": num * (page - 1),
                        "num": num,
                        "withTags": False,
                    },
                }
            },
            self.credential,
        )

    def qq_login_qr(self) -> Any:
        response = self.session.get(
            "https://ssl.ptlogin2.qq.com/ptqrshow",
            params={
                "appid": "716027609",
                "e": "2",
                "l": "M",
                "s": "3",
                "d": "72",
                "v": "4",
                "t": str(random.random()),
                "daid": "383",
                "pt_3rd_aid": "100497308",
            },
            timeout=30,
        )
        response.raise_for_status()
        qrsig = ""
        for cookie in response.headers.get("set-cookie", "").split(","):
            match = re.search(r"qrsig=([^;]+)", cookie)
            if match:
                qrsig = match.group(1)
                break
        return {
            "identifier": qrsig,
            "type": "qq",
            "image_base64_prefix": base64.b64encode(response.content).decode("ascii")[:60],
        }

    def wx_login_qr(self) -> Any:
        response = self.session.get(
            "https://open.weixin.qq.com/connect/qrconnect",
            params={
                "appid": "wx48db31d50e334801",
                "redirect_uri": "https://y.qq.com/portal/wx_redirect.html?login_type=2&surl=https://y.qq.com/",
                "response_type": "code",
                "scope": "snsapi_login",
                "state": "STATE",
                "href": "https://y.qq.com/mediastyle/music_v17/src/css/popup_wechat.css#wechat_redirect",
            },
            headers=headers(),
            timeout=30,
        )
        response.raise_for_status()
        match = re.search(r"uuid=(.+?)\"", response.text)
        if not match:
            raise RuntimeError("uuid not found")
        uuid = match.group(1)
        qr = self.session.get(
            f"https://open.weixin.qq.com/connect/qrcode/{uuid}",
            headers=headers({"Referer": "https://open.weixin.qq.com/connect/qrconnect"}),
            timeout=30,
        )
        qr.raise_for_status()
        return {"identifier": uuid, "type": "wx", "image_base64_prefix": base64.b64encode(qr.content).decode("ascii")[:60]}

    def check_login_status(self, identifier: str, login_type: str) -> Any:
        if login_type == "qq":
            response = self.session.get(
                "https://ssl.ptlogin2.qq.com/ptqrlogin",
                params={
                    "u1": "https://y.qq.com/",
                    "ptqrtoken": str(hash33(identifier)),
                    "ptredirect": "0",
                    "h": "1",
                    "t": "1",
                    "g": "1",
                    "from_ui": "1",
                    "ptlang": "2052",
                    "action": f"0-0-{int(time.time() * 1000)}",
                    "js_ver": "20102616",
                    "js_type": "1",
                    "login_sig": "",
                    "pt_uistyle": "40",
                    "aid": "716027609",
                    "daid": "383",
                    "pt_3rd_aid": "100497308",
                },
                headers=headers({"Cookie": f"qrsig={identifier};", "Referer": "https://xui.ptlogin2.qq.com/"}),
                timeout=30,
            )
            return {"status_code": response.status_code, "raw": response.text}
        response = self.session.get(
            "https://lp.open.weixin.qq.com/connect/l/qrconnect",
            params={"uuid": identifier, "_": str(int(time.time() * 1000))},
            headers=headers({"Referer": "https://open.weixin.qq.com/"}),
            timeout=35,
        )
        return {"status_code": response.status_code, "raw": response.text}

    def euin(self, musicid: str) -> Any:
        response = self.session.get(
            "https://c6.y.qq.com/rsc/fcgi-bin/fcg_get_profile_homepage.fcg",
            params={"ct": 20, "cv": 4747474, "cid": 205360838, "userid": musicid},
            headers=headers(),
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def user_info(self) -> Any:
        return post_musicu(
            {
                "music.UserInfo.userInfoServer": {
                    "method": "GetLoginUserInfo",
                    "module": "music.UserInfo.userInfoServer",
                    "param": {},
                }
            },
            self.require_credential(),
        )

    def my_favorite(self, page: int = 1, num: int = 30) -> Any:
        credential = self.require_credential()
        euin_data = self.euin(credential["musicid"])
        enc_uin = euin_data.get("data", {}).get("creator", {}).get("encrypt_uin", "")
        return post_musicu(
            {
                "music.srfDissInfo.DissInfo": {
                    "method": "CgiGetDiss",
                    "module": "music.srfDissInfo.DissInfo",
                    "param": {
                        "disstid": 0,
                        "dirid": 201,
                        "tag": True,
                        "song_begin": (page - 1) * num,
                        "song_num": num,
                        "userinfo": True,
                        "orderlist": True,
                        "enc_host_uin": enc_uin,
                    },
                }
            },
            credential,
        )

    def my_playlists(self) -> Any:
        credential = self.require_credential()
        return post_musicu(
            {
                "music.musicasset.PlaylistBaseRead": {
                    "method": "GetPlaylistByUin",
                    "module": "music.musicasset.PlaylistBaseRead",
                    "param": {"uin": credential["musicid"]},
                }
            },
            credential,
        )

    def playlist_write_payload(self, method: str, dirid: int, song_ids: list[int]) -> dict[str, Any]:
        return {
            "music.musicasset.PlaylistDetailWrite": {
                "method": method,
                "module": "music.musicasset.PlaylistDetailWrite",
                "param": {
                    "dirId": dirid,
                    "v_songInfo": [{"songType": 0, "songId": song_id} for song_id in song_ids],
                },
            }
        }

    def playlist_write(self, method: str, dirid: int, song_ids: list[int]) -> Any:
        return post_musicu(self.playlist_write_payload(method, dirid, song_ids), self.require_credential())

    def radar_recommend(self) -> Any:
        return post_musicu(
            {
                "music.recommend.TrackRelationServer": {
                    "method": "GetRadarSong",
                    "module": "music.recommend.TrackRelationServer",
                    "param": {"Page": 1, "ReqType": 0, "FavSongs": [], "EntranceSongs": []},
                }
            },
            self.credential,
        )

    def guess_recommend(self) -> Any:
        return post_musicu(
            {
                "music.radioProxy.MbTrackRadioSvr": {
                    "method": "get_radio_track",
                    "module": "music.radioProxy.MbTrackRadioSvr",
                    "param": {
                        "id": 99,
                        "num": 5,
                        "from": 0,
                        "scene": 0,
                        "song_ids": [],
                        "ext": {"bluetooth": ""},
                        "should_count_down": 1,
                    },
                }
            },
            self.credential,
        )

    def singer_info(self, mid: str) -> Any:
        return post_musicu(
            {
                "music.UnifiedHomepage.UnifiedHomepageSrv": {
                    "method": "GetHomepageHeader",
                    "module": "music.UnifiedHomepage.UnifiedHomepageSrv",
                    "param": {"SingerMid": mid},
                }
            },
            self.credential,
        )

    def singer_songs(self, mid: str, page: int = 1, num: int = 20) -> Any:
        return post_musicu(
            {
                "musichall.song_list_server": {
                    "method": "GetSingerSongList",
                    "module": "musichall.song_list_server",
                    "param": {"singerMid": mid, "order": 1, "number": num, "begin": (page - 1) * num},
                }
            },
            self.credential,
        )

    def require_credential(self) -> dict[str, str]:
        if not self.credential:
            raise RuntimeError("Set QQMUSIC_MUSICID and QQMUSIC_MUSICKEY first")
        return self.credential


def require_execute(args: argparse.Namespace, preview: Any) -> bool:
    if args.execute:
        return True
    print("Dry-run only. Add --execute to send this mutating request.")
    print_json(preview)
    return False


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Test QQMusic APIs")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("all")

    p = sub.add_parser("search-songs")
    p.add_argument("--keyword", default="周杰伦")
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--num", type=int, default=20)

    p = sub.add_parser("search-singers")
    p.add_argument("--keyword", default="周杰伦")

    p = sub.add_parser("song-url")
    p.add_argument("--mid", default=DEFAULT_SONG_MID)
    p.add_argument("--quality", type=int, default=128)

    for name in ["song-detail", "lyric"]:
        p = sub.add_parser(name)
        p.add_argument("--mid", default=DEFAULT_SONG_MID)

    p = sub.add_parser("recommend-playlists")
    p.add_argument("--num", type=int, default=10)

    p = sub.add_parser("playlist-detail")
    p.add_argument("--dissid", type=int, required=True)
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--num", type=int, default=30)

    sub.add_parser("rank-lists")
    p = sub.add_parser("rank-detail")
    p.add_argument("--top-id", type=int, default=DEFAULT_TOP_ID)
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--num", type=int, default=30)

    sub.add_parser("qq-login-qr")
    sub.add_parser("wx-login-qr")
    p = sub.add_parser("check-login")
    p.add_argument("--identifier", required=True)
    p.add_argument("--type", choices=["qq", "wx"], required=True)

    p = sub.add_parser("euin")
    p.add_argument("--musicid", default=os.getenv("QQMUSIC_MUSICID", ""))

    sub.add_parser("user-info")
    p = sub.add_parser("my-favorite")
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--num", type=int, default=30)
    sub.add_parser("my-playlists")

    for name, method in [("add-songs", "AddSonglist"), ("remove-songs", "DelSonglist")]:
        p = sub.add_parser(name)
        p.add_argument("--dirid", type=int, required=True)
        p.add_argument("--song-id", type=int, action="append", required=True)
        p.add_argument("--execute", action="store_true")

    sub.add_parser("radar-recommend")
    sub.add_parser("guess-recommend")
    p = sub.add_parser("singer-info")
    p.add_argument("--mid", default=DEFAULT_SINGER_MID)
    p = sub.add_parser("singer-songs")
    p.add_argument("--mid", default=DEFAULT_SINGER_MID)
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--num", type=int, default=20)
    return parser


def run_all(client: QQMusicClient) -> list[dict[str, Any]]:
    recommended_playlist_id: int | None = None
    qq_qr_identifier: str | None = None

    def get_recommend_and_capture() -> Any:
        nonlocal recommended_playlist_id
        data = client.recommend_playlists(3)
        items = data.get("music.playlist.PlaylistSquare.GetRecommendFeed", {}).get("data", {}).get("List", [])
        for item in items:
            tid = item.get("Playlist", {}).get("basic", {}).get("tid")
            if tid:
                recommended_playlist_id = int(tid)
                break
        return data

    def get_qq_qr_and_capture() -> Any:
        nonlocal qq_qr_identifier
        data = client.qq_login_qr()
        qq_qr_identifier = data.get("identifier")
        return data

    results = [
        summarize("search_songs", lambda: client.search_songs("周杰伦", 1, 3)),
        summarize("search_singers", lambda: client.search_singers("周杰伦")),
        summarize("song_detail", lambda: client.song_detail(DEFAULT_SONG_MID)),
        summarize("lyric", lambda: client.lyric(DEFAULT_SONG_MID)),
        summarize("song_url", lambda: client.song_url(DEFAULT_SONG_MID, 128)),
        summarize("recommend_playlists", get_recommend_and_capture),
        summarize(
            "playlist_detail",
            lambda: client.playlist_detail(recommended_playlist_id, 1, 3)
            if recommended_playlist_id
            else {"skipped": "no recommended playlist id"},
        ),
        summarize("rank_lists", client.rank_lists),
        summarize("rank_detail", lambda: client.rank_detail(DEFAULT_TOP_ID, 1, 5)),
        summarize("qq_login_qr", get_qq_qr_and_capture),
        summarize(
            "check_login_status_qq",
            lambda: client.check_login_status(qq_qr_identifier, "qq")
            if qq_qr_identifier
            else {"skipped": "no qq qrsig"},
        ),
        summarize("wx_login_qr", client.wx_login_qr),
        summarize("radar_recommend", client.radar_recommend),
        summarize("guess_recommend", client.guess_recommend),
        summarize("singer_info", lambda: client.singer_info(DEFAULT_SINGER_MID)),
        summarize("singer_songs", lambda: client.singer_songs(DEFAULT_SINGER_MID, 1, 5)),
        {
            "api": "add_songs_to_playlist",
            "ok": None,
            "dry_run": client.playlist_write_payload("AddSonglist", 201, [97773]),
        },
        {
            "api": "remove_songs_from_playlist",
            "ok": None,
            "dry_run": client.playlist_write_payload("DelSonglist", 201, [97773]),
        },
    ]
    if client.credential:
        results.extend(
            [
                summarize("euin", lambda: client.euin(client.credential["musicid"])),
                summarize("user_info", client.user_info),
                summarize("my_favorite", lambda: client.my_favorite(1, 5)),
                summarize("my_playlists", client.my_playlists),
            ]
        )
    else:
        results.extend(
            [
                {"api": "euin", "ok": None, "skipped": "missing QQMUSIC_MUSICID"},
                {"api": "user_info", "ok": None, "skipped": "missing credential"},
                {"api": "my_favorite", "ok": None, "skipped": "missing credential"},
                {"api": "my_playlists", "ok": None, "skipped": "missing credential"},
            ]
        )
    return results


def main() -> int:
    args = build_parser().parse_args()
    client = QQMusicClient()
    cmd = args.command

    if cmd == "all":
        print_json(run_all(client))
    elif cmd == "search-songs":
        print_json(client.search_songs(args.keyword, args.page, args.num))
    elif cmd == "search-singers":
        print_json(client.search_singers(args.keyword))
    elif cmd == "song-url":
        print_json(client.song_url(args.mid, args.quality))
    elif cmd == "song-detail":
        print_json(client.song_detail(args.mid))
    elif cmd == "lyric":
        print_json(client.lyric(args.mid))
    elif cmd == "recommend-playlists":
        print_json(client.recommend_playlists(args.num))
    elif cmd == "playlist-detail":
        print_json(client.playlist_detail(args.dissid, args.page, args.num))
    elif cmd == "rank-lists":
        print_json(client.rank_lists())
    elif cmd == "rank-detail":
        print_json(client.rank_detail(args.top_id, args.page, args.num))
    elif cmd == "qq-login-qr":
        print_json(client.qq_login_qr())
    elif cmd == "wx-login-qr":
        print_json(client.wx_login_qr())
    elif cmd == "check-login":
        print_json(client.check_login_status(args.identifier, args.type))
    elif cmd == "euin":
        if not args.musicid:
            raise SystemExit("Provide --musicid or set QQMUSIC_MUSICID")
        print_json(client.euin(args.musicid))
    elif cmd == "user-info":
        print_json(client.user_info())
    elif cmd == "my-favorite":
        print_json(client.my_favorite(args.page, args.num))
    elif cmd == "my-playlists":
        print_json(client.my_playlists())
    elif cmd == "add-songs":
        payload = client.playlist_write_payload("AddSonglist", args.dirid, args.song_id)
        if require_execute(args, payload):
            print_json(client.playlist_write("AddSonglist", args.dirid, args.song_id))
    elif cmd == "remove-songs":
        payload = client.playlist_write_payload("DelSonglist", args.dirid, args.song_id)
        if require_execute(args, payload):
            print_json(client.playlist_write("DelSonglist", args.dirid, args.song_id))
    elif cmd == "radar-recommend":
        print_json(client.radar_recommend())
    elif cmd == "guess-recommend":
        print_json(client.guess_recommend())
    elif cmd == "singer-info":
        print_json(client.singer_info(args.mid))
    elif cmd == "singer-songs":
        print_json(client.singer_songs(args.mid, args.page, args.num))
    return 0


if __name__ == "__main__":
    sys.exit(main())
