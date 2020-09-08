# All rights for this file belong to George Imedashvili <george.lifeslice@gmail.com>. Do NOT edit these comments
# You can copy this file, modify it (but don't edit these comments) and use in your own project for free

from . import DicAcademicBase, WordResult


class Dic(DicAcademicBase):
    def __init__(self, dic: str):
        super().__init__()
        self.dic = dic

    def get_word_results(self, q: str, limit=20):
        results = self.request(dic=self.dic, q=q, limit=limit)
        return [WordResult(result) for result in results]
