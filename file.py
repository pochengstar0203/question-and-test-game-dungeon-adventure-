# -*- coding: utf-8 -*-
"""
Created on Mon May 22 03:37:30 2023

@author: user
"""

import random

class random_Question:
    def __init__(self,note):
        file_in = open("Question_and_Answer.txt","r",encoding="utf-8")
        if note == 1:
            n = 2
        elif note == 2:
            n = 99
        elif note == 3:
            n = 68
        elif note == 4:
            n = 51
        elif note == 5:
            n = 52
        elif note == 6:
            n = 47
        elif note == 7:
            n = 101
        elif note == 8:
            n = 129
        elif note == 9:
            n = 110
        elif note == 10:
            n = 134
        elif note == 11:
            n = 133
        else:
            n = random.randint(1,134)#題庫有134題
        for i in range(1,n):
            file_in.readline()#隨機跳幾行後開始出題
        Q_and_A = file_in.readline().replace("\n","").split(" ")#題目格式存入QAlist
        self.question = Q_and_A[0]
        del Q_and_A[0]
        self.answer = [[Q_and_A[0],True],[Q_and_A[1],False],
                       [Q_and_A[2],False],[Q_and_A[3],False]]
        random.shuffle(self.answer)
    def getQuestion(self):
        return self.question
    def getAnswer(self):
        return self.answer