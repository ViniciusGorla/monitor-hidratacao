import sys


def calcular_meta_agua(peso: float, clima: str) -> float:
    """Calcula a meta diaria de agua com base no peso e no clima."""
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")

    # Regra base: 35ml por kg
    meta = peso * 35

    # Adicional por clima
    if clima.lower() == "quente":
        meta += 500

    # Retorna em litros
    return meta / 1000


def main():
    print("--- MONITOR DE HIDRATAÇÃO ---")
    try:
        peso = float(input("Digite seu peso em kg: "))
        clima = input("Digite o clima atual (Normal/Quente): ").strip()

        meta = calcular_meta_agua(peso, clima)
        print(f"\nSua meta diaria de hidratacao e: {meta:.2f} Litros.")
    except ValueError as e:
        print(f"\nErro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()