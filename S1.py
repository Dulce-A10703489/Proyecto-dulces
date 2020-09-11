#Estas serán las otras variables que utilizaré más adelante cuando ya sepa hacer bien las funciones con strings
"""sabor = ('dulce','salado','picante')
textura = ('crujiente', 'chicloso', 'suave', 'duro')
tamaño = ('chico', 'mediano', 'grande')
origen = ('dulce tipico','dulce comercial')"""

#Este será más o menos el formato que seguiré para todas las preguntas, en este caso es únicamente sobre el precio del dulce
#La función busca mostrarle al usuario un resumen de lo que él va eligiendo y así que vaya teniendo una idea del tipo de dulce que se le recomendará
def precio(gasto):
    if gasto <= 0:
        return "Error, el número debe ser mayor a cero"
    
    elif gasto >= 1 and gasto <= 5:
        return "Será un dulce pequeño"
    
    elif gasto >= 6 and gasto <= 10:
        return "Será un dulce mediano"
    
    else:
        return "Puede ser un dulce grande"
        
gasto = float (input("¿Cuántos pesos quieres gastar? "))

print(precio(gasto))

  
    
        


