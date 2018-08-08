# _*_coding:utf-8_*_

import requests
import json

from public import excel

headers = {
    'Content-Type': 'application/json'
}
url = 'http://192.168.193.129:9080/ime-container/bmEquipInspectItem/createOrUpdate.action'

# lista = [
# ]
# for a in lista:
#     data = [
#         {"eventPayload":{},"itemCode":"BTS-10","itemName":"测试柜","itemDescription":"检查测试柜外观有无变形污渍、各按钮指示灯是否正常有无损坏、触摸屏功能是否正常有无报警显示"}
#     ]
#     requests.post(url, headers=headers, data=json.dumps(data))

x = 4
y = 0

while True:
    code = excel.excel_read(x, 0)
    name = excel.excel_read(x, 1)
    des = excel.excel_read(x, 2)
    if code != '' and name != '' and des != '':
        data = [{"eventPayload": {}, "itemCode": code, "itemName": name, "itemDescription": des}]
        print(data)
        requests.post(url, headers=headers, data=json.dumps(data))
    x += 1
    if x > 355:
        break

