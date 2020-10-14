"""
PROYECTO DULCES
El programa tiene 3 secciones, en la primera puedes hacer un test que te recomienda un dulce,
la segunda te dice qué dulce eres y la tercera muestra un porcentaje de recomendación 
de cada dulce que el usuario guarda
"""

"""
========================= funciones de preguntas ===========================================
"""
#Seccion 1 preguntas 
def dulce(pregunta):
    """
    (funciones, listas, ciclos, condicionales)
    Cuando el usuario decide un sabor dulce,
    se le recomiendan ciertos dulces de acuerdo 
    a la textura que prefiere
    """
    i=0
    if (pregunta[i]!=sabor[i]):
        return False
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
    """
    (funciones, listas, ciclos, condicionales)
    Cuando el usuario decide un sabor salado,
    se le recomiendan ciertos dulces de acuerdo 
    a la textura que prefiere
    """
    i=0
    if (pregunta[i]!=sabor[1]):
        return False
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
    """
    (funciones, listas, ciclos, condicionales)
    Cuando el usuario decide un sabor picante,
    se le recomiendan ciertos dulces de acuerdo 
    a la textura que prefiere
    """
    i=0
    if (pregunta[i]!=sabor[2]):
        return False
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
    """
    (funciones, listas, ciclos, condicionales)
    Cuando el usuario decide de tamaño chico,
    se le recomiendan ciertos dulces de acuerdo 
    al precio que gusta pagar
    """
    i=2
    if (pregunta[i] != "chico"):
        return False 
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
    """
    (funciones, listas, ciclos, condicionales)
    Cuando el usuario decide de tamaño mediano,
    se le recomiendan ciertos dulces de acuerdo 
    al precio que gusta pagar
    """
    i=2
    if (pregunta[i] != "mediano"):
        return False 
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
    """
    (funciones, listas, ciclos, condicionales)
    Cuando el usuario decide de tamaño grande,
    se le recomiendan ciertos dulces de acuerdo 
    al precio que gusta pagar
    """
    i=2
    if (pregunta[i] != "grande"):
        return False 
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
    
def imprime_1 (sabores):
    i=0
    for arg in sabores:
        if arg == False:
            print (" ")
        else:
            return arg
        i=i+1
        
def imprime_2 (tamaños):
    i=0
    for arg in tamaños:
        if arg == False:
            print (" ")
        else:
            return arg
        i=i+1

#Seccion 2 preguntas
def primera(resp):
    """
    (funciones, listas, ciclos, condicionales, operadores)
    Cuando la respuesta del usuario, que se va guardando en "resp",
    es igual a una de las opciones de la lista animo, se le otorga
    cierto valor que se guarda en el acumulador "acum" que en este 
    momento inicia en cero 
    """
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
    """
    (funciones, listas, ciclos, condicionales, operadores)
    Cuando la respuesta del usuario, que se va guardando en "resp",
    es igual a una de las opciones de la lista color, se le otorga
    cierto valor que se guarda en el acumulador "acum" que en este 
    caso inicia con el valor de la función anterior 
    """
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
    """
    (funciones, listas, ciclos, condicionales, operadores)
    Cuando la respuesta del usuario, que se va guardando en "resp",
    es igual a una de las opciones de la lista paisaje, se le otorga
    cierto valor que se guarda en el acumulador "acum", en este 
    momento inicia con el valor de la función anterior 
    """
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
    """
    (funciones, listas, ciclos, condicionales, operadores)
    Cuando la respuesta del usuario, que se va guardando en "resp",
    es igual a una de las opciones de la lista paisaje, se le otorga
    cierto valor que se guarda en el acumulador "acum", igualmente, 
    en este momento inicia con el valor de la función anterior 
    """
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
    """
    (condicionales, funciones)
    Esta funcion ayuda a designar el dulce 
    dependiendo del total que se obtuvo
    al contestar las preguntas anteriores
    """
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
def recomienda(calif, dulce):
    """
    (Uso de operadores, uso de funcioes)
    El usuario define el dulce que califica
    y la calificacion que le otorga, esto 
    devuelve el porcentaje de recomendacion
    de su parte 
    """
    while (calif>0):
        if (calif>=1 and calif<=10):
            
            calif=calif*100/10
            return calif
        else:
            return "Error"
"""
================= parte principal del programa ============================
"""

#Listas usadas para las opciones a las preguntas 
"""
Listas que indican las opciones en 
la seccion 1
""" 
sabor =['dulce','salado','picante']
textura =['chicloso', 'suave', 'duro']
tamaño =['chico', 'mediano', 'grande']
"""
Listas que funcionan como opciones
de la seccion 2
"""
animo=["feliz","triste","enojado","sonriente"]
color= ["blanco", "negro", "azul","amarillo"]
paisaje= ["selva","bosque","playa","ciudad"]
accion= ["leer","musica","television","deportes"]


#Preguntas de la seccion 1 y respuestas del usuario 
print("¿Qué prefieres?", sabor)
p1=input()
print("¿Qué textura te gusta más?",textura)
p2= input()
print("De qué tamaño prefieres tu dulce?",tamaño)
p3=input()
print("¿Cuántos pesos quieres gastar? ")
p4 = float (input())

pregunta= [p1,p2,p3,p4]
sabores=dulce(pregunta),salado(pregunta),picante(pregunta)
tamaños=chico(pregunta),mediano(pregunta),grande(pregunta)

print("Puedes comprar: ",imprime_1(sabores),imprime_2(tamaños))

#Preguntas de la seccion 2 y las respuestas del usuario
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

#Preguntas de la seccion 3 y respuestas del usuario 
dulce= str(input("Nombre del dulce que calificas "))
calif = float(input("¿Qué calificación le das del 1-10? "))
print ("El ", dulce, "es ", recomienda(calif,dulce),"% recomendado por ti")
