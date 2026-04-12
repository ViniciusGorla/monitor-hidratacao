import pytest
import sys
import os

# Truque para a pasta 'src' ser encontrada
caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(caminho)

from main import calcular_meta, registrar_agua  # noqa: E402


def test_calcular_meta_caminho_feliz():
    """Testa o calculo da meta para um peso normal."""
    assert calcular_meta(70) == 2.45


def test_calcular_meta_peso_invalido():
    """Testa erro ao receber peso zero ou negativo."""
    with pytest.raises(ValueError, match="O peso deve ser maior que zero."):
        calcular_meta(0)


def test_registrar_agua_soma_correta():
    """Testa se a soma da agua bebida esta correta."""
    consumido_atual = 1.0
    bebido_agora = 0.5
    assert registrar_agua(consumido_atual, bebido_agora) == 1.5


def test_registrar_agua_quantidade_invalida():
    """Testa o bloqueio de quantidade negativa de agua."""
    with pytest.raises(ValueError):
        registrar_agua(1.0, -0.2)
