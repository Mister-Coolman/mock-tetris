import pygame

class Button():
    def __init__(self, x: int, y: int, image: pygame.Surface, scale: float) -> None:
        self.image = pygame.transform.scale_by(image, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface: pygame.Surface) -> bool:
        pressed = False

        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and not self.clicked:
                self.clicked = True
                pressed = True
        else:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return pressed
