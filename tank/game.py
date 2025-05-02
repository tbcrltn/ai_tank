import pygame
from player import Player
from level import Level
from bullet import Bullet
from computer import Computer
from ai import AI
import numpy as np 
from collections import deque

MAX_MEMORY = 100000


class Game:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.running = True
        self.clock = pygame.time.Clock()
        self.reward = 0
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.dt = 0
        self.level = Level(self.screen, self)
        self.current_level = 1
        self.player = Player(self.player_pos, self.screen, self.dt, self.clock, self, 2)
        self.computer = Computer(200, 600, self.screen, self.player, 1, self.clock, self)
        self.bullet = Bullet(self.screen, 5, self.player, self.computer)
        self.font = pygame.font.Font("fonts/pixel.ttf", 20)
        self.enemies = []
        self.enemy_pos = []
        self.enemies.append(self.computer)
        self.enemy_pos.append((75,75))
        self.over = False
        self.walls = self.level.draw(self.current_level)
        self.ai = AI(self.player, self.bullet, self.walls, self.computer)
        self.memory = deque(maxlen=MAX_MEMORY)

    def runGame(self):
        self.main_menu()
        while self.running:
            self.check_events()
            self.blit_screen()
            if not self.over:
                self.player.move()
                self.walls = self.level.draw(self.current_level)
                #AI Tank
                self.Tank_AI()

                
                self.player.blit()
                self.bullet.update_bullets()
                self.bullet.update_enemy_bullets()
                self.manage_health()
                self.display_level()
                self.blit_enemies()
                self.player.update_turret()
            self.clock.tick(60)
            
            self.moving = True
            self.check_game_over()
            self.check_win()
            pygame.display.flip()


        pygame.quit()









        
    def reset(self):
        done = False
        destroyed = self.check_destroyed()
        self.long_term()
        print(self.ai.epsilon)
        if destroyed:
            self.player.player.x = self.player_pos.x
            self.player.player.y = self.player_pos.y
            self.current_level += 1
            for enemy in self.enemies:
                enemy.enemy.x = self.enemy_pos[self.enemies.index(enemy)][0]
                enemy.enemy.y = self.enemy_pos[self.enemies.index(enemy)][1]
                enemy.health = 5
            self.bullet.destroybullet()
            done = True

        return done
    
    def reward_wall(self): 
        for wall in self.walls:
            for enemy in self.enemies:   
                if enemy.enemy.colliderect(wall):
                    print("hit")
        return False
                    
    def reward_damage(self): 
        for bullet in self.bullet.bullets:
            for enemy in self.enemies:
                if enemy.enemy.colliderect(bullet):
                    return True
        return False
    
    def wall_collision(self):
        for wall in self.walls:
            if self.player.player.colliderect(wall):
                self.player.hit_wall()
                
            for enemy in self.enemies:   
  

                if enemy.enemy.colliderect(self.player.player):
                    self.player.hit_wall()


    def bullet_collision(self):
        for bullet in self.bullet.bullets:
            for enemy in self.enemies:
                if enemy.enemy.colliderect(bullet):
                    self.bullet.destroy(bullet)
                    enemy.damage()
                    return True
            for wall in self.walls:
                if wall.colliderect(bullet):
                    self.bullet.destroy(bullet)
        for bullet in self.bullet.enemy_bullets:
            if self.player.player.colliderect(bullet):
                self.bullet.enemy_destroy(bullet)
                self.player.damage()
            for wall in self.walls:
                if wall.colliderect(bullet):
                    self.bullet.enemy_destroy(bullet)
    
    def reset_player(self):
        self.bullet.destroybullet()
        self.player.player.x = self.player_pos.x
        self.player.player.y = self.player_pos.y
        self.player.health = 5
        for enemy in self.enemies:
            enemy.enemy.x = self.enemy_pos[self.enemies.index(enemy)][0]
            enemy.enemy.y = self.enemy_pos[self.enemies.index(enemy)][1]
            enemy.health = 5


    def enemy_shoot(self, enemy):
        self.bullet.enemy_shoot(enemy)
    
    def manage_health(self):
        text = self.font.render("LIVES:", False, "black")
        self.screen.blit(text, (1050, 35))
        for x in range(self.player.lives):
            dist = x*25
            image = pygame.image.load("sprites/heart.png")
            image = pygame.transform.scale(image, (20, 20))
            self.screen.blit(image, (1120+dist, 35))

    def new_enemy(self, x, y):
        enemy = Computer(x, y, self.screen, self.player, 1, self.clock, self)
        self.enemies.append(enemy)
        self.enemy_pos.append((x,y))

    def check_destroyed(self):
        for enemy in self.enemies:
            if not enemy.enemy.x < 0:
                return False
        return True
    
    def game_over(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.fill("black")
        font = pygame.font.Font("fonts/pixel.ttf", 100)
        rendered_font = font.render("GAME OVER", False, "red")
        self.screen.blit(rendered_font, (1280/2-300, 720/2-50))
        rect = pygame.Rect(1280/2-50, 720/2+200, 100, 50)
        text = self.font.render("RETRY", False, "black")
        if rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(self.screen, "red", rect)
            self.screen.blit(text, (rect.x+13, rect.y+20))
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                self.over = False
                self.current_level = 1
                self.reset()
                self.reset_player()
                self.player.health = 5
                self.player.lives = 3
                self.enemies = [self.computer]
        else:
            pygame.draw.rect(self.screen, "white", rect)
            self.screen.blit(text, (rect.x+13, rect.y+20))
        

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.bullet.shoot()

    def blit_screen(self):
        if not self.over:
            image = pygame.image.load("sprites/grass.jpg")
            image = pygame.transform.scale(image, (1280, 720))
            self.screen.blit(image, (0,0))
            
    def check_game_over(self):
        if self.over:
            self.game_over()
    def blit_enemies(self):
        for enemy in self.enemies:
            enemy.blit()
            enemy.update_turret()


    def win_game(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.fill("black")
        font = pygame.font.Font("fonts/pixel.ttf", 100)
        rendered_font = font.render("YOU WIN!", False, (0, 180, 0))
        self.screen.blit(rendered_font, (1280/2-250, 720/2-50))
        rect = pygame.Rect(1280/2-100, 720/2+200, 150, 50)
        text = self.font.render("PLAY AGAIN", False, "black")
        if rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(self.screen, (0, 180, 0), rect)
            self.screen.blit(text, (rect.x+13, rect.y+20))
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                self.over = False
                self.current_level = 1
                self.reset()
                self.reset_player()
                self.player.health = 5
                self.player.lives = 3
                self.enemies = [self.computer]
        else:
            pygame.draw.rect(self.screen, "white", rect)
            self.screen.blit(text, (rect.x+13, rect.y+20))

    def check_win(self):
        if self.current_level == 21:
            self.win_game()

    def main_menu(self):
        menu_up = True
        
        font = pygame.font.Font("fonts/pixel.ttf", 100)
        rendered_font = font.render("TANK GAME", False, (0, 180, 0))
        rect = pygame.Rect(1280/2-50, 720/2+200, 100, 50)
        text = self.font.render("PLAY", False, "black")
        while menu_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    menu_up = False
    
            self.screen.fill("black")
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.screen.blit(rendered_font, (1280/2-280, 720/2-50))
            if rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(self.screen, (0, 180, 0), rect)
                mouse = pygame.mouse.get_pressed()
                if mouse[0]:
                    menu_up = False
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), rect)
            
            self.screen.blit(text, (rect.x+22.5, rect.y+20))
            
            
            pygame.display.flip()
            
    def display_level(self):
        level = self.font.render(f"LEVEL: {self.current_level}", False, "black")
        self.screen.blit(level, (35, 35))

    def Tank_AI(self): 
        done = False
        #ai
        # Get state
        state_old = self.ai.get_states()

        # Get action index
        action_index = self.ai.get_action(state_old)

        # Map index to movement
        moves = ["up", "down", "left", "right", "stationary"]
        movement = moves[action_index]
        self.computer.direction = movement
        self.move_enemies()

        # Get reward and new state
        reward = self.get_reward()
        new_state = self.ai.get_states()
        done = self.computer.health == 0

        # Store and train
        self.ai.remember(state_old, action_index, reward, new_state, done)
        self.train_short_term_memory(state_old, action_index, reward, new_state, done)

        if done:
            self.reset()

    

    def train_short_term_memory(self, state_old, prob, reward, new_state, done): 
        self.ai.train_short_term(state_old, prob, reward, new_state, done)


    def get_reward(self): 
        wall_col =  self.computer.move()
        damage = self.bullet_collision()
        reward = self.ai.get_reward(wall_col, damage)
        self.reward = reward
        return reward

    def long_term(self):
        self.ai.train_long_term_memory()
        self.ai.n_games += 1
        print(self.ai.n_games, self.reward, self.ai.epsilon)



