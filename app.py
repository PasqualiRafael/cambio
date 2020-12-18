from fractions import Fraction
from code.calculo import converter, converter_to_brl


def run():


    def mostrar(cash, origem, destino, cotacao, result, ratio):
        print(f"{cash} {origem} = {result:.2f} {destino}")
        print(f"{destino} - {ratio} - {origem}")

    def choose():
        print(f"Digite o valor e a sigla da moeda: ")
        print(f"USD | ARS | EUR | BRL | GBP | BTC")

        vo = list(map(str, input().rstrip().lstrip().upper().split(" ")))
        cash = float(vo[0])
        origem = vo[1]

        print(f"Escolha a moeda de conversao: ")
        destino = str(input().upper().strip())

        cotacao = converter_to_brl(origem)        
        cotacao = converter_to_brl(destino)
        

        result, ratio = converter(cash, origem, destino, cotacao)

        mostrar(cash, origem, destino, cotacao, result, ratio)
    
    choose()


if __name__ == "__main__":
    run()
