#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urlparse
import re

### M3U8 Tag
TAG_PREFIX = '#EXT'
PLAYLIST_HEADER = '#EXTM3U'
TAG_ENDLIST = '#EXT-X-ENDLIST'
TAG_KEY = '#EXT-X-KEY'
TAG_MEDIA_DURATION = "#EXTINF";
TAG_STREAM_INF = '#EXT-X-STREAM-INF'
TAG_DISCONTINUITY = '#EXT-X-DISCONTINUITY'

### M3U8 Pattern Tag
REGEX_MEDIA_DURATION = TAG_MEDIA_DURATION + ':([\\d\\.]+)\\b'

URL='http://video.yjf138.com:8091/20180812/6yl0Q2YZ/index.m3u8'

### 返回m3u8文件,不是最终的
def parse_m3u8_info(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    result = ''
    request = requests.get(url, timeout=20)
    for line in request.iter_lines():
        result += line + '\n'
    return result

### 返回最终的m3u8文件
def parse_final_m3u8_info(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    result = ''
    hasStreamInf = False
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            result += line + '\n'
            if (line.startswith(TAG_STREAM_INF)):
                hasStreamInf = True
            continue
        if (hasStreamInf):
            return parse_final_m3u8_info(get_final_url(url, line))
        hasStreamInf = False
        result += get_final_url(url, line) + '\n'
    return result

### 根据m3u8中的分片写法得到完整的url
def get_final_url(url, line):
    val = urlparse.urlsplit(url)
    hostUrl = url[0:url.index(val.netloc)+len(val.netloc)]
    baseUrl = url[0:url.rindex('/')+1]
    if (line.startswith('/')):
        tempUrl = ''
        if (line[1:].find('/') != -1):
            tempIndex = line[1:].index('/')
            tempUrl = line[0:tempIndex]
            if (url.find(tempUrl) != -1):
                tempIndex = url.index(tempUrl)
                tempUrl = url[0:tempIndex] + line
            else:
                tempUrl = hostUrl + line[1:]
            return tempUrl
        else:
            tempUrl = baseUrl + line[1:]
        return tempUrl
    if (line.startswith('http://') or line.startswith('https://')):
        return line
    return baseUrl + line

### 判断m3u8中是否存在#EXT-X-STREAM-INF
def has_ext_stream(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            if (line.startswith(TAG_STREAM_INF)):
                return True
    return False

### 判断m3u8中是否存在#EXT-X-KEY
def has_ext_key(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    hasStreamInf = False
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            if (line.startswith(TAG_STREAM_INF)):
                hasStreamInf = True
            elif (line.startswith(TAG_KEY)):
                return True
            continue
        if (hasStreamInf):
            return has_ext_key(get_final_url(url, line))
        hasStreamInf = False
    return False

### 判断m3u8中是否存在#EXT-X-DISCONTINUITY
def has_ext_discontinuity(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    hasStreamInf = False
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            if (line.startswith(TAG_STREAM_INF)):
                hasStreamInf = True
            elif (line.startswith(TAG_DISCONTINUITY)):
                return True
            continue
        if (hasStreamInf):
            return has_ext_key(get_final_url(url, line))
        hasStreamInf = False
    return False

### 获取M3U8文件的总时长
def get_total_duration(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    result = ''
    hasStreamInf = False
    totalDuration = 0
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            if (line.startswith(TAG_STREAM_INF)):
                hasStreamInf = True
            elif (line.startswith(TAG_MEDIA_DURATION)):
                ret = parse_pattern_str(REGEX_MEDIA_DURATION, line)
                totalDuration += float(ret)
            continue
        if (hasStreamInf):
            return get_total_duration(get_final_url(url, line))
        hasStreamInf = False
    return totalDuration

def parse_pattern_str(pattern_str, str):
    matchObj = re.match(pattern_str, str)
    if (matchObj) :
        return matchObj.group(1)
    return ''

# m3u8下载的脚本
URL = 'http://video.yjf138.com:8091/20180812/6yl0Q2YZ/1500kb/hls/bm02h76314876.ts'
request = requests.get(URL, timeout=20)
with open('test.ts', 'wb') as output:
    output.write(request.content)

result = parse_m3u8_info(URL)
print('M3U8文件内容如下:\n' + result)

finalResult = parse_final_m3u8_info(URL)
print('M3U8文件最终内容如下:\n' + finalResult)

hasExtStream = has_ext_stream(URL)
print('是否存在多路流: ---> ' + str(hasExtStream))

hasExtKey = has_ext_key(URL)
print('是否存在key: ---> ' + str(hasExtKey))

hasDisContinuity = has_ext_discontinuity(URL)
print('是否存在不连续的 : ---> ' + str(hasDisContinuity))

totalDuration = get_total_duration(URL)
print('此M3U8文件的总时间: --->' + str(totalDuration))


