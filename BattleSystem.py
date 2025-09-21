
# -*- coding: utf-8 -*-

import random
import pygame

White = [255, 255, 255]
Black = [0, 0, 0]
colorBlood = [250, 128, 114]
Brown = [139, 69, 19]
Gray = [255, 250, 240]


class Player():
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, num, atk, hp, screen):  # (編號,攻擊力,血量)
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load("images//enemy" + str(num) + ".png"), (175, 175))
            self.rect = self.image.get_rect()
            self.pos = (130, 15)
            self.rect.topleft = self.pos
            self.attack = atk
            self.hp = hp#初始血量不改變
            self.blood = self.hp#隨著遊戲改變的血量
            self.distance = 10
            self.screen = screen
            self.level = 1

        def levelUP(self):
            atk_ran = random.randint(5, 8)
            hp_ran = random.randint(6, 9)
            self.attack += int(self.attack * (atk_ran / 10))
            self.hp += int(self.hp * (hp_ran / 10))
            self.blood = self.hp
            self.level += 1

        def showBlood(self):
            pygame.draw.rect(self.screen, Black,
                             (self.rect.topleft[0] + 15, self.rect.topleft[1] + 175 + self.distance, 144, 14))#外面黑框
            pygame.draw.rect(self.screen, colorBlood, (
            self.rect.topleft[0] + 50, self.rect.topleft[1] + 175 + self.distance + 2, (self.blood / self.hp) * 107,
            10))#血量框框
            font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 12)
            font_show = font.render("Lv " + str(self.level), True, White)
            (self.screen).blit(font_show, (self.rect.topleft[0] + 20, self.rect.topleft[1] + 175 + self.distance))

        def show(self):
            (self.screen).blit(self.image, self.pos)
            self.showBlood()

    class Boss(pygame.sprite.Sprite):
        def __init__(self, atk, hp, screen):  # (編號,攻擊力,血量)
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load("images//boss.png"), (175, 175))
            self.rect = self.image.get_rect()
            self.pos = (130, 15)
            self.rect.topleft = self.pos
            self.attack = atk
            self.hp = hp
            self.blood = self.hp
            self.distance = 10
            self.screen = screen
            self.level = 1

        def levelUP(self):
            self.attack = self.attack * 2
            self.hp += self.hp * 4
            self.blood = self.hp
            self.level += 1

        def showBlood(self):
            pygame.draw.rect(self.screen, Black,
                             (self.rect.topleft[0] + 15, self.rect.topleft[1] + 175 + self.distance, 144, 14))
            pygame.draw.rect(self.screen, colorBlood, (
            self.rect.topleft[0] + 50, self.rect.topleft[1] + 175 + self.distance + 2, (self.blood / self.hp) * 107,
            10))
            font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 12)
            font_show = font.render("Lv " + str(self.level), True, White)
            (self.screen).blit(font_show, (self.rect.topleft[0] + 20, self.rect.topleft[1] + 175 + self.distance))

        def show(self):
            (self.screen).blit(self.image, self.pos)
            self.showBlood()

    def __init__(self, atk, hp, screen):  # (攻擊力,血量)
        self.attack = atk
        self.hp = hp
        self.blood = self.hp
        self.level = 1
        self.screen = screen
        # (編號,攻擊力,血量)
        self.enemys = [self.Enemy(1, 73, 160, screen),
                       self.Enemy(4, 72, 260, screen),
                       self.Enemy(5, 79, 171, screen),
                       self.Enemy(6, 62, 550, screen)]
        self.boss = self.Boss(700, 2400, screen)

    def levelUP(self):
        sub = self.hp - self.blood
        atk_ran = random.randint(1, 3)
        hp_ran = random.randint(1, 3)
        self.attack += int(self.attack * (atk_ran / 10))
        self.hp += int(self.hp * (hp_ran / 10))
        self.blood = int(self.hp - sub)
        self.level += 1

    def showBlood(self):
        pygame.draw.rect(self.screen, Black, (60, 246, 390, 14))##x,y座標都是從左上角算起
        pygame.draw.rect(self.screen, colorBlood, (62, 248, (self.blood / self.hp) * 386, 10))
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 11)
        font_show = font.render(str(self.blood) + " / " + str(self.hp), True, Gray)
        (self.screen).blit(font_show, (380, 247))

    def Bar(self, screen, cnt, i, total):
        pygame.draw.rect(screen, Brown, (0, 690, 450, 30))
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 15)
        font_show = font.render("第 " + str(self.level) + " 關   |  第 " + str(cnt) + " 回  |  第 " + str(
            i + 1) + " 題  |   累積傷害： " + str(total), True, White)
        (self.screen).blit(font_show, (80, 690 + 7))