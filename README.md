中文 | [English](README.en.md)

# <img src="src/favicon.png" width = "50" height = "48" alt="" align="left" /> bilibili-mp3

## 简介
B站歌曲MP3下载工具。

> 随着b站的虚拟主播大爆发，优秀翻唱作品频出。
> 特别制作此工具快速抓取为mp3收藏。

| 前缀                           | 支持 |
| ------------------------------ | ---- |
| https://www.bilibili.com/audio | ×    |
| https://www.bilibili.com/video | √    |

## 下载
[![GitHub downloads](https://img.shields.io/github/downloads/emako/bilibili-mp3/total)](https://github.com/emako/bilibili-mp3/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/emako/bilibili-mp3/latest/total)](https://github.com/emako/bilibili-mp3/releases)

[下载页](https://github.com/emako/bilibili-mp3/releases)


## Cookies支持

支持`cookies.txt`，该文件可从谷歌浏览器`cookiestxt.crx`插件获取。

如果想要4K分辨率对应音轨，就把`cookies.txt`文件放到一个目录下。

## 用法

> bilibili-mp3 <url|bvid>

```bash
bilibili-mp3 "https://www.bilibili.com/video/BV1kS4y1T7kK?p=3"
bilibili-mp3 BV1kS4y1T7kK
```

## 问题反馈

当有错误但没有新版本时，可以尝试更新[you-get](https://github.com/soimort/you-get)的版本。
或者从[这里](https://github.com/emako/bilibili-mp3/issues)新建一个issuse。

## 所需项目

```bash
pip install -r requirements.txt
```

其他：

wget.exe、MediaInfo.dll、lame.exe、ffmpeg.exe

## 友情链接

[zlrc](https://github.com/emako/zlrc)是一款自己开发的lrc歌词快速下载工具，它从网易云获得歌词。

在使用zlrc之前，最好确保已正确填好MP3的标签。

