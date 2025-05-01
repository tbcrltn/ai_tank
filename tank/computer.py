import pygame
import math
class Computer:
    def __init__(self, x, y, screen, player, speed, clock, game):
        self.xpos, self.ypos = x, y
        self.screen = screen
        self.speed = speed
        self.clock = clock
        self.player = player
        self.image = pygame.image.load("sprites/tankBase.png")
        self.red_image = pygame.image.load("sprites/redTank.png")
        self.red_image = pygame.transform.scale(self.red_image, (40, 40))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.og_turret_image = pygame.image.load("sprites/tankTurret.png")
        self.turret_image = pygame.transform.scale(self.og_turret_image, (50, 50))
        self.redturret_image = pygame.image.load("sprites/redTurret.png")
        self.redturret_image = pygame.transform.scale(self.redturret_image, (50, 50))
        self.enemy = self.image.get_rect(topleft = (self.xpos, self.ypos))
        self.turret = self.image.get_rect(topleft = self.enemy.topleft)
        self.health = 5
        self.game = game
        self.color_timer = 31
        self.shoot_rate = 30
        self.direction = "down"
        self.angle = 0
       
    def blit(self):
        if self.direction == "up":
            self.angle = 0
        if self.direction == "left":
            self.angle = 90
        if self.direction == "down":
            self.angle = 180
        if self.direction == "right":
            self.angle = 270
        self.color_timer += 1
        if self.color_timer > 15:
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            self.screen.blit(rotated_image, self.enemy)
            self.turret_image = pygame.transform.scale(self.og_turret_image, (50, 50))

        else:
            rotated_image = pygame.transform.rotate(self.red_image, self.angle)
            self.screen.blit(rotated_image, self.enemy)
            self.turret_image = self.redturret_image


    def move(self):
        if self.shoot_rate > 30:
            self.game.enemy_shoot(self)
            self.shoot_rate = 0 
        else:
            self.shoot_rate += 1
        new_rect = self.enemy.copy()
        if self.direction == "right":
            new_rect.x += self.speed
        elif self.direction == "left":
            new_rect.x -= self.speed
        elif self.direction == "up":
            new_rect.y -= self.speed
        elif self.direction == "down":
            new_rect.y += self.speed

        # Check wall collisions BEFORE moving
        for wall in self.game.walls:
            if new_rect.colliderect(wall):
                return  

        # No collision — safe to move
        self.enemy = new_rect


    def hit_wall(self):
        if self.direction == "right":
            self.enemy.x -= self.speed
        elif self.direction == "down":
            self.enemy.y -= self.speed
        elif self.direction == "up":
            self.enemy.y += self.speed
        elif self.direction == "left":
            self.enemy.x += self.speed

        
    def damage(self):
        self.health -= 1
        self.color_timer = 0
        if self.health == 0:
            self.enemy.x = -10000
            


    def update_turret(self):
        player_x, player_y = self.player.player.centerx, self.player.player.centery
        dist_x = player_x - self.enemy.x
        dist_y = player_y - self.enemy.y
        angle = math.atan2(dist_y, dist_x)  
        angle_degrees = math.degrees(angle)  
       
        rotated_turret = pygame.transform.rotate(self.turret_image, -angle_degrees-90)
            
        rotated_rect = rotated_turret.get_rect(center=self.enemy.center)

        
        self.screen.blit(rotated_turret, rotated_rect.topleft)


       
        

