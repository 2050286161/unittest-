import json

from jsonpath_ng import parse

from RedisTest import RedisAgent


class CreatData:

    # 单一新增多条数据
    def SCreatJson(self, CreateTest):

        if CreateTest is None:
            return
        with open('./AnJson/Write.json', 'r', encoding='utf8') as fp:
            JsonData = json.load(fp)
        CreateTest = CreateTest.strip(',')
        CreateTest = CreateTest.split(',')
        for datas in CreateTest:
            path,data= datas.split(':')
            data = data.replace('/', ":")
            data=data.replace("+",",")
            parser = parse(path)  # 语法
            matches = parser.find_or_create(JsonData)
            for match in matches:
                # 更新原始输入的JSON数据
                match.full_path.update_or_create(JsonData, data)

        fp.close()
        return JsonData

    def CreateEmail(self, EmailCount):
        if EmailCount is None:
            return -1
        emailcoun = []
        if EmailCount.isdigit():
            EmailCount = int(EmailCount)
            for index in range(EmailCount):
                emailcoun.append('...' + str(index) + '...')
        else:
            EmailCount = EmailCount.split(',')
            for email in EmailCount:
                emailcoun.append(email)
        return emailcoun

    def CreateDa(self, CreateTest=None, EmailCount=0):
        emailCount = self.CreateEmail(EmailCount)
        if emailCount is None or emailCount == -1:
            return False
        if CreateTest is not None:
            CreateT = CreateTest.split('|')
        value = []
        if CreateTest is None:
            for email in emailCount:
                CreateT = 'email:' + email
                data = self.SCreatJson(CreateTest=CreateT)
                value.append(data)
                RedisAgent().set(email, str(json.dumps(data)))
        else:
            i=0
            for email in emailCount:
                Create = 'email:' + email + ',' + CreateT[i]
                i+=1
                data = self.SCreatJson(CreateTest=Create)
                value.append(data)

                RedisAgent().set(email, str(json.dumps(data)))
        return value

    def deleterious(self, EmailCount):
        if EmailCount.isdigit():
            EmailCount = int(EmailCount)
            for email in range(EmailCount):
                RedisAgent().delete('...' + str(email) + '...')
        else:
            for email in EmailCount:
                RedisAgent().delete(email)


if __name__ == '__main__':
    test = CreatData()
    print(test.CreateDa(EmailCount='2'))