from classes import *
def main():
    pix = Pix()
    cartao = CartaoCredito()
    boleto = Boleto()

    finalizar_compra(pix, 1500)
    finalizar_compra(cartao, 9540.84)
    finalizar_compra(boleto, 439.23)

if __name__ == '__main__':
    main()