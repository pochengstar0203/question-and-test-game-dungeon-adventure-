# -*- coding: utf-8 -*-

import pygame

White = [255, 255, 255]
Black = [0, 0, 0]
Red = [227, 23, 13]
Green = [48, 128, 20]
Blue = [61, 89, 171]
Gold = [255, 215, 0]

pygame.mixer.init()
correctSound = pygame.mixer.Sound("audio//correct.mp3")
wrongSound = pygame.mixer.Sound("audio//wrong.mp3")


class Option():
    def __init__(self, num, answer, screen):
        self.pos_x = [75, 375]  # x座標
        self.pos_y = [420 + num * 65, 420 + num * 65 + 60]  # y座標
        self.font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 28)
        self.text = answer[0]
        self.correct = answer[1]
        self.screen = screen

    def show(self, rectColor, textColor):  # 顯示選項
        pygame.draw.rect(self.screen, rectColor, (self.pos_x[0], self.pos_y[0], 300, 60))
        self.font_show = (self.font).render(self.text, True, textColor)
        (self.screen).blit(self.font_show, (self.pos_x[0] + 15, self.pos_y[0] + 15))

    def on_Option(self, x, y):
        if (self.pos_x[0] <= x and x <= self.pos_x[1]) and (self.pos_y[0] <= y and y <= self.pos_y[1]):
            self.show(White, Black)  # 矩形填滿白色，文字顏色黑色
            return True
        else:
            self.show(Blue, White)  # 矩形填滿藍色，文字顏色白色
            return False

    def Click(self, x, y):
        if self.correct:  # 正確
            correctSound.play()
            self.show(Green, White)  # 矩形填滿綠色，文字顏色白色
            return True
        else:
            wrongSound.play()
            self.show(Red, White)  # 矩形填滿紅色，文字顏色白色
            return False

    def checkAnswer(self):
        if self.correct:
            self.show(Green, White)  # 矩形填滿綠色，文字顏色白色


class Question():
    def __init__(self, text, screen):
        if len(text) <= 12:
            self.text1 = text
            self.text2 = ""
        else:
            self.text1 = text[0:12]
            self.text2 = text[12:]
        self.screen = screen
        self.time = pygame.time.get_ticks()
        self.show()
        self.countdown()

    def show(self):
        pygame.draw.rect(self.screen, Gold, (0, 260, 450, 150))
        pygame.draw.rect(self.screen, Blue, (5, 265, 440, 140))

        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 30)
        font_show = (font).render(self.text1, True, White)
        (self.screen).blit(font_show, (50, 305))
        font_show = (font).render(self.text2, True, White)
        (self.screen).blit(font_show, (50, 345))

    def countdown(self):
        time = (pygame.time.get_ticks() - self.time) // 1000
        pygame.draw.circle(self.screen, Gold, (25, 260), 38)
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 40)
        font_show = (font).render(str(15 - time), True, White)
        if 15 - time >= 15:
            (self.screen).blit(font_show, (5, 240))
        else:
            (self.screen).blit(font_show, (15, 240))

        return 15 - time


def checkAll(options, x, y):
    Done = False
    Correct = False
    for i in options:
        if i.on_Option(x, y):
            if not i.Click(x, y):
                Correct = False
                for j in options:
                    j.checkAnswer()
            else:
                Correct = True
            pygame.display.update()
            Done = True
            return Done, Correct
    return Done, Correct