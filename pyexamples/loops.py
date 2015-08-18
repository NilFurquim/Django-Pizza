pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'margarita'
    },
    {
        'nome': 'Luigi',
        'sabor': 'portuguesa'
    }
]

for pedido in pedidos:
    s = 'Nome: {0}\nSabor: {1}'
    print(s.format(pedido['nome'], pedido['sabor']))

