from array import array


lista = [2,0,1,5,323,231323,2112]
qtd_pares = 0
for i in range(len(lista)):
    if lista[i]%2==0:
        qtd_pares += 1
print(qtd_pares)