from cardapio.bebida import Bebida
from cardapio.prato import Prato
from restaurante import Restaurante

def main():
    restaurante_praca = Restaurante('praça', 'Gourmet')
    bebida_suco = Bebida('Suco de Laranja',5.00,'500 ml')
    prato_pizza = Prato('Pizza de Peperonni', 25.00, 'Grande')
    restaurante_praca.adicionar_no_cardapio(bebida_suco)
    restaurante_praca.adicionar_no_cardapio(prato_pizza)

    bebida_suco.desconto()
    prato_pizza.desconto()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
    