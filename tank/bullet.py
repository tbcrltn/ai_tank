import pygame
import math

class Bullet:
    def __init__(self, screen, speed, player, computer):
        self.screen = screen
        self.speed = speed
        self.player = player
        self.bullets = []
        self.bullet_dx = []
        self.bullet_dy = []
        self.enemy_bullets = []
        self.enemy_bullet_dx = []
        self.enemy_bullet_dy = []
        self.computer = computer
        self.max_bullets = 4
        
    def shoot(self):
        if len(self.bullets) < self.max_bullets:
            player_x = self.player.player.centerx
            player_y = self.player.player.centery
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.bullets.append(pygame.Rect(player_x, player_y, 5, 5))
            dx, dy = self.calculate_direction(player_x, player_y, mouse_x, mouse_y)
            self.bullet_dx.append(dx)
            self.bullet_dy.append(dy)
    def update_bullets(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, "red", bullet)
            bullet.x -= self.bullet_dx[self.bullets.index(bullet)] * self.speed
            bullet.y -= self.bullet_dy[self.bullets.index(bullet)] * self.speed            
    def calculate_direction(self, start_x, start_y, target_x, target_y):
        dx = start_x - target_x
        dy = start_y - target_y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        return dx, dy     
    def destroy(self, bullet):
        try:
            self.bullet_dx.pop(self.bullets.index(bullet))
            self.bullet_dy.pop(self.bullets.index(bullet))
            self.bullets.remove(bullet)
        except:
            pass
        
    def enemy_shoot(self, enemy_type):
        enemy_x = enemy_type.enemy.centerx
        enemy_y = enemy_type.enemy.centery
        player_x = self.player.player.centerx
        player_y = self.player.player.centery
        self.enemy_bullets.append(pygame.Rect(enemy_x, enemy_y, 5, 5))
        dx, dy = self.calculate_direction(enemy_x, enemy_y, player_x, player_y)
        self.enemy_bullet_dx.append(dx)
        self.enemy_bullet_dy.append(dy)
    
    def destroybullet(self): 
        self.bullets = []
        self.bullet_dx = []
        self.bullet_dy = []
        self.enemy_bullets = []
        self.enemy_bullet_dx = []
        self.enemy_bullet_dy = []
    def update_enemy_bullets(self):
        
        for bullet in self.enemy_bullets:
            pygame.draw.rect(self.screen, "red", bullet)
            bullet.x -= self.enemy_bullet_dx[self.enemy_bullets.index(bullet)] * self.speed
            bullet.y -= self.enemy_bullet_dy[self.enemy_bullets.index(bullet)] * self.speed
    def enemy_destroy(self, bullet):
        try:
            self.enemy_bullet_dx.pop(self.enemy_bullets.index(bullet))
            self.enemy_bullet_dy.pop(self.enemy_bullets.index(bullet))
            self.enemy_bullets.remove(bullet)
        except:
            pass
        
        