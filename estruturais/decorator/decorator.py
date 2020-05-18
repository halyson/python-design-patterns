def LogItem(metodo):
    def wrapper(self, item):
        print('Item Adicionado')
        return metodo(self, item)

    return wrapper


def TotalizarItem(function):
    def wrapper(self, item):
        print('Item Totalizado')
        self.quantidade_itens = self.quantidade_itens + item.quantidade
        return function(self, item)

    return wrapper


class Item:
    def __init__(self, codigo, valor, quantide):
        self.codigo = codigo
        self.valor = valor
        self.quantidade = quantide


class Carrinho:
    def __init__(self):
        self.quantidade_itens = 0
        self.valor_total = 0
        self.itens = []

    @LogItem
    @TotalizarItem
    def adicionar_item(self, item):
        self.itens.append(item)


carrinho = Carrinho()
item_1 = Item(10, 150, 2)
item_2 = Item(5, 100, 1)

# Sempre que adicionar um item ao carrinho os decorators LogItem e TotalizarItem serao executados
carrinho.adicionar_item(item_1)
carrinho.adicionar_item(item_2)


print(f'Total de Itens: {carrinho.quantidade_itens}')
