# Decorator

Ao utilizar o design pattern decorator, podemos compor/decorar os parâmetros de forma dinâmica.
Neste exemplo, sempre que adicionar um item no carrinho ele temos um decorator que vai gerar um log e outro que vai totalizar a quantidade de itens do carrinho.

## Quando usar?

> Sempre que percebemos que temos comportamentos que podem ser formados por comportamentos de outras classes envolvidas em uma mesma hierarquia.

## Decorator do Python

Ao utilizar o recurso de decorator da linguagem Python, podemos chamar outra função ou método (neste caso o wrapper do nome_decorator) antes de executar uma função ou método, e assim compor os resultados.

A diferença entre o design pattern decorator e o decorator do Python é que o decorator do Python fica "fixo" no código, já o design pattern decorator, podemos compor os decorators em tempo de execução.

```python
def nome_decorator(metodo_ou_funcao):
    def wrapper(self, valor):
        return metodo_ou_funcao(self, valor) + 10
    return wrapper


class Teste(Parametro):

    @nome_decorator
    def calcula_valor(self, valor):

        return teste.valor + self.calcula_outro_valor(valor)
```
