import pygame
import math
class Player:
    def __init__(self, player_pos, screen, dt, clock, game, speed):
        self.player_pos = player_pos
        self.screen = screen
        self.dt = dt
        self.clock = clock
        self.image = pygame.image.load("sprites/tankBase.png")
        self.redimage = pygame.image.load("sprites/redTank.png")
        self.redturret = pygame.image.load("sprites/redTurret.png")
        self.turret_image = pygame.image.load("sprites/tankTurret.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.turret_image = pygame.transform.scale(self.turret_image, (50, 50))
        self.redimage = pygame.transform.scale(self.redimage, (40, 40))
        self.redturret = pygame.transform.scale(self.redturret, (50, 50))
        self.player = self.image.get_rect(topleft  = (self.player_pos.x, self.player_pos.y))
        self.turret = self.image.get_rect(topleft = (self.player_pos.x, self.player_pos.y))
        self.lives = 3
        self.health = 5
        self.game = game
        self.direction = "up"
        self.speed = speed
        self.color_timer = 30

    def blit(self):
        if self.direction == "up":
            angle = 0
        if self.direction == "left":
            angle = 90
        if self.direction == "down":
            angle = 180
        if self.direction == "right":
            angle = 270
        self.color_timer += 1
        if self.color_timer > 15:
            rotated_image = pygame.transform.rotate(self.image, angle)
            self.updated_turret_image = self.turret_image
        else:
            rotated_image = pygame.transform.rotate(self.redimage, angle)
            self.updated_turret_image = self.redturret
        
        self.screen.blit(rotated_image, self.player)

        

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction = "up"
            self.player.y -= self.speed

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction = "down"
            self.player.y += self.speed
            
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction = "left"
            self.player.x -= self.speed
            
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.player.x += self.speed
                
    def hit_wall(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player.y += self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player.y -= self.speed
            
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.x += self.speed
            
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.x -= self.speed

    def get_coor(self):
        return self.player.centerx, self.player.centery
    def damage(self):
        self.health -= 1
        self.color_timer = 0
        if self.health == 0:
            self.lives -= 1
            self.health = 5
            self.game.reset_player()
        if self.lives == 0:
            self.game.over = True
    
    def update_turret(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dist_x = mouse_x - self.player.x
        dist_y = mouse_y - self.player.y
        angle = math.atan2(dist_y, dist_x)  
        angle_degrees = math.degrees(angle)  
        rotated_turret = pygame.transform.rotate(self.updated_turret_image, -angle_degrees-90)

        rotated_rect = rotated_turret.get_rect(center=self.player.center)

        
        self.screen.blit(rotated_turret, rotated_rect.topleft)
        


            

        
        