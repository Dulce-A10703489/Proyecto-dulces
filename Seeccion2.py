animo=["feliz","triste","enojado","sonriente"]
color= ["blanco", "negro", "azul","amarillo"]
paisaje= ["selva","bosque","playa","ciudad"]
accion= ["leer","escuchar musica","ver la tele","hacer ejercicio"]

#Este también es mi avance 5 porque aquí es como uso las listas en mi proyecto  

decidir= input("¿Quieres saber qué dulce eres? ")
print("¿Cómo te sientes hoy?",animo)
r1=input()
print("¿Qué color prefieres?",color)
r2=input()
print("¿Qué lugar prefieres?",paisaje)
r3=input()
print("¿Qué te gusta más?",accion)
r4=input()

#Aquí estoy usando mi ciclo while para que funcione solamente cuando el usuario sí quiere hacer la encuesta 
#A cada resouesta le estoy dando un valor y dependiendo de la sumatoria de puntos que hagan les dirá un dulce
#El valor máximo de puntos que pueden hacer es 7

def encuesta(r1,r2,r3,r4):
    while (decidir=="si"):
        if (r1 == "feliz" or r1=="sonriente"):
            val1=1
        elif (r1== "triste"):
            val1=0.5
        else:
            val1=0.25
            
        if(r2== "blanco" or r2=="azul"):
            val2=val1+1
        elif (r2=="amarillo"):
            val2=val1+2
        else:
            val2=val1+0.25
            
        if (r3=="playa"):
            val3=val2+2
        elif (r3=="selva" or r3=="bosque"):
            val3=val2+1
        else:
            val3=val2+0.5
            
        if (r4=="leer" or r4=="escuchar musica"):
            val4=val3+ 2
        elif (r4=="ver tele"):
            val4=val3+0.25
        else:
            val4=val3+1
            
        return(val4)
    
print("Tuviste un total de:",encuesta(r1,r2,r3,r4), "puntos y eso quiere decir que...")
 
 
total= encuesta(r1,r2,r3,r4)

if (total >= 2 and total< 3):
    print("¡Eres una Rockaleta!")
elif (total >= 3 and total< 4):
    print("¡Eres unos skwinkles!")
elif (total >= 4 and total< 5):
    print("¡Eres un tamarindo!")
elif (total >= 5 and total< 6):
        print("¡Eres un bombón!")
elif (total >= 6 and total< 7):
        print("¡Eres una paleta de manita!")
elif (total>=7):
    print("¡Eres un mazapán!")
else:
    print ("Error =(")
