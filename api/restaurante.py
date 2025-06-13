from api.avaliacao import Avaliacao
from api.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._cardapio = []
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status".ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria} | {"Ativo" if cls._ativo else "Inativo"}')


    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'Inativo'
    

    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self,cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)


    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma/quantidade_de_notas, 1)
        return media

    
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao') and hasattr(item,'tamanho'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item.descricao} | Tamanho: {item.tamanho}'
                print(mensagem_sobremesa)
            elif hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item,'tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)

