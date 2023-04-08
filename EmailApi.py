import unittest
from ddt import ddt, unpack, file_data, data
import datetime
from do_method import ReUilt
from excel_read import HandleExcel
from Compare import Compare_
from CreateTestData import CreatData


@ddt
class EmailAPI(unittest.TestCase):
    scase = HandleExcel('email.xlsx', 'Sheet1').read_data()


    def setUp(self):
        self.re = ReUilt(Url='...', ApiKey='...')


    @data(*scase)
    def test_sin(self, case):
        if case['CaseName'] is None:
            return
        value = CreatData().CreateDa(CreateTest=case['CreateTest'], EmailCount=str(case['EmailCount']))
        data_json = self.re.do_go(param=str(case['email']), mode=case['mode'])
        if value:
            CreatData().deleterious(EmailCount=str(case['EmailCount']))
        result = Compare_.SinCompare(Data=data_json, JsPath=case['jspath'])
        if case['AnResult'] is None:
            case['AnResult'] = ''
        self.assertEqual(str(case['AnResult']), str(result),
                         msg='预期结果字段为：{0}==返回结果字段为：{1}\n传输参数为:email={2},mode={3}\n构建的数据为：{4},\n返回所有数据为:{5}'.format(
                             case['AnResult'], result, str(case['email']), str(case['mode']), value, data_json))
        print('预期结果字段为：{0}==返回结果字段为：{1}\n传输参数为:email={2},mode={3}\n构建的数据为：{4},\n返回所有数据为:{5}'.format(
                             case['AnResult'], result, str(case['email']), str(case['mode']), value, data_json))


    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main

