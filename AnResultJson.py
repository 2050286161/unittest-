#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class AnJson:
    @staticmethod
    def Anjson():
        result = open("./package-lock.json", "r", encoding="utf-8")
        print(json.load(result))


if __name__ == '__main__':
    AnJson().Anjson()
