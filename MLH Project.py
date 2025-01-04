import pygame
import sys
import random


# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption("Feed the Cat")

# Load the cat
cat = pygame.image.load(r"C:\Users\pmili\Downloads\Screenshot_2025-01-03_155703-removebg-preview.png")
catx, caty = 40, 50  # Initial position

# Load the fish
fish = pygame.image.load(r"C:\Users\pmili\Downloads\Screenshot_2025-01-03_172249-removebg-preview.png")
fishx, fishy = 176, 550  # Initial position

# setup for feeding
foodState = "nothing"
mouse_x, mouse_y = 0, 0
originFishsizeX, originFishsizeY = fish.get_size()
feedingFish = pygame.transform.scale(fish, (int(originFishsizeX*0.5), int(originFishsizeY*0.5)))
randBlue = random.randint(0, 255)
randRed = random.randint(0, 255)
randGreen = random.randint(0, 255)

#set up for heart
heart = pygame.image.load(r"C:\Users\pmili\Downloads\Screenshot_2025-01-03_171411-removebg-preview.png")
heartSizeX, heartSizeY = heart.get_size()


# setup for text
font = pygame.font.Font(None, 25)
fontBIG = pygame.font.Font(None, 50)
score = 0
text = font.render("Number of Fish Eaten: " + str(score), True, (mouse_x, 230, 230))

#particle system
class fish_Particle:
    def __init__(self, y, x, velY, velX, shape, color):
        #mouse_x, mouse_y = pygame.mouse.get_pos()
        self.y = 265
        self.x = 190
        self.velY = random.randint(-10, 0)
        self.velX = random.randint(-10, 10)
        self.shape = random.randint(1, 2)
        self.color = (0, 230 + random.randint(-20, 20), 230 + random.randint(-20, 20), 100)
        #print(str(self.y) + " " + str(self.x) + " " + str(self.velY))

    def update(self):
        self.velY += 1
        self.y += self.velY
        self.x += self.velX

    def draw(self, screen):
        #screen = pygame.display.set_mode((600, 750))
        if(self.shape == 1):
            pygame.draw.rect(screen, self.color[:3], (self.x, self.y, 10, 10))
        else:
            pygame.draw.circle(screen, self.color[:3], (self.x, self.y), 10)

class heart_Particle:
    def __init__(self, y, x, size):
        
        self.y = random.randint(90, 410)
        self.x = random.randint(50, 450)
        self.size = random.randint(2, 6)/4
        

    def update(self):
        self.y -= 2.5
        self.size *= 0.975

    def draw(self, screen):
        #screen = pygame.display.set_mode((600, 750))
        heart = pygame.image.load(r"C:\Users\pmili\Downloads\Screenshot_2025-01-03_171411-removebg-preview.png")
        heartScaled = pygame.transform.scale(heart, (int(heartSizeX*self.size), int(heartSizeY*self.size)))
        screen.blit(heartScaled, (self.x, self.y))
    
    
    
fish_Particles = []
heart_Particles = []
messages = [
    "", "You're PURR-fect as is!", "CAT get enough of you!", "You're PAWesome!", "You'll go down in HISS-tory!", "You look very PURR-ty!", "So FUR, so good!", "You give me PURR joy!", "You're HISS-terical!", "You are radi-CLAW, dude!", "Stay PAW-sitive!", "I am so FUR-tunate to have you!", "You the best FUR-end!", "You have an amazing PURR-sonality!", "Let's PURR-sonality!"
]

message = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((175, 100, 50))
     
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Place Fish and Cat
    screen.blit(cat, (catx, caty))
    pygame.draw.rect(screen, (0, 100, 100), (200, 580, 220, 110))

    # Place text and instructions
    text = font.render("Number of Fish Eaten: " + str(score), True, (230, 230, 230))
    instructions = fontBIG.render("Drag Fish to Feed the Cat!", True, (230, 230, 230))
    inspiration = font.render(messages[message], True, (230, 230, 230))
    screen.blit(text, (10, 10))
    screen.blit(instructions, (100, 700))
    screen.blit(inspiration, (275, 175))

    # fish counter
    if mouse_x > 200 and mouse_x < 410 and mouse_y > 580 and mouse_y < 690:
        pygame.draw.rect(screen, (0, 70, 70), (200, 580, 220, 110))
        #print(foodState)
        if foodState == "nothing" and event.type == pygame.MOUSEBUTTONDOWN:
            randBlue = random.randint(0, 255)
            randRed = random.randint(0, 255)
            randGreen = random.randint(0, 255)
            foodState = "fish"

    if mouse_x > 50 and mouse_x < 530 and mouse_y > 50 and mouse_y < 490:
        #print(foodState)
        if foodState == "fish" and event.type == pygame.MOUSEBUTTONDOWN:
            foodState = "nothing"
            score+=1
            for i in range(random.randint(20, 45)):
                fish_Particles.append(fish_Particle(1, 1, 1, 1, 1, 1))
            for i in range(random.randint(3, 7)):
                heart_Particles.append(heart_Particle(1, 1, 1))
            message = random.randint(1, len(messages)-1)
                #print(i)
            #print(fish_Particles)

    screen.blit(fish, (fishx, fishy))
            
    #print(str(mouse_y) + " " + str(mouse_x))
    if foodState == "fish":
        feedingFish = pygame.transform.scale(fish, (int(originFishsizeX*0.5), int(originFishsizeY*0.5)))
        screen.blit(feedingFish, (mouse_x - 50, mouse_y - 50))
        feedingFish2 = pygame.transform.scale(fish, (int(originFishsizeX*0.375), int(originFishsizeY*0.325)))
        feedingFish2.fill((randRed, randBlue, randGreen, 100))
        #feedingFish2.fill(0, 0, 0)
        screen.blit(feedingFish2, (mouse_x - 27.5, mouse_y - 32.5))
        
    for fish_piece in fish_Particles[:]:
        fish_piece.update()
        fish_piece.draw(screen)
        if(fish_piece.y < 0 and fish_piece.x < 0 and fish_piece.x > 750 and fish_piece.y > 600):
            fish_Particles.remove(fish_piece)
    
    for heart_piece in heart_Particles[:]:
        heart_piece.update()
        heart_piece.draw(screen)
        if(heart_piece.size < 0.20):
            heart_Particles.remove(heart_piece)

    # Update display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(120)

pygame.quit()
sys.exit()