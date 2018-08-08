# _*_ coding: utf-8 _*_

import requests
import json

from public import params
from public import excel


class BaseModeData():
    def __init__(self):
        self.baseurl = 'http://' + params.testdomain + ':' + params.testport
        self.headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }

    def create_basemodedata(self):
        # 1创建业务组
        url = self.baseurl + '/ime-container/busiGroup/add.action'
        data = {"busiGroupCode": "autotest", "busiGroupName": "自动化", "active": "true"}
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        groupGid = json.loads(req)['data']
        value = ['groupGid', groupGid]
        for v in range(2):
            excel.excel_write(1, v, value[v])

        # 2创建业务单元
        url = self.baseurl + '/ime-container/busiUnit/add.action'
        data = {
            "descr": "自动化测试",
            "mobile": "18888888888",
            "active": "true",
            "abbreviate": "接口",
            "active1": "true",
            "active2": "true",
            "active3": "true",
            "active4": "true",
            "active5": "true",
            "active6": "true",
            "active7": "true",
            "active8": "true",
            "active9": "true",
            "busiUnitName": "接口自动化_V1",
            "busiUnitCode": "autotest",
            "funcGid": [
                "6392A29965804A03E055000000000001",
                "6392A29965814A03E055000000000001",
                "6392A29965824A03E055000000000001",
                "6392A29965834A03E055000000000001",
                "6392A29965844A03E055000000000001",
                "6392A29965854A03E055000000000001",
                "6392A29965864A03E055000000000001",
                "6392A29965874A03E055000000000001",
                "6392A29965884A03E055000000000001"
            ],
            "busiUnitFunRelationList": [
                {"funGid": "6392A29965804A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965814A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965824A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965834A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965844A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965854A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965864A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965874A03E055000000000001", "active": "true"},
                {"funGid": "6392A29965884A03E055000000000001", "active": "true"}
            ],
            "groupGid": groupGid
        }
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        BusiUnitGid = json.loads(req)['data']
        value = ['BusiUnitGid', BusiUnitGid]
        for v in range(2):
            excel.excel_write(2, v, value[v])

        # 3创建部门
        url = self.baseurl + '/ime-container/department/add.action'
        data = {
            "smBusiUnitGid": BusiUnitGid,
            "smBusiUnitGidRef": {"busiUnitName": "接口自动化_V1"},
            "busiUnit": BusiUnitGid,
            "smBusiGroupGid": "",
            "code": "autotest",
            "name": "自动化测试"
        }
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        DepartmentGid = json.loads(req)['data']
        value = ['DepartmentGid', DepartmentGid]
        for v in range(2):
            excel.excel_write(3, v, value[v])

        # 4创建人员分类
        url = self.baseurl + '/ime-container/personnelType/add.action'
        data = {
            "personnelTypeCode": "autotest",
            "personnelTypeName": "接口自动化_V1"}
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        PersonnelTypeGid = json.loads(req)['data']
        value = ['PersonnelTypeGid', PersonnelTypeGid]
        for v in range(2):
            excel.excel_write(4, v, value[v])

        # 5创建人员
        url = self.baseurl + '/ime-container/personnel/add.action'
        data = {
            "smDepartmentGidRef": {"name": "自动化测试"},
            "smDepartmentGid": DepartmentGid,
            "personnelCode": "autotester",
            "personnelName": "接口自动化测试人员",
            "smPersonnelTypeGid": PersonnelTypeGid,
            "smBusiUnitGid": BusiUnitGid
        }
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        PersonnelGid = json.loads(req)['data']
        value = ['PersonnelGid', PersonnelGid]
        for v in range(2):
            excel.excel_write(5, v, value[v])

        # 6创建设备分类
        url = self.baseurl + '/ime-container/bmEquipmentType/createOrUpdate.action'
        data = {"code": "autotest", "name": "接口自动化设备"}
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        EquipmentTypeGid = json.loads(req)['data']
        value = ['EquipmentTypeGid', EquipmentTypeGid]
        for v in range(2):
            excel.excel_write(6, v, value[v])

        # 7创建计量单位
        url = self.baseurl + '/ime-container/bmMeasurementUnit/createOrUpdate.action'
        data = [{
            "type": "other",
            "code": "autotest",
            "name": "轮次",
            "englishName": "time",
            "conversionFactor": "1",
            "decimalDigit": "1"
        }]
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        MeasurementUnitGid = json.loads(req)['data']
        value = ['MeasurementUnitGid', MeasurementUnitGid]
        for v in range(2):
            excel.excel_write(7, v, value[v])

        # 8创建设备1
        url = self.baseurl + '/ime-container/bmEquipment/add.action'
        data = {
            "bmEquipmentTypeGid": EquipmentTypeGid,
            "bmMeasurementUnitGidRef": {"name": "轮次", "code": "autotest"},
            "model": "autotest",
            "name": "设备1",
            "code": "autotest1",
            "bmMeasurementUnitGid": MeasurementUnitGid,
            "mdEquipmentTypeGid": EquipmentTypeGid,
            "status": "intact",
            "mdEquipmentTypeGidRef.name": "接口自动化设备"
        }
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        EquipmentGid = json.loads(req)['data']
        value = ['EquipmentGid', EquipmentGid]
        for v in range(2):
            excel.excel_write(8, v, value[v])

        # 9创建设备检查项目
        url = self.baseurl + '/ime-container/bmEquipInspectItem/createOrUpdate.action'
        data = [
            {"eventPayload": {}, "itemCode": "autotest1", "itemName": "round1"}
        ]
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        EquipInspectItemGid = json.loads(req)['data']
        value = ['EquipInspectItemGid', EquipInspectItemGid]
        for v in range(2):
            excel.excel_write(9, v, value[v])

        # 10创建设备检查部位
        url = self.baseurl + '/ime-container/bmEquipInspectPart/createOrUpdate.action'
        data = [
            {"eventPayload": {}, "partCode": "autotest", "partName": "line1"}
        ]
        req = requests.post(url, headers=self.headers, data=json.dumps(data)).content.decode()
        EquipInspectPartGid = json.loads(req)['data']
        value = ['EquipInspectPartGid', EquipInspectPartGid]
        for v in range(2):
            excel.excel_write(10, v, value[v])


if __name__ == '__main__':
    bmd = BaseModeData()
    print(bmd.create_basemodedata())
