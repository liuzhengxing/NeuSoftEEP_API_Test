import json
import requests
import time
import cx_Oracle as oracle

from public import params

BaseUrl = params.BaseUrl


def neu_login():
    headers = {
        "Content-Type": "application/json"
    }

    s = requests.Session()
    loginURL = BaseUrl + '/ime-container/login.action'
    loginheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = 'username=QU1&password=123456'
    loginres = s.post(loginURL, headers=loginheaders, data=data).content.decode()
    token = json.loads(loginres)['data']['token']
    headers['Authorization'] = token

    currentheaders = {
        'Authorization': token
    }
    currentURL = BaseUrl + '/ime-container/user/current.action'
    ree = s.post(currentURL, headers=currentheaders).content.decode()
    smbggid = json.loads(ree)['data']['smBusiGroupGid']

    switchURL = BaseUrl + '/ime-container/busiGroup/switch.action?gid=' + smbggid
    s.post(switchURL, headers=headers, data=data).content.decode()
    return s, token


def neu_reqeust(**kwargs):
    """
    :param kwargs: 请求数据
    :return:
    """
    headers = {
        'Content-Type': 'application/json'
    }
    neu_session, token = neu_login()
    headers['Authorization'] = token
    resp = None
    method = kwargs.pop('method')
    url = BaseUrl + kwargs.pop('url')
    if 'dataSource' in kwargs.keys():
        headers['dataSource'] = kwargs.pop('dataSource')
    if method == 'GET':
        resp = neu_session.get(url, headers=headers).content.decode()
    elif method == 'POST':
        if 'data' in kwargs.keys():
            data = kwargs.pop('data')
            resp = neu_session.post(url, headers=headers, data=json.dumps(data)).content.decode()
        else:
            resp = neu_session.post(url, headers=headers).content.decode()
    try:
        dict_resp = dict(json.loads(resp))

        return dict_resp
    except(ValueError, TypeError):
        return resp
    finally:
        neu_session.close()


def create_code():
    return str(int(time.time() * 1000))


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def exec_oracle(sql):
    username = "ime_v11"
    userpwd = "ime_v11"
    host = "192.168.138.192"
    port = 1521
    dbname = "ora11g"
    dsn = oracle.makedsn(host, port, dbname)
    connection = oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    cursor.execute(sql)
    # result = cursor.fetchall()
    # count = cursor.rowcount
    # print("=====================")
    # print("Total:", count)
    # print("=====================")
    # for row in result:
    #     print(row)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    create_code()
