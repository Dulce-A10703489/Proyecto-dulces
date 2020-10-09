sabor = ['dulce','salado','picante']
textura = ['chicloso', 'suave', 'duro']
tamaño = ['chico', 'mediano', 'grande']

print("¿Qué prefieres?", sabor)
p1=input()
print("¿Qué textura te gusta más?",textura)
p2= input()
print("De qué tamaño prefieres tu dulce?",tamaño)
p3=input()
print("¿Cuántos pesos quieres gastar? ")
p4 = float (input())

def sabor_textura (p1,p2):
    if(p1=="dulce"):
        if (p2=="chicloso"):
            rec=["gomitas","chicles","sugus"]
        elif (p2=="suave"):
            rec=["chocolate","bombones","mazapan"]
        else:
            rec=["Halls","paleta de caramelo","tic tac"]
        p1="nada"
            
    if(p1=="salado"):
        if (p2=="chicloso"):
            rec=["chicles de menta","aciditos","mentos"]
        elif (p2=="suave"):
            rec=["pepitas","palomitas","nachos"]
        else:
            rec=["cacahuates","churritos","papas"]
            
    if(p1=="picante"):
        if (p2=="chicloso"):
            rec=["skwinkles","pulparindo","picafresa"]
        elif (p2=="suave"):
            rec=["pelon pelo rico ","lucas muecas","tama-roca(banderilla)"]
        else:
            rec=["paleta de chile","tamborines","pelon pelonetes"]
    
    return (rec)

        
    
def tamaño_precio(p3,p4):
    if (p3=="chico"):
        if (p4 <= 0):
            return "Error, el número debe ser mayor que cero"
        elif (p4 >= 1 and p4 <= 5):
            rec2=["chicles individuales","paletas","caramelos"]
        elif (p4 >= 6 and p4 <= 10):
            rec2=["dulces tipicos","pastillitas", "dulces canel\'s"]
        else:
            rec2=["mayor cantidad de dulces pequeños","dulces a granel"]
            
    if(p3=="mediano"):
        if (p4 <= 0):
            return "Error, el número debe ser mayor que cero"
        elif (p4 >= 1 and p4 <= 5):
            rec2=["dulces de la rosa","dulces vero"]
        elif (p4 >= 6 and p4 <= 10):
            rec2=["dulces chupa chups","dulces ricolino"]
        else:
            rec2=["dulces wonka", "dulces lucky gummy\'s", "dulces lucas"]
            
    if (p3=="grande"):
        if (p4 <= 0):
            return "Error, el número debe ser mayor que cero"
        elif (p4 >= 1 and p4 <= 5):
            rec2=["dulces duvalin","dulces tutsi"]
        elif (p4 >= 6 and p4 <= 10):
            rec2=["dulces twix","dulces barcel","dulces marinela"]
        else:
            rec2=["dulces Haribo","dulces pringles","dulces kinder"]
    
    return (rec2)

#Al momento de imprimir estas dos funciones, es como si le estuviera dando una lista anidada al usuario,ya que muestra dos listas. 
primera = sabor_textura(p1,p2)
segunda = tamaño_precio(p3,p4)

print("Puedes comprar: ",primera,segunda)





            
            
        
        
        
        
        
    
