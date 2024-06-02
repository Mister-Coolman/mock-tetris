import pygame

clicked = False

class Button():
    def __init__(self, x: int, y: int, image: pygame.Surface, scale: float) -> None:
        self.image = pygame.transform.scale_by(image, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self, surface: pygame.Surface) -> bool:
        global clicked
        pressed = False

        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and not clicked:
                clicked = True
                pressed = True
        else:
            clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return pressed
