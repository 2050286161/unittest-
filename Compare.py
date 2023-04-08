#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import jsonpath
from deepdiff import DeepDiff


class Compare_:
    # 上面2个是增量方法比对
    @staticmethod
    def SinCompare(Data, JsPath):
        try:
            AnResult = list(JsPath.split('/'))
            for data in AnResult:
                if data.isdigit():
                    data = int(data)
                Data = Data[data]
            return Data
        except Exception as e:
            return e


    @staticmethod
    def MitCompare(Data, JsPath):
        try:
            # 这地方直接改成excel数据会好点
            Data = jsonpath.jsonpath(Data, '$' + JsPath)
            if Data is False:
                Data = ['参数比对失败，没有找到路径，测试不通过，或没有路径']
            if str(Data[0]).isdigit():
                Data = [str(Data[0])]
            return Data
        except Exception as e:
            return e

    #     全量比对方法
    @staticmethod
    def AllCompare(Data, AnResult):
        try:
            AnResults = json.loads(AnResult)
            return DeepDiff(Data, AnResults)
        except Exception as e:
            return e

    @staticmethod
    def Format(Data, AnResult):
        Datas = json.loads(Data)
        AnResults = json.loads(AnResult)
        return json.dumps(Datas, ensure_ascii=False, indent=2), json.dumps(AnResults, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    test = Compare_()
    key = test.MitCompare(input(), input())
    print("返回数据：{}\n".format(key))
