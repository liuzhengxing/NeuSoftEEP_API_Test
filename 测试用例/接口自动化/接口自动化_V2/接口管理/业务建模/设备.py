# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class Equipments:
    """
    设备类
    """

    def equipment_create(self, data):
        """
        设备创建接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/bmEquipment/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req