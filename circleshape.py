import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub classes will override
        pass

    def update(self, dt):
        # Sub classes will override
        pass

    def check_collision(self, other) -> bool :
        # Check if the distance between the two objects is less than the sum of their radii
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius

