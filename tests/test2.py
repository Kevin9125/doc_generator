import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, image: str, vitesse: int, x: int, y: int):
        self.image = pygame.image.load(image).convert()
        self.vitesse = vitesse
        self.x = x
        self.y = y

    def avancer(self) -> None:
        if self.x < 365:
            self.x = self.x + self.vitesse
        elif self.x > 365:
            self.x = self.x - self.vitesse

    def get_x(self) -> int:
        return self.x 
    
    def get_y(self) -> int:
        return self.y
    
    def get_image(self):
        return self.image
    
    def get_vitesse(self) -> int:
        return self.vitesse
    
    def modif_speed(self, new_vitesse) -> None:
        self.vitesse = new_vitesse

    def mort(self, new_y) -> None:
        self.y = new_y
        self.vitesse = 0
        