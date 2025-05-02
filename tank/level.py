import pygame

class Level:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        image = pygame.image.load("sprites/wall.png")
        self.wall_image = pygame.transform.scale(image, (1300, 750))
    def draw(self, level): 
        if level == 1:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25)
            ]
        elif level == 2:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(250, 300, 25, 275),
                pygame.Rect(250, 300, 275, 25),
                pygame.Rect(780, 435, 275, 25),
                pygame.Rect(1030, 160, 25, 275)
            ]
        elif level == 3:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(648, 420, 25, 275),
                pygame.Rect(648, 0, 25, 275),
                pygame.Rect(250, 210, 25, 275),
                pygame.Rect(1030, 210, 25, 275)
            ]
        elif level == 4:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(200, 0, 25, 300),
                pygame.Rect(400, 100, 25, 400),
                pygame.Rect(600, 300, 25, 200),
                pygame.Rect(800, 0, 25, 200),
                pygame.Rect(100, 400, 200, 25),
                pygame.Rect(600, 500, 25, 100),
                pygame.Rect(1000, 400, 200, 25)
            ]
        elif level == 5:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(200, 0, 25, 200),
                pygame.Rect(400, 200, 25, 400),
                pygame.Rect(600, 0, 25, 200),
                pygame.Rect(800, 200, 25, 400),
                pygame.Rect(100, 500, 200, 25),
                pygame.Rect(900, 300, 200, 25),
                pygame.Rect(700, 500, 25, 100)
            ]
        elif level == 6:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(400, 0, 25, 300),
                pygame.Rect(200, 400, 200, 25),
                pygame.Rect(100, 200, 25, 200),
                pygame.Rect(800, 400, 200, 25)
            ]
        elif level == 7:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(300, 0, 25, 400),
                pygame.Rect(600, 100, 25, 600),
                pygame.Rect(100, 300, 200, 25),
                pygame.Rect(800, 500, 200, 25)
            ]
        elif level == 8:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(300, 0, 25, 400),
                pygame.Rect(500, 100, 200, 25),
                pygame.Rect(100, 500, 200, 25),
                pygame.Rect(800, 200, 25, 500)
            ]
        elif level == 9:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(500, 0, 25, 400),
                pygame.Rect(200, 300, 200, 25),
                pygame.Rect(600, 400, 200, 25),
                pygame.Rect(900, 150, 25, 500)
            ]
        elif level == 10:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(400, 200, 25, 400),
                pygame.Rect(100, 200, 200, 25),
                pygame.Rect(600, 600, 200, 25),
                pygame.Rect(800, 400, 25, 200)
            ]
        elif level == 11:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(500, 0, 25, 400),
                pygame.Rect(100, 300, 200, 25),
                pygame.Rect(600, 250, 200, 25),
                pygame.Rect(900, 200, 25, 500)
            ]
        elif level == 12:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(500, 50, 25, 500),
                pygame.Rect(100, 300, 200, 25),
                pygame.Rect(600, 250, 200, 25),
                pygame.Rect(900, 200, 25, 500)
            ]
        elif level == 13:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(300, 0, 25, 400),
                pygame.Rect(200, 300, 200, 25),
                pygame.Rect(500, 400, 200, 25),
                pygame.Rect(900, 100, 25, 600)
            ]
        elif level == 14:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(500, 0, 25, 400),
                pygame.Rect(100, 300, 200, 25),
                pygame.Rect(600, 250, 200, 25),
                pygame.Rect(900, 200, 25, 500)
            ]
        elif level == 15:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(300, 0, 25, 400),
                pygame.Rect(600, 0, 25, 300),
                pygame.Rect(200, 400, 200, 25),
                pygame.Rect(800, 500, 200, 25)
            ]
        elif level == 16:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(350, 0, 25, 400),
                pygame.Rect(500, 300, 200, 25),
                pygame.Rect(600, 100, 25, 500),
                pygame.Rect(800, 400, 200, 25)
            ]
        elif level == 17:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(300, 0, 25, 400),
                pygame.Rect(500, 200, 200, 25),
                pygame.Rect(700, 400, 200, 25),
                pygame.Rect(100, 500, 200, 25)
            ]
        elif level == 18:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(200, 100, 25, 200),
                pygame.Rect(600, 100, 200, 25),
                pygame.Rect(800, 300, 200, 25),
                pygame.Rect(100, 500, 200, 25)
            ]
        elif level == 19:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(400, 100, 25, 400),
                pygame.Rect(200, 400, 25, 200),
                pygame.Rect(600, 300, 200, 25),
                pygame.Rect(800, 500, 200, 25)
            ]
        elif level == 20:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
                pygame.Rect(300, 0, 25, 400),
                pygame.Rect(500, 200, 200, 25),
                pygame.Rect(700, 400, 25, 200),
                pygame.Rect(100, 500, 200, 25),
                pygame.Rect(800, 300, 25, 400)
            ]
        elif level == 21:
            walls = [
                pygame.Rect(0, 0, 25, 720),
                pygame.Rect(0, 0, 1280, 25),
                pygame.Rect(1255, 0, 25, 720),
                pygame.Rect(0, 695, 1280, 25),
            ]
        if not self.game.over:
            for wall in walls:
                border_width = 4
                crop = self.wall_image.subsurface(wall)
                self.screen.blit(crop, wall)
            return walls


        