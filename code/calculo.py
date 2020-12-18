from fractions import Fraction
from .constants import BRL


cotacao = dict()


def converter_to_brl(coin):
    if coin == "BRL":
        cotacao["BRL"] = 1

    elif coin == "USD":
        cotacao["USD"] = BRL

    elif coin == "ARS":
        cotacao["ARS"] = 0.07

    elif coin == "EUR":
        cotacao["EUR"] = BRL * 1.18

    elif coin == "GBP":
        cotacao["GBP"] = 7.24

    elif coin == "BTC":
        cotacao["BTC"] = BRL * 10700

    return cotacao


def converter(cash, origem, destino, cotacao):

    result = (cash * cotacao[origem]) / cotacao[destino]

    ratio = Fraction(cotacao[destino] / cotacao[origem]).limit_denominator()

    return result, ratio


if __name__ == "__main__":
    pass

