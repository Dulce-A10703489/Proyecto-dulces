"""
El programa tiene 3 secciones, en la primera puedes hacer un test que te recomienda un dulce,
la segunda te dice qué dulce eres y la tercera muestra un porcentaje de recomendación 
de cada dulce que el usuario guarda
"""

#Seccion 1 preguntas 
def dulce(pregunta):
    i=0
    while (pregunta[i]==sabor[i]):
        if (p2==textura[i]):
            regresa=["gomitas","chicles","sugus"]
        i=i+1
        if(p2==textura[i]):
            regresa=["chocolate","bombones","mazapan"]
        i=i+1
        if (p2==textura[i]):
            regresa=["Halls","paleta de caramelo","tic tac"]
        return regresa

def salado (pregunta):
    i=0
    while (pregunta[i]==sabor[1]):
        if (p2==textura[i]):
            regresa=["chicles de menta","aciditos","mentos"]
        i=i+1
        if(p2==textura[i]):
            regresa=["pepitas","palomitas","nachos"]
        i=i+1
        if (p2==textura[i]):
            regresa=["cacahuates","churritos","papas"]
        return regresa

def picante(pregunta):
    i=0
    while (pregunta[i]==sabor[2]):
        if (p2==textura[i]):
            regresa=["skwinkles","pulparindo","picafresa"]
        i=i+1
        if(p2==textura[i]):
            regresa=["pelon pelo rico ","lucas muecas","tama-roca(banderilla)"]
        i=i+1
        if (p2==textura[i]):
            regresa=["paleta de chile","tamborines","pelon pelonetes"]
        return regresa
    
def chico (pregunta):
    i=2
    while (pregunta[i]=="chico"):
        if (p4 <= 0):
            return "Error, el número debe ser mayor que cero"
        elif(p4 >= 1 and p4 <= 5):
            regresa=["chicles individuales","paletas","caramelos"]
        elif(p4 >= 6 and p4 <= 10):
            regresa=["dulces tipicos","pastillitas", "dulces canel\'s"]
        else:
            regresa=["mayor cantidad de dulces pequeños","dulces a granel"]
        return regresa
    
def mediano (pregunta):
    i=2
    while (pregunta[i]=="mediano"):
        if (p4 <= 0):
            return "Error, el número debe ser mayor que cero"
        elif(p4 >= 1 and p4 <= 5):
            regresa=["dulces de la rosa","dulces vero"]
        elif(p4 >= 6 and p4 <= 10):
            regresa=["dulces chupa chups","dulces ricolino"]
        else:
            regresa=["dulces wonka", "dulces lucky gummy\'s", "dulces lucas"]
        return regresa

def grande (pregunta):
    i=2
    while (pregunta[i]=="grande"):
        if (p4 <= 0):
            return "Error, el número debe ser mayor que cero"
        elif (p4 >= 1 and p4 <= 5):
            regresa=["dulces duvalin","dulces tutsi"]
        elif(p4 >= 6 and p4 <= 10):
            regresa=["dulces twix","dulces barcel","dulces marinela"]
        else:
            regresa=["dulces Haribo","dulces pringles","dulces kinder"]
        return regresa

#Seccion 2 preguntas
def primera(resp):
    acum=0
    i=0
    for resp in animo[i]:
        if (r1==animo[i] or r1==animo[1]):
            acum=1
        i=i+2
        if(r1==animo[i]):
            acum= 0.5
        i=i+1
        if (r1==animo[i]):
            acum=0.25
        return acum
    
def segunda(resp):
    acum=primera(resp)
    i=0
    for resp in color[i]:
        if (r2==color[i] or r2==color[1]):
            acum=acum+1
        i=i+2
        if (r2==color[i]):
            acum= acum+2
        i=i+1
        if(r2==color[i]):
            acum=acum+0.25
        return acum

def tercera(resp):
    acum=segunda(resp)
    i=0
    for reso in paisaje[i]:
        if (r3==paisaje[i] or r3==paisaje[1]):
            acum=acum+1
        i=i+2
        if(r3==paisaje[i]):
            acum= acum+2
        i=i+1
        if(r3==paisaje[i]):
            acum=acum+0.25
        return acum

def cuarta(resp):
    acum=tercera(resp)
    i=0
    for resp in accion[i]:
        if(r4==accion[i] or r4==accion[1]):
            acum=acum+2
        i=i+2
        if(r4==accion[i]):
            acum= acum+0.25
        i=i+1
        if(r4==accion[i]):
            acum=acum+1
        return acum

def regresa(total):
    if (total >= 2 and total< 3):
        return "¡Eres una Rockaleta!"
    elif (total >= 3 and total< 4):
        return "¡Eres unos skwinkles!"
    elif (total >= 4 and total< 5):
        return"¡Eres un tamarindo!"
    elif (total >= 5 and total< 6):
        return "¡Eres un bombón!"
    elif (total >= 6 and total< 7):
        return("¡Eres una paleta de manita!")
    elif (total>=7):
        return "¡Eres un mazapán!"
    else:
        return "Error =("

#Seccion 3 preguntas 
def rec(calif, dulce):
    while (calif>0):
        if (calif>=1 and calif<=10):
            calif=calif*100/10
            return calif
        else:
            return "Error"

#Listas usadas para las opciones a las preguntas  
sabor =['dulce','salado','picante']
textura =['chicloso', 'suave', 'duro']
tamaño =['chico', 'mediano', 'grande']
animo=["feliz","triste","enojado","sonriente"]
color= ["blanco", "negro", "azul","amarillo"]
paisaje= ["selva","bosque","playa","ciudad"]
accion= ["leer","musica","television","deportes"]

#Seccion 1 preguntas
print("¿Qué prefieres?", sabor)
p1=input()
print("¿Qué textura te gusta más?",textura)
p2= input()
print("De qué tamaño prefieres tu dulce?",tamaño)
p3=input()
print("¿Cuántos pesos quieres gastar? ")
p4 = float (input())

pregunta= [p1,p2,p3,p4]

listas=dulce(pregunta),salado(pregunta),picante(pregunta),chico(pregunta),mediano(pregunta),grande(pregunta)

print("Puedes comprar: ",listas)



#Seccion 2 preguntas
print ("¿Cómo te sientes hoy?",animo)
r1=input()
print("¿Qué color prefieres?",color)
r2=input()
print("¿Qué lugar prefieres?",paisaje)
r3=input()
print("¿Qué prefieres?",accion)
r4=input()

resp=[r1,r2,r3,r4]
total= cuarta(resp)

print("Tuviste un total de:",total, "puntos y eso quiere decir que...")
print (regresa(total))


#Seccion 3 preguntas
dulce= str(input("Nombre del dulce que calificas "))
calif = float(input("¿Qué calificación le das del 1-10? "))
print ("El ", dulce, "es ", rec(calif,dulce),"% recomendado por ti")


