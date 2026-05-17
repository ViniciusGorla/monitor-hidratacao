import requests


def calcular_meta(peso: float) -> float:
    """Calcula a meta de agua diaria (35ml por kg)."""
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    return peso * 0.035


def buscar_temperatura_api(cidade: str) -> float:
    """Busca a temperatura atual de uma cidade usando a API pública wttr.in."""
    try:
        # Substitui espaços por '+' para a URL não quebrar
        cidade_formatada = cidade.replace(" ", "+")
        url = f"https://wttr.in/{cidade_formatada}?format=j1"

        # Faz a requisição GET para a API externa (Timeout de 5 segundos)
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()
            # Extrai a temperatura em graus Celsius de dentro do JSON
            temp_c = float(dados["current_condition"][0]["temp_C"])
            return temp_c
        return 25.0  # Temperatura padrão caso a API falhe
    except Exception:
        return 25.0  # Temperatura padrão caso dê erro de conexão


def registrar_agua(consumido: float, quantidade: float) -> float:
    """Adiciona a quantidade de agua bebida ao total consumido."""
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    return consumido + quantity


def interface_cli():
    """Interface de Linha de Comando (CLI)."""
    print("-" * 40)
    print("Bem-vindo ao Monitor de Hidratacao Inteligente")
    print("-" * 40)

    try:
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))
        meta = calcular_meta(peso)

        # NOVO: Integração com a API Pública de Clima
        cidade = input(
            "Digite sua cidade para verificar o clima (ex: Sao Paulo): "
        )
        print("\nBuscando dados climáticos na nuvem...")
        temp = buscar_temperatura_api(cidade)

        print(f"Temperatura atual em {cidade}: {temp}°C")

        # Regra de negócio com base na API externa
        if temp > 28.0:
            meta += 0.50  # Adiciona 500ml na meta se estiver calor
            print(
                "⚠️ Está muito calor hoje! Sua meta foi aumentada em 0.50L para evitar desidratação."
            )

        print(f"\nSua meta diaria final e de {meta:.2f} litros de agua.")

        consumido = 0.0
        while consumido < meta:
            print(f"\nStatus: Voce ja bebeu {consumido:.2f}L de {meta:.2f}L.")
            msg = "Quantos litros voce bebeu agora? (ex: 0.25): "
            bebido = float(input(msg))
            consumido = registrar_agua(consumido, bebido)

            if consumido >= meta:
                print(f"\nPARABENS! Atingiu sua meta de {meta:.2f}L!")
                print("Continue assim para cuidar da sua saude!\n")
                break

    except ValueError:
        msg_erro = "\nErro: Entrada invalida. Digite numeros."
        print(msg_erro)


if __name__ == "__main__":
    interface_cli()