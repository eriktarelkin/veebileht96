import pygame
import random

pygame.init()
pygame.display.set_caption('ErikJaKertSneeeeeiK')
ekraan = pygame.display.set_mode([450,450]) #Loob ekraani mängu jaoks
välja = False #välja kui uss sööb ennast ja nupuvajutus
ajanäitaja = pygame.time.Clock() # et teha tick ja näha normaalseslt ussi

class Pea():
    def __init__(madu_uss):
        madu_uss.location = [random.randint(4,10) * 20,random.randint(4,10) * 20]
        madu_uss.direction = random.randint(0,20)
        return
        

    def liikumine(madu_uss): #Põhiosa ussi liikumiseks
        pööratud = False
        for nupuvajutus in pygame.event.get():
            if nupuvajutus == pygame.QUIT: välja = True
            if nupuvajutus.type == pygame.KEYDOWN:
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
           
    ekraan.fill([255,255,255]) #ekraanivärv(taust)
    font = pygame.font.Font(None,20)
    score_text = font.render("Score: " + str(len(keha) - 2) + "",1,(random.randint(0,250),random.randint(0,250),random.randint(0,250)))#Teeb vikerkaare :)))
    ekraan.blit(score_text,[390,5])
    for osa in keha: #Surm
        pygame.draw.rect(ekraan,[0,0,0],[osa[0],osa[1],20,20],0)
        if osa != keha[0] and [osa[0],osa[1]] == pea.location:
            välja = True
            
    pygame.draw.rect(ekraan,[100,0,0],[pea.location[0],pea.location[1],20,20],0) #Näitamine ekraanil(joonistamine peavärvid)
    pygame.draw.rect(ekraan,[100,25,67],[söögi_asetsus[0],söögi_asetsus[1],20,20],0) #Näitamine ekraanil(joonistamine söök, värvid)
    pygame.display.flip()   #Uuendab ekraanil toimuvat


pygame.quit()


