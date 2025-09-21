# -*- coding: utf-8 -*-

import sys
import pygame
import random
from pygame.locals import QUIT

from file import random_Question
import QuestionSystem
import BattleSystem
import setBackground

pygame.init()
screen = pygame.display.set_mode((450, 720))  # 設置一個450*720的視窗
pygame.display.set_caption("鬥智地下城")  # 視窗標題
screen.fill((0, 0, 0))  # 視窗填滿黑色


def music(n,note):
    pygame.mixer.music.load("audio//"+n + ".mp3")  #
    #pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(note)

pygame.mixer.init()
Done = True
PlayGame = False
Begin = True
Rest = False
Fail = False

# (攻擊力,血量)
player = BattleSystem.Player(80, 1150, screen)

while True:
    pygame.time.Clock().tick(30)
    # 偵測是否要離開
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 開始畫面
    music("begin",-1)
    setBackground.beginBackgroung(screen)
    buttons = setBackground.Button(0, "開始", screen)
    while Begin:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            buttons.on_Button(x, y)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                if buttons.on_Button(x, y):
                    buttons.Click(x, y)
                    PlayGame = True
                    Begin = False
                    pygame.display.update()
                    pygame.time.delay(500)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    # 遊戲本身
    if player.level % 7 == 0:
        music("happycat",-1)
    else:
        music("playgame",-1)
    while PlayGame:
        if player.level % 7 == 0:
            setBackground.gameBackground_Boss(screen)
            enemy = player.boss
        else:
            setBackground.gameBackground_Normal(screen)
            enemy = player.enemys[random.randint(0, 3)]
        enemy.show()
        player.showBlood()
        cnt = 0
        while True:  # 一關的迴圈
            cnt += 1
            total = 0
            bonus = 1
            for j in range(0, player.level // 10 + 3):  # 答題累積傷害
                # 要第幾題出在這
                if player.level == 1 and cnt == 1 and j == 0 :
                    note = 1
                elif player.level == 2 and cnt == 1 and j == 0 :
                    note = 2
                elif player.level == 2 and cnt == 1 and j == 2 :
                    note = 3
                elif player.level == 3 and cnt == 1 and j == 0 :
                    note = 4
                elif player.level == 4 and cnt == 1 and j == 0 :
                    note = 5
                elif player.level == 5 and cnt == 1 and j == 0 :
                    note = 6
                elif player.level == 5 and cnt == 1 and j == 1 :
                    note = 7
                elif player.level == 6 and cnt == 1 and j == 0 :
                    note = 8
                elif player.level == 6 and cnt == 2 and j == 0 :
                    note = 9
                elif player.level == 7 and cnt == 1 and j == 0 :
                    note = 10
                elif player.level == 7 and cnt == 2 and j == 0 :
                    note = 11
                else:
                    note = 0
                player.Bar(screen, cnt, j, total)
                x, y = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if Done:
                    Q_and_A = random_Question(note)
                    options = [QuestionSystem.Option(0, Q_and_A.getAnswer()[0], screen),
                               QuestionSystem.Option(1, Q_and_A.getAnswer()[1], screen),
                               QuestionSystem.Option(2, Q_and_A.getAnswer()[2], screen),
                               QuestionSystem.Option(3, Q_and_A.getAnswer()[3], screen)]
                    question = QuestionSystem.Question(Q_and_A.getQuestion(), screen)
                    pygame.display.update()
                    Done = False
                for i in options:  # 防止滑鼠放在選項上
                    i.on_Option(x, y)
                    pygame.display.update()
                while not Done:
                    question.countdown()
                    if question.countdown() <= 0:
                        for i in options:
                            i.checkAnswer()
                        pygame.display.update()
                        Done = True
                        Correct = False
                        pygame.time.delay(700)
                    x, y = pygame.mouse.get_pos()
                    for i in options:  # 防止滑鼠放在選項上
                        i.on_Option(x, y)
                        pygame.display.update()
                    for event in pygame.event.get():
                        if not Done:
                            if event.type == pygame.MOUSEBUTTONUP:
                                Done, Correct = QuestionSystem.checkAll(options, x, y)
                                pygame.time.delay(700)
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                if Correct:
                    total += int(player.attack * bonus)
                    bonus += 0.15
                    # print(total)
                else:
                    bonus = 1
            enemy.blood -= total
            if enemy.blood <= 0:
                enemy.blood = 0
            enemy.showBlood()
            if enemy.blood <= 0:
                enemy.levelUP()
                player.levelUP()
                PlayGame = False
                Rest = True
                break
            player.blood -= enemy.attack
            if player.blood <= 0:
                player.blood = 0
            player.showBlood()
            pygame.display.update()
            if player.blood <= 0:
                PlayGame = False
                Fail = True
                break

    # 確認是否進行下一關
    setBackground.Filter(screen)
    if Rest:
        music("success",0)
    if Fail:
        music("fail",0)
    while Rest:  # 上一關成功
        setBackground.Success(screen)
        buttons = [setBackground.Button(0, "下一關", screen),
                   setBackground.Button(1, "返回主畫面", screen)]
        x, y = pygame.mouse.get_pos()
        for i in buttons:  # 防止滑鼠放在選項上
            i.on_Button(x, y)
            pygame.display.update()
        for event in pygame.event.get():
            for i in buttons:  # 防止滑鼠放在選項上
                i.on_Button(x, y)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                if buttons[0].on_Button(x, y):
                    buttons[0].Click(x, y)
                    PlayGame = True
                    Rest = False
                    pygame.display.update()
                    pygame.time.delay(500)
                if buttons[1].on_Button(x, y):
                    buttons[1].Click(x, y)
                    Begin = True
                    PlayGame = False
                    Rest = False
                    pygame.display.update()
                    pygame.time.delay(500)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    while Fail:  # 上一關失敗
        # 重設
        player = BattleSystem.Player(80, 1150, screen)
        x, y = pygame.mouse.get_pos()
        setBackground.Fail(screen)
        buttons = setBackground.Button(0, "返回主畫面", screen)
        for event in pygame.event.get():
            buttons.on_Button(x, y)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                if buttons.on_Button(x, y):
                    buttons.Click(x, y)
                    PlayGame = False
                    Fail = False
                    Begin = True
                    pygame.display.update()
                    pygame.time.delay(500)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()