# encoding:utf-8

import requests
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=BhgoOojWQj14BCuEfGiDkt0g&client_secret=Rb8TZMSW23DvH2sU0tmBUPjE5ToKHYvx'
response = requests.get(host)
if response:
    access_token = response.json()['access_token']
    print(access_token)
    '''
    相似图检索—检索
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/search"
    # 二进制方式打开图片文件
    f = open('./test2.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img, "pn": 0, "rn": 5}
    # access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())

