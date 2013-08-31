#simulateur de vie
import pickle,math

BOXWIDTH = 10
BOXHEIGHT = 10

box = BOXWIDTH *[0]
for i in range(len(box)):	box[i] = BOXHEIGHT*[0]
f = open("boite",'w')
pickle.dump(box,f)
f.close()

anim = [[],[]]
miam = [[],[]]


def changeItem(liste,y,x,etat):
    liste[x][y] = etat
    return liste

def addItem(liste,x,y):
    liste[0].append(x)
    liste[1].append(y)
    return liste

def closestMiam(y,x,mi):
    coord = [mi[0][1],mi[1][1]]
    
    for i in range(0,len(mi[0])-1):
        if math.sqrt((coord[0]-x)*(coord[0]-x) + (coord[1]-y)*(coord[1]-y)) > math.sqrt((mi[0][i]-x)*(mi[0][i]-x) + (mi[1][i]-y)*(mi[1][i]-y)):
            coord[0],coord[1] = mi[0][i],mi[1][i]       
    return coord

def afficher(boite):
    for i in boite:
        string = ""
        for t in i:
            string += str(t)
        print string

def analyser(box):
    global anim
    global miam
    x,y=0,0
    for ligne in box:
        y = 0
        for item in ligne:
        
            if item == 1:
                
                anim = addItem(anim,x,y)
            elif item == 2:
                miam = addItem(miam,x,y)
            y+=1
        x+=1
       
def findMove(ya,xa,ym,xm):
    distx,disty = 0,0
    direction = ""
    
    if xa >= xm:
        distx = xa - xm
    else:
        distx = xm - xa
    if ya >= ym:
        disty = ya - ym
    else:
        disty = ym - ya

    if distx >= disty:
        if xa >= xm:
            direction = "left"
        else:
            direction = "right"
    else:
        if ya >= ym:
            direction = "up"
        else:
            direction = "down"

    return direction


box = changeItem(box,4,6,1)
box = changeItem(box,4,5,2)
box = changeItem(box,8,7,2)


analyser(box)

 
#print box
print anim
print miam
afficher(box)
closest = closestMiam(anim[0][0],anim[1][0],miam)
print closest
print findMove(anim[0][0],anim[1][0],closest[0],closest[1])
