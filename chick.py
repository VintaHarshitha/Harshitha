import pygame.display
pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("FARM GAME")
icon = pygame.image.load('hen.png')
pygame.display.set_icon(icon)
player1Img=pygame.image.load('player1.png')
player1X = 100
player1Y = 570
player2Img = pygame.image.load('player2.png')
player2X = 220
player2Y = 570
house1Img = pygame.image.load('house1.png')
house1X = 500
house1Y = 150
fox1Img = pygame.image.load('fox1.png')
fox1X = 580
fox1Y = 500
grass1Img = pygame.image.load('grass1.png')
grass1X = 590
grass1Y = 550
grass2Img = pygame.image.load('grass2.png')
grass2X = 340
grass2Y = 550
grass3Img = pygame.image.load('grass3.png')
grass3X = 0
grass3Y = 570
grass4Img = pygame.image.load('grass4.png')
grass4X = 0
grass4Y = 610
grass5Img = pygame.image.load('grass5.png')
grass5X = 185
grass5Y = 610
grass6Img = pygame.image.load('grass6.png')
grass6X = 180
grass6Y = 570
grass7Img = pygame.image.load('grass7.png')
grass7X = 340
grass7Y = 570
grass8Img = pygame.image.load('grass8.png')
grass8X = 340
grass8Y = 610
grass9Img = pygame.image.load('grass9.png')
grass9X = 0
grass9Y = 550
balloon1Img = pygame.image.load('balloon1.png')
balloon1X = 0
balloon1Y = 500
balloon2Img = pygame.image.load('balloon2.png')
balloon2X = 0
balloon2Y = 450
blastImg = pygame.image.load('blast.png')
blastX = 380
blastY = 450


def player1():
    screen.blit(player1Img, (player1X, player1Y))
def player2():
    screen.blit(player2Img, (player2X, player2Y))
def house1():
    screen.blit(house1Img, (house1X, house1Y))
def fox1():
    screen.blit(fox1Img, (fox1X, fox1Y))
def grass1():
    screen.blit(grass1Img, (grass1X, grass1Y))
def grass2():
    screen.blit(grass1Img, (grass2X, grass2Y))
def grass3():
    screen.blit(grass3Img, (grass3X, grass3Y))
def grass4():
    screen.blit(grass4Img, (grass4X, grass4Y))
def grass5():
    screen.blit(grass5Img, (grass5X, grass5Y))
def grass6():
    screen.blit(grass6Img, (grass6X, grass6Y))
def grass7():
    screen.blit(grass7Img, (grass7X, grass7Y))
def grass8():
    screen.blit(grass8Img, (grass8X, grass8Y))
def grass9():
    screen.blit(grass9Img, (grass9X, grass9Y))
def balloon1():
    screen.blit(balloon1Img, (balloon1X, balloon1Y))
def balloon2():
    screen.blit(balloon2Img, (balloon2X, balloon2Y))
def blast():
    screen.blit(blastImg, (blastX, blastY))


running=True
while running:
    player1X += 0.12
    player2X += 0.11
    fox1X -= 0.6
    if fox1X <= 370:
        balloon1X += 5
        balloon2X += 5
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,255,0))
    player1()
    player2()
    house1()
    fox1()
    grass1()
    grass2()
    grass3()
    grass4()
    grass5()
    grass6()
    grass7()
    grass8()
    grass9()
    balloon1()
    balloon2()
    if player2X >= 250:
        player2X = 250
    if player1X >= 150:
        player1X = 150
    if balloon1X >= 380:
        balloon1X = 380
    if balloon2X >= 380:
        balloon2X = 380
        fox1Y += 10
        blast()
    pygame.display.update()