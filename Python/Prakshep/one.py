import requests
import json
import base64

with open("1.jpeg", "rb") as imageFile:
    str1 = base64.b64encode(imageFile.read())
    str2 = str1.decode("utf-8")
data1 = {
    "requests": [
        {
            "image": {
                "content": str2
            },
            "features": [
                {
                    "type": "TEXT_DETECTION"
                }
            ]
        }
    ]
}

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
r = requests.post('https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBcFS2uhY_sGEeyHsJmxcr-u8bvMWwl9N0', json=data1, headers=headers)
response = r.json()

aa = response['responses'][0]['textAnnotations']
for i in aa:
    desc = i.get("description","")
    print(desc)