import requests
import json

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }

url = 'http://192.168.138.132/ime-container/bmMaterielInfo/query.action?usedPost=true'


def getbomgid(code):
    data = {
        "query":
            {"query":
                 [
                     {"operator": "and",
                      "field": "code",
                      "type": "eq",
                      "value": code,
                      "left": "(", "right": ")"
                      }
                 ]
            },
        "pager": {"page": 1, "pageSize": 10}
    }
    req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
    # print(json.loads(req)['data'][0])
    return json.loads(req)['data'][0]['gid']


if __name__ == "__main__":
    getbomgid('per10')
