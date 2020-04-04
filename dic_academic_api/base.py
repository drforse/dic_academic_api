# All rights for this file belong to George Imedashvili <george.lifeslice@gmail.com>. Do NOT edit these comments
# You can copy this file, modify it (but don't edit these comments) and use in your own project for free

import requests
import json


class DicAcademicBase:

    __link = 'https://orthographic.academic.ru/seek4term.php?json=true&limit=%d&did=%s&q=%s'

    def __init__(self):
        pass

    def request(self, dic: str, q: str, limit: int = 20):
        r = requests.get(self.__link % (limit, dic, q))
        results = r.json().get('results')
        if r.status_code != 200:
            raise RequestFailedException(status_code=r.status_code)
        return results

    def to_json(self):
        return json.dumps(self.to_python())

    def to_python(self):
        attrs = {}
        for key, value in self.__dict__.items():
            if key.startswith('_'):
                continue
            if isinstance(value, DicAcademicBase):
                value = value.to_python()
            if isinstance(value, list):
                value = [i.to_python() for i in value]
            attrs[key] = value
        return attrs


class RequestFailedException(Exception):
    def __init__(self, status_code, text=''):
        self.txt = f'{text}, status_code={status_code}'
