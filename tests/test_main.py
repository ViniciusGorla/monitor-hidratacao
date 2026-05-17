import requests
from src.main import buscar_temperatura_api


def test_integracao_api_clima():
    """Teste de Integração: Valida se a aplicação consegue se comunicar com a API wttr.in."""
    url = "https://wttr.in/Sao+Paulo?format=j1"

    # Executa a chamada real para o serviço externo
    resposta = requests.get(url, timeout=5)

    # Verifica se a API respondeu com Status 200 OK
    assert resposta.status_code == 200

    # Verifica se o JSON retornado contém as chaves esperadas pela aplicação
    dados = resposta.json()
    assert "current_condition" in dados
    assert "temp_C" in dados["current_condition"][0]


def test_buscar_temperatura_retorna_float():
    """Valida se a nossa função interna trata a resposta da API corretamente retornando um número."""
    temp = buscar_temperatura_api("Sao Paulo")
    assert isinstance(temp, float)