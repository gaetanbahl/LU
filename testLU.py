#-------------------------------------------------------------------------------
# Name:        Programme SFML pour utiliser LU
# Purpose:
#
# Author:      Timosis
#
# Created:     16/09/2011
# Copyright:   (c) BPCT 2011
# Licence:     CC-BY-SA
#-------------------------------------------------------------------------------

from PySFML import sf
import lu


def main():

    nombreGentils = 100
    nombreMechants = 100

    taillex = 800.0
    tailley = 700.0


    window = sf.RenderWindow(sf.VideoMode(int(taillex),int(tailley)),"Test de LU")
    running = True

    while(running):

        event = sf.Event()
        while window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                running = False

        texte = sf.String()
        terre = lu.Planet(taillex,tailley)

        for i in range(nombreGentils):
            terre.newAnimal(reprod = 0.95,vie = 150)
        for i in range(nombreMechants):
            terre.newAnimal(1,vie = 150)
        terre.newRandomFood(1)
        terre.newRandomFood(0)
        terre.newRandomFood(1)
        terre.newRandomFood(0)

        window.Clear()
        window.Display()
        a = 0
        for i in range(500):
            window.Clear()

            a+=1
            drawlist = terre.round()
            print "ROUND : " + str(a)
            pointList = []

            for t in range(len(drawlist.a)-1):
                if drawlist.d[t] == True:
                    if drawlist.c[t] == 0:
                        rectangle = sf.Shape.Circle(drawlist.a[t],drawlist.b[t],1,sf.Color.Green)

                        pointList.append(rectangle)
                    if drawlist.c[t] == 1:
                        rectangle = sf.Shape.Circle(drawlist.a[t],drawlist.b[t],1,sf.Color.Blue)

                        pointList.append(rectangle)

            for f in pointList:
                window.Draw(f)

            for f in terre.foodList:
                if f.duree > 0:
                    if f.sorte ==0:
                        rectangle = sf.Shape.Circle(f.x,f.y,3,sf.Color.White)
                    if f.sorte ==1:
                        rectangle = sf.Shape.Circle(f.x,f.y,3,sf.Color.Yellow)
                    window.Draw(rectangle)

            texte.SetText(str(terre.nombreAnim))
            texte.SetSize(30)
            window.Draw(texte)


            window.Display()
        running = False
#if __name__ == '__main__':
main()
