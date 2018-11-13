#SnEEiK!
import pygame
import sys
import random
import time

class madu_uss():
    
    def algne_pos(isend):
        isend.position = [100,40]
        isend.body = [[100,50],[90,50],[80,50]]
        isend.direction = 'paremale'
        isend.changedirectionto = isend.direction
    
    def suunavahetus(isend, suund):
        if suund == 'paremale' and not isend.direction == 'vasakule':
            isend.direction = 'paremale'
            
        if suund == 'vasakule' and not isend.direction == 'paremale':
            isend.direction = 'vasakule'
            
        if suund == 'üles' and not isend.direction == 'alla':
            isend.direction = 'paremale'
            
        if suund == 'alla' and not isend.direction == 'üles':
            isend.direction = 'alla'
        
    def liikumine(isend, söögipositsioon):
        if isend.direction == 'paremale':
            isend.position[0] += 10
        if isend.direction == 'vasakule':
            isend.position[0] -= 10
        if isend.direction == 'üles':
            isend.position[1] += 10
        if isend.direction == 'alla':
            isend.position[1] -= 10
            
        isend.body.insert(0,isend.position)
        
        if isend.position == söögipositsioon:
            return 1
        else:
            isend.body.pop()
            return 0
        
    def kokkupõrge(isend):
        if isend.position[0] > 490 or isend.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for kehaosa in isend.body[1:]:
            if isend.position == kehaosa: 
                return 1
        return 0

    def peapositsioon(isend): #Annab tagasi peapositsiooni väärtuse.
        return isend.position
    
    def kehaosa(isend):
        return isend.position
    

class toit_ilmub():
    def algne_positsioon (isend):
        isend.position = [random.randorange(1, 50) * 10, random.randrange(1, 50) * 10]
        isend.toitEkraanil = True
        
    def ilmuta_toit(isend):
        if isend.toitEkraanil == False:
            isend.position = [random.randorange(1, 50) * 10, random.randrange(1, 50) * 10]
            isend.toitEkraanil = True
            
        return isend.position
    def aseta_toit_ekraanile(isend, koht):
        isend.toitEkraanil = koht
        
        
        
mängu_aken = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ussimäng")
FPS = pygame.time.Clock()

skoor = 0

uss = madu_uss()
toit = toit_ilmub()

def mäng_läbi():
    pygame.quit()
    sys.exit()
while True:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.quit:
            mäng_läbi;
        elif sündmus.type == pygame.KEYDOWN:
            if sündmus.key == pygame.K_RIGHT:
                uss.suunavahetus('paremale')
            if sündmus.key == pygame.K_LEFT:
                uss.suunavahetus('vasakule')
            if sündmus.key == pygame.K_UP:
                uss.suunavahetus('üles')
            if sündmus.key == pygame.K_DOWN:
                uss.suunavahetus('alla')
    toidu_asetus = toit_ilmub.ilmuta_toit()
    if(uss.liikumine(toidu_asetus)==1):
       skoor += 10
       toit_ilmub.aseta_toit_ekraanile(False)
       
    mängu_aken.fill(pygame.color(225, 225, 225))
    for i in uss.kehaosa():
        pygame.draw.rect(mängu_aken, pygame.color(0, 225, 0), pygame.rect(i[0], i[1], 10, 10))
    pygame.draw.rect(mängu_aken, pygame.color(0, 225, 0), pygame.rect(toidu_asetus[0], toidu_asetus[1], 10, 10))
    if(uss.kokkupõrge() == 1):
        mäng_läbi()
    pygame.display.set_caption("Ussimäng | Skoor :" + str(skoor))
    pygame.display.flip()
    FPS.tick(24)