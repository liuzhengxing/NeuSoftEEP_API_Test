# _*_coding: utf-8 _*_

import requests
import json

from public import params

BaseUrl = params.BaseUrl

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def get_workCenter():
    """工作中心"""
    url = BaseUrl + ''

