from api.bebida import Bebida
from api.prato import Prato
from api.restaurante import Restaurante
from api.sobremesa import Sobremesa

def main():
    restaurante_praca = Restaurante('praça', 'Gourmet')
    bebida_suco = Bebida('Suco de Laranja',5.00,'500 ml')
    prato_pizza = Prato('Pizza de Peperonni', 25.00, 'Grande')
    sobremesa_doce = Sobremesa('Doce de leite', 8.00, 'Doce', 'Pequeno', 'Doce de leite com cobertura de brigadeiro')
    restaurante_praca.adicionar_no_cardapio(bebida_suco)
    restaurante_praca.adicionar_no_cardapio(prato_pizza)
    restaurante_praca.adicionar_no_cardapio(sobremesa_doce)

    bebida_suco.desconto()
    prato_pizza.desconto()
    sobremesa_doce.desconto()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
    