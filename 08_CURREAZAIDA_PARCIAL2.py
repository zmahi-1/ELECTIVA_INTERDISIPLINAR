productos=[
    {"nombre":"Teclado","precio":80000,"cantidad":3},
    {"nombre":"Mouse","precio":50000,"cantidad":5},
    {"nombre":"Monitor","precio":700000,"cantidad":2},
    {"nombre":"Camara","precio":120000,"cantidad":1},

]

def calcular_total(precio,cantidad):
    total=precio*cantidad
    return total
for producto in productos:
    total=calcular_total(producto["precio"],producto["cantidad"])
    producto["total"]=total
    print(producto["nombre"],producto["total"])
if producto["cantidad"]<=2:
    productos.append(bajo_stock)
