def rec(calif, dulce):
    return (calif * 100)/10

dulce= str(input("Nombre del dulce que calificas "))
calif = float(input("¿Qué calificación le das del 1-10? "))

print ("El ", dulce, "es ", rec(calif,dulce),"% recomendado por ti")

def porcentaje(calif):
    if (10>calif>0):
        return True
    else:
        return False
    
print ("caso 1 valor %i, es %r debe ser %r" % (4, porcentaje(4),True))
print ("caso 2 valor %f, es %r debe ser %r" % (8.9, porcentaje(8.9),True))
print ("caso 3 valor %f, es %r debe ser %r" % (9.5, porcentaje(9.5),True))
print ("caso 4 valor %i, es %r debe ser %r" % (80, porcentaje(80),False))
print ("caso 5 valor %i, es %r debe ser %r" % (45, porcentaje(45),False))

