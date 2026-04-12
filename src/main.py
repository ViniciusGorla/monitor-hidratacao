def calcular_meta(peso: float) -> float:
    """Calcula a meta de agua diaria (35ml por kg)."""
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    return peso * 0.035


def registrar_agua(consumido: float, quantidade: float) -> float:
    """Adiciona a quantidade de agua bebida ao total consumido."""
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    return consumido + quantidade


def interface_cli():
    """Interface de Linha de Comando (CLI)."""
    print("-" * 40)
    print("Bem-vindo ao Monitor de Hidratacao")
    print("-" * 40)

    try:
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))
        meta = calcular_meta(peso)
        print(f"\nSua meta diaria e de {meta:.2f} litros de agua.")

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
