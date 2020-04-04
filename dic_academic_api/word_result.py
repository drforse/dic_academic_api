# All rights for this file belong to George Imedashvili <george.lifeslice@gmail.com>. Do NOT edit these comments
# You can copy this file, modify it (but don't edit these comments) and use in your own project for free

from . import DicAcademicBase


class WordResult(DicAcademicBase):
    def __init__(self, word_dict: dict):
        super().__init__()
        self.id = word_dict.get('id')
        self.value = word_dict.get('value')
        self.info = word_dict.get('info')

    def __str__(self):
        return self.to_json()
