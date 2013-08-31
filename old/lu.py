#-------------------------------------------------------------------------------
# Name:        Life Unit
# Purpose:     Simulation de vie dans un univers restreint
#
# Author:      Timosis
#
# Created:     15/09/2011
# Copyright:   (c) BPCT 2011
# Licence:     CC-BY-SA
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import math,random


class Espece:

    def __init__(self,x,y,espece,deplacement,portee,reprod,vie):
        self.x=x
        self.y=y
        self.espece=espece
        self.deplacement=deplacement
        self.portee=portee
        self.reprod=reprod
        self.vie=vie
        self.faim=100
        self.resistance=10
        self.alive=True

    def move(self):
        deplacement = self.deplacement
        moinsdeplacement = deplacement * (-1)
        self.x = self.x + random.randrange(moinsdeplacement,deplacement)
        self.y = self.y + random.randrange(moinsdeplacement,deplacement)

    def moveToFood(self,coord):
        depl = self.deplacement

        distx = coord[0] - self.x
        disty = coord[1] - self.y

        self.x = self.x + (distx/depl)
        self.y = self.y + disty/depl


class Food:

    def __init__(self,x,y,duty,sort):
        self.duree = duty
        self.sorte = sort
        self.x=x
        self.y=y

class Planet:
    def __init__(self,sizeX,sizeY):
        self.sizeX= sizeX
        self.sizeY= sizeY
        self.animalList = []
        self.foodList = []
        self.speciesList = []
        self.nombreAnim = 0

        print "Monde cree"

    def newAnimal(self,espece=0,deplacement=10,portee=5,reprod=0.50,vie=40):

        x=random.randrange(0,self.sizeX)
        y=random.randrange(0,self.sizeY)
        animal = Espece(x,y,espece,deplacement,portee,reprod,vie)
        self.animalList.append(animal)
        print "animal spawned"
        self.plusPop()

    def newFood(self,x=0,y=0,duree=100,sorte=0):
        nourriture=Food(x,y,duree,sorte)
        self.foodList.append(nourriture)

    def newRandomFood(self,sorte,duree=10000000):
        x = random.randrange(0,self.sizeX)
        y = random.randrange(0,self.sizeY)
        self.newFood(x,y,duree,sorte)

    def plusPop(self):
        self.nombreAnim+=1
        print self.nombreAnim

    def moinsPop(self):
        self.nombreAnim -= 1
        print self.nombreAnim

    def round(self):
        toDraw = Abc()
        longueur,a = len(self.animalList),0
        for animal in self.animalList:
            if a > longueur:
                break
            toDraw.add(animal.x,animal.y,animal.espece,animal.alive)

            if animal.alive == True:

                if animal.faim < 20:
                    nourriture = self.findFood(animal.x,animal.y,animal.espece)
                    animal.moveToFood(nourriture)
                else:
                    animal.move()
                #print "MOVED"

                for other in self.animalList:
                    rangeplus=animal.portee
                    rangemoins=animal.portee * (-1)

                    if other.x < rangeplus+animal.x and other.x > rangemoins+animal.x:
                        if other.y < rangeplus+animal.y and other.y > rangemoins+animal.y:
                            if other.x != animal.x and other.y != animal.y:
                                if other.espece == animal.espece:
                                    if animal.faim > 40:
                                        if random.random() < animal.reprod:
                                            print "REPRODUCTION !"
                                            self.newAnimal(animal.espece,animal.deplacement,animal.portee,animal.reprod,animal.vie)
                                        else:
                                            print "FAIL REPRODUCTION"
                                else:
                                    if other.espece > animal.espece:
                                        animal.alive = False
                                        print "TUE PAR AUTRE ESPECE"
                                        self.moinsPop()
                                        break

                for food in self.foodList:
                    if food.x < rangeplus+animal.x and food.x > rangemoins+animal.x:
                        if food.y < rangeplus+animal.y and food.y > rangemoins+animal.y:
                            if food.duree > 0:
                                animal.faim = 100
                                print "ANIMAL A MANGE"
                                food.duree -= 1
                animal.vie -= 1
                if animal.faim <= 0:
                    animal.vie -= 1
                    print 'FAIM !'
                animal.faim -= 1
                if animal.vie == 0:
                    animal.alive = False
                    print "MORT DE VIEILLESSE"
                    self.moinsPop()

            a+=1

        return toDraw

    def findFood(self,animalx,animaly,espece):
        dist=math.sqrt((animalx-self.foodList[0].x)**2 + (animaly-self.foodList[0].y)**2)
        x=self.foodList[0].x
        y=self.foodList[0].y

        for i in self.foodList:
            if i.duree >0 and espece == i.sorte:
                if math.sqrt((animalx-i.x)**2 + (animaly - i.y)**2) < dist:
                    dist= math.sqrt((animalx-i.x)**2 + (animaly - i.y)**2)
                    x = i.x
                    y = i.y

        liste = [x,y,dist]
        return liste


class Abc:

    def __init__(self):
        self.a = []
        self.b = []
        self.c = []
        self.d = []

    def add(self,a,b,c,d):
        self.a.append(a)
        self.b.append(b)
        self.c.append(c)
        self.d.append(d)


def main():
    terre = Planet(80.0,80.0)
    for i in range(50):
        terre.newAnimal()
    for i in range(50):
        terre.newAnimal(1)

    a = 0
    for i in range(100):
        a+=1
        terre.round()
        print "ROUND : " + str(a)

if __name__ == '__main__':
    main()
