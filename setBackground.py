# -*- coding: utf-8 -*-


import pygame


White = [255, 255, 255]
Black = [0, 0, 0]
Red = [227, 23, 13]
Green = [48, 128, 20]
Blue = [61, 89, 171]
Gold = [255, 215, 0]


def gameBackground_Normal(screen):
    bg = pygame.image.load('images//background1.jpg')#圖片引進去
    bg1 = pygame.transform.scale(bg, (450, 450))#圖片尺寸改為450*450cm
    screen.blit(bg1, (0, 0))#圖片背景弄上去
    pygame.draw.rect(screen, Black, (0, 400, 450, 300))#畫布矩形(x,y,寬,高)

def gameBackground_Boss(screen):
    bg= pygame.image.load('images//background2.jpg')
    bg1 = pygame.transform.scale(bg,(450,450))
    screen.blit(bg1,(0,0))
    pygame.draw.rect(screen,[0,0,0],(0,400,450,300))

def beginBackgroung(screen): #開始畫面
    title = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 75)#設定字形及大小
    title_show = title.render("鬥智地下城", True, (255, 250, 240))#題目設定
    bg = pygame.image.load('images//background3.jpg')
    screen.blit(bg, (0, 0))
    screen.blit(title_show, (40, 175))


def Filter(screen):  # 濾鏡用#背景
    source = pygame.transform.scale(pygame.image.load("images//filter.png").convert_alpha(), (450, 720))
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(screen, (0, 0))
    temp.blit(source, (0, 0))
    temp.set_alpha(200)
    screen.blit(temp, (0, 0))


def Success(screen):
    font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 50)
    font_show = font.render("Congratulations!", True, White)#True式改變平滑值使之看起來比較好看
    screen.blit(font_show, (30, 210))
    font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 20)
    font_show = font.render("Continue?", True, White)
    screen.blit(font_show, (175, 400))


def Fail(screen):
    font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 60)
    font_show = font.render("You Fail!", True, White)
    screen.blit(font_show, (100, 210))


class Button():#開始遊戲回到主畫面成功跟失敗選項
    def __init__(self, num, text, screen):
        self.num = num
        self.text = text
        self.screen = screen
        self.pos_x = [125, 125 + 200]
        self.pos_y = [450 + 80 * self.num, 450 + 80 * self.num + 60]

    def show(self, rectColor, textColor):
        pygame.draw.rect(self.screen, rectColor, (self.pos_x[0], self.pos_y[0], 200, 60))
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 30)
        font_show = font.render(self.text, True, textColor)
        (self.screen).blit(font_show, (self.pos_x[0] + 15, self.pos_y[0] + 15))

    def on_Button(self, x, y):#滑鼠游標在範圍內顏色會變白
        if (self.pos_x[0] <= x and x <= self.pos_x[1]) and (self.pos_y[0] <= y and y <= self.pos_y[1]):
            self.show(White, Black)
            return True
        else:
            self.show(Blue, White)
            return False

    def Click(self, x, y):
        self.show(Green, White)