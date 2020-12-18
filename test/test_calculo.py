import pytest
from fractions import Fraction
from code.calculo import converter, converter_to_brl


@pytest.mark.parametrize(
    "cash, origem, destino, expect_result",
    [
        (1, "USD", "BRL", 5.65),
        (1, "ARS", "BRL", 0.07),
        (1, "EUR", "USD", 1.18),
        (1, "GBP", "BRL", 7.24),
        (1, "BTC", "USD", 10700),
        (10, "USD", "GBP", 7.804),
        (5, "BTC", "ARS", 4318214.286)
    ],
)
def test_convert_each_coin(cash, origem, destino, expect_result):
    cotacao = converter_to_brl(origem)
    cotacao = converter_to_brl(destino)
    result, ratio = converter(cash, origem, destino, cotacao)
    result = round(result, 3)

    assert result == expect_result


@pytest.mark.parametrize(
    "cash, origem, destino, expect_ratio",
    [
        (1, "USD", "BRL", Fraction(20, 113)),
        (1, "ARS", "BRL", Fraction(100, 7)),
        (1, "EUR", "USD", Fraction(50, 59)),
        (1, "GBP", "BRL", Fraction(25, 181)),
        (1, "BTC", "USD", Fraction(1, 10700)),
        (10, "USD", "GBP", Fraction(724, 565)),
        (5, "BTC", "ARS", Fraction(1, 863643))
    ],
)
def test_ratio_convert_each_coin(cash, origem, destino, expect_ratio):
    cotacao = converter_to_brl(origem)
    cotacao = converter_to_brl(destino)
    result, ratio = converter(cash, origem, destino, cotacao)

    assert ratio == expect_ratio


@pytest.mark.parametrize(
    "cash, origem, destino, expect_result",
    [
        (1, "BRL", "BRL", 1),
        (1, "USD", "BRL", 5.65),
        (1, "ARS", "BRL", 0.07),
        (1, "EUR", "BRL", 6.667),
        (1, "GBP", "BRL", 7.24),
        (1, "BTC", "BRL", 60455)
    ],
)
def test_convert_to_brl(cash, origem, destino, expect_result):
    cotacao = converter_to_brl(origem)
    cotacao = converter_to_brl(destino)
    result, ratio = converter(cash, origem, destino, cotacao)
    result = round(result, 3)

    assert result == expect_result


@pytest.mark.parametrize(
    "cash, origem, destino, expect_result",
    [
        (1, "BRL", "BRL", 1),
        (1, "BRL", "USD", 0.177),
        (1, "BRL", "ARS", 14.286),
        (1, "BRL", "EUR", 0.15),
        (1, "BRL", "GBP", 0.138),
        (1, "BRL", "BTC", "1.654e-05"),
    ],
)
def test_convert_brl_to_each_type(cash, origem, destino, expect_result):
    cotacao = converter_to_brl(origem)
    cotacao = converter_to_brl(destino)
    result, ratio = converter(cash, origem, destino, cotacao)

    if destino != "BTC":
        result = round(result, 3)
    else:
        result = f"{result:.3e}"

    assert result == expect_result
