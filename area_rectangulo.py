#funcion area
def area_rectangulo (base,altura):
    area_rec= base*altura
    return area_rec
#programa Principal

base= 5
altura= 10
area= area_rectangulo (base,altura)

print("El area del rectangulo es: ",area)
