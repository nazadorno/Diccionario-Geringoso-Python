# 2.14 diccionario_geringoso.py

lista = ['banana', 'manzana', 'mandarina']

def diccionario_geringoso(lista):

    geringosas = {}
    
    for cadena in lista:
        capadepenapa = ''

        for c in cadena:
            if c in 'aeiou': 
                capadepenapa = capadepenapa + c + 'p' + c 
            else:
                capadepenapa = capadepenapa + c           
        
            geringosas[cadena] = capadepenapa
    
    for k in geringosas:
        print(k, '=', geringosas[k])


diccionario_geringoso(lista)





