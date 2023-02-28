def message_creator(text):
    arts =  {'computadora': 'Con mi computadora puedo programar usando Python', 'celular':'En mi celular puedo aprender usando la app de Platzi','cable':'¡Hay un cable en mi bota!'}
    text in arts.keys()
    try:
        return arts[text]
    except:
        return "Artículo no encontrado"


fff = 'ddsfedf'#agregar palabra del articulo.
response = message_creator(text)
print(response)