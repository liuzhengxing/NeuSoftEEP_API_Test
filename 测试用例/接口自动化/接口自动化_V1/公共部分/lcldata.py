# _*_coding: utf-8_*_

import time
import json

from public import params
from public.excel import excel_readline


ParaDir = params.ParaFile


def lcl_data(sheet, row):
    time.sleep(1)
    fields = excel_readline(ParaDir, sheet, 1)
    args = excel_readline(ParaDir, sheet, row)
    sends = {}
    for i, field in enumerate(fields[:-1]):
        sends[fields[i+1]] = args[i+1]
    dd = json.dumps(sends)
    dl = json.loads(dd)
    # print(dl)
    return dl
