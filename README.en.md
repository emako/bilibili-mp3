# <img src="src/favicon.png" width = "50" height = "48" alt="" align="left" /> bilibili-mp3

## Intro
A tools for downloading bilibili songs as mp3.

> With the outbreak of the virtual avatar of bilibili, excellent cover songs appear frequently.
> This tool is specially made to quickly capture for MP3 collection.

随着b站的虚拟主播大爆发，优秀翻唱作品频出，特别制作此工具快速抓取为mp3收藏

| Url Prefix                     | Supports |
| ------------------------------ | -------- |
| https://www.bilibili.com/audio | ×        |
| https://www.bilibili.com/video | √        |

## Cookies supports

Now `cookies.txt` is supported, got from `cookiestxt.crx`.

If you want 4K resolutions, the `cookies.txt` file should be added to the same path.

## Usage

> Usage: bilibili-mp3 <url|bvid>

```bash
bilibili-mp3 "https://www.bilibili.com/video/BV1kS4y1T7kK?p=3"
bilibili-mp3 BV1kS4y1T7kK
```

## When Wrongs

When somethings wrongs but not new release here, you should get new version [you-get](https://github.com/soimort/you-get) for updating by yourself.
Or send a new issuse [here](https://github.com/emako/bilibili-mp3/issues).

## Requirements

```bash
pip install -r requirements.txt
```

## Friendly link

[zlrc](https://github.com/emako/zlrc) is a optional app for fast download `lrc` from NeteaseCloud.

Before using zlrc, please edit the corrected mp3tag.

