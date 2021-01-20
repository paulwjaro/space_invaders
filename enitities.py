import pygame

pygame.init()

spd = 0.1
score = 0


class Entity:
    def __init__(self, x, y, img):
        self.x_pos = x
        self.y_pos = y
        self.sprite = img

    def draw_entity(self, _screen):
        _screen.blit(self.sprite, (self.x_pos, self.y_pos))

    def entity_state(self, _screen):
        self.draw_entity(_screen)



class Player(Entity):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
        self.left = 0
        self.right = 0
        self.bullets = []

    def entity_state(self, _screen, _width, _enemy_list, _explosion):
        self.draw_entity(_screen)
        self.moving(_width)

        if len(self.bullets) != 0:
            for bullet in self.bullets:
                if bullet.y_pos > 10:
                    bullet.move(_screen, _enemy_list, _explosion)
                else:
                    self.bullets.pop(self.bullets.index(bullet))

    def moving(self, width):
        axis = self.right - self.left
        if axis > 0 and self.x_pos + axis + 64 >= width:
            axis = 0
        elif axis < 0 and self.x_pos + axis <= 0:
            axis = 0
        self.x_pos += axis * spd

    def fire(self):
        bullet = Bullet(self.x_pos + 16, self.y_pos)
        self.bullets.append(bullet)


class Enemy(Entity):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
        self.dir = 1

    def entity_state(self, _screen, _width):
        self.draw_entity(_screen)
        self.movement(_width)

    def movement(self, _width):
        _spd = self.dir * 0.05
        if self.x_pos + _spd + 64 >= _width:
            self.dir = -1
            self.y_pos += 32
        elif self.x_pos + _spd <= 0:
            if self.y_pos > 32:
                self.dir = 1
                self.y_pos += 32

        self.x_pos += _spd


class Bullet:
    def __init__(self, x, y):
        self.img = pygame.image.load('bullet.png')
        self.x_pos = x
        self.y_pos = y

    def move(self, _screen, _enemy_list, _explosion):
        _screen.blit(self.img, (self.x_pos, self.y_pos))
        self.enemy_collision(_enemy_list, _explosion)
        self.y_pos -= 0.5

    def enemy_collision(self, enemy_list, _explosion):
        global score
        for enemy in enemy_list:
            if enemy.x_pos < self.x_pos < (enemy.x_pos + 64) and enemy.y_pos < self.y_pos < enemy.y_pos + 64:
                enemy_list.pop(enemy_list.index(enemy))
                _explosion()
                score += 1
                print(score)


