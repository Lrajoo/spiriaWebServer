
import json
import requests
import os

###POST
ENDPOINT = "http://127.0.0.1:8000/api/userdatas/"
###UPDATE
#ENDPOINT = "http://127.0.0.1:8000/api/userdatas/"+"1"+"/update/"
###DELETE
#ENDPOINT = "http://127.0.0.1:8000/api/userdatas/"+"1"+"/delete/"
###DETAIL
#ENDPOINT = "http://127.0.0.1:8000/api/userdatas/1"

image_path = '/Users/lingessrajoo/Desktop/spiriaWebServer/media/images/sp1-P1.jpg'

def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if image_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'spiral': image
            }
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    return r

#post put delete
do_img(method='put', data={'userid':1,'age':444, 'spiral': '', 'tremor': 4, 'questionnaire': 66, 'prediction': 'True', 'date': '2019-4-21 00:00:00'}, is_json=False, img_path=image_path)