import pygame
import random

pygame.init()
pygame.display.set_caption('ErikJaKertSneeeeeiK')
ekraan = pygame.display.set_mode([450,450]) #Loob ekraani mängu jaoks
välja = False #välja kui uss sööb ennast ja nupuvajutus
ajanäitaja = pygame.time.Clock() # et teha tick ja näha normaalseslt ussi
peapilt = pygame.image.load('homerr.png')
peapiltrect = peapilt.get_rect()
söögipilt = pygame.image.load('donut.png')
söögipiltrect = söögipilt.get_rect()
taust = pygame.image.load('pilved.jpg')

class Pea():
    def __init__(madu_uss):
        madu_uss.location = [random.randint(4,10) * 20,random.randint(4,10) * 20]
        madu_uss.direction = random.randint(0,20)
        return
    
    def liikumine(madu_uss): #Põhiosa ussi liikumiseks
        pööratud = False
        for nupuvajutus in pygame.event.get():
            if nupuvajutus.type == pygame.KEYDOWN:
                välja = True
            
                if nupuvajutus.key == pygame.K_q:
                    välja == True
                elif nupuvajutus.key == pygame.K_w and madu_uss.direction != 2:
                    madu_uss.direction = 0
                    pööratud = True
                elif nupuvajutus.key == pygame.K_s and madu_uss.direction != 0:
                    madu_uss.direction = 2
                    pööratud = True
                elif nupuvajutus.key == pygame.K_d and madu_uss.direction != 3:
                    madu_uss.direction = 1
                    pööratud = True
                elif nupuvajutus.key == pygame.K_a and madu_uss.direction != 1:
                    madu_uss.direction = 3
                    pööratud = True
                elif nupuvajutus.key == pygame.K_ESCAPE:
                    pygame.quit()
                     
        if madu_uss.direction == 0: # ussi kehaosade paiknemine üksteise suhtes, õige suhe söögi ja keha vahel(et jääks keskele)
            madu_uss.location[1] -= 20
        if madu_uss.direction == 1:
            madu_uss.location[0] += 20
        if madu_uss.direction == 2:
            madu_uss.location[1] += 20
        if madu_uss.direction == 3:
            madu_uss.location[0] -= 20
            
        if pea.location[0] < 0: #Õigetel väärtustel ei lähe raamidest välja, tõkestamine
            pea.location[0] = 440
        if pea.location[0] > 440:
            pea.location[0] = 0
        if pea.location[1] < 0:
            pea.location[1] = 440
        if pea.location[1] > 440:
            pea.location[1] = 0
        return

keha = []
pea = Pea()
pöörded = 0
söögi_asetsus = [random.randint(1, 20) * 20,random.randint(1, 20) * 20] #Söök random kohta
must = (0,0,0)
lõpetus = False
while (lõpetus==False):
    ekraan.fill(must)
    uusfont = pygame.font.SysFont("Britannic Bold", 40)
    kiri_ekraanile = uusfont.render('Head mänguelamust!', 1, (255, 255, 0))
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            lõpetus=True
    ekraan.blit(kiri_ekraanile,(75,100))
    pygame.display.flip()
while not välja: # Main mäng
    ajanäitaja.tick(10)
    pöörded += 1
    söök = False
    
    if pea.location == söögi_asetsus:
        söök = True
        söögi_asetsus = [random.randint(1, 20) * 20,random.randint(1, 20) * 20]
    if (pöörded < 3):
        söök = True
    if not söök:
        del keha[0]
    keha.append([pea.location[0],pea.location[1]]) #Lisab keha listi juurde, keha pikemaks
    pea.liikumine()
           
    ekraan.blit(taust, (0,0))#ekraanivärv(taust)
    font = pygame.font.Font(None,20)
    score_text = font.render("Score: " + str((len(keha) - 2)*100) + "",1,(random.randint(0,250),random.randint(0,250),random.randint(0,250)))#Teeb vikerkaare :)))
    ekraan.blit(score_text,[370,5])
    for osa in keha: #Surm
        pygame.draw.rect(ekraan,[255, 255, 0],[osa[0],osa[1],20,20],0)
        if osa != keha[0] and [osa[0],osa[1]] == pea.location:
            välja = True
            basicfont = pygame.font.SysFont(None, 48)
            lõputekst = basicfont.render("Mäng läbi!", True, (255,255,255),(0,0,0))
            ekraan.blit(lõputekst,[150,150])
            
    pygame.draw.rect(ekraan,[0, 0, 0],[pea.location[0],pea.location[1],20,20],0) #Näitamine ekraanil(joonistamine peavärvid)
    pygame.draw.rect(ekraan,[100,25,67],[söögi_asetsus[0],söögi_asetsus[1],20,20],0) #Näitamine ekraanil(joonistamine söök, värvid)
    ekraan.blit(peapilt, pea.location)
    ekraan.blit(söögipilt, söögi_asetsus)
    pygame.display.flip()#Uuendab ekraanil toimuvat 
pygame.quit()


