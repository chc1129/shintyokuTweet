#!/usr/bin/env python
#coding: utf-8

import json
from requests_oauthlib import OAuth1Session

CK = ''
CS = ''
AT = ''
AS = ''

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text ="https://api.twitter.com/1.1/statuses/update.json"

twitter = OAuth1Session(CK, CS, AT, AS)

files = {"media": open("img.png", 'rb')}
req_media = twitter.post(url_media, files = files)

if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

params = {'status': '進捗ダメです', "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")

