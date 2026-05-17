# 💧 Monitor de Hidratação Inteligente

![CI Status](https://github.com/ViniciusGorla/monitor-hidratacao/actions/workflows/ci.yml/badge.svg)

> **Versão:** 1.1.0  
> **Autor:** Vinícius Gorla  
> **Contexto:** Projeto desenvolvido como entrega final para o Bootcamp de Desenvolvimento de Software.

Um aplicativo inteligente focado em saúde que integra lógica de terminal (CLI), consumo de APIs públicas globais e uma interface web moderna de alta usabilidade.

---

## 🌐 Demonstração em Tempo Real

A interface visual do projeto já está compilada, hospedada e disponível publicamente através do **GitHub Pages**. Você pode realizar simulações de cálculo instantaneamente pelo navegador:

👉 **[Acesse o HidraMonitor Web aqui](https://viniciusgorla.github.io/monitor-hidratacao/)**

---

## ⚙️ Arquitetura e Funcionalidades

O projeto foi estruturado para resolver o problema da desidratação diária unindo precisão matemática a dados contextuais do usuário:

* **Cálculo Base Científico:** Automatiza a recomendação padrão de consumo diário utilizando a métrica de 35 ml de água por quilograma de peso corporal.
* **Integração com API de Clima (CLI):** O script em Python realiza requisições HTTP para o serviço global `wttr.in`. Caso a temperatura detectada na cidade informada seja maior que 28°C, o sistema recalcula e eleva dinamicamente a meta em +500 ml.
* **Interface Web Responsiva:** Aplicação Single Page (SPA) em *Dark Mode*, otimizada para dispositivos móveis e desktop, utilizando lógica nativa de eventos javascript.
* **Fluxo Dinâmico de Consumo:** CLI interativa com estruturas de repetição que guiam o usuário no registro fracionado de água até o atingimento da meta de saúde diária.

---

## 🛠️ Stack Tecnológica

| Camada / Escopo | Tecnologia / Ferramenta | Descrição |
| :--- | :--- | :--- |
| **Backend & Core** | Python 3.x | Linguagem estrutural para regras de negócio. |
| **Consumo de APIs** | Requests (HTTP Client) | Comunicação externa com o serviço meteorológico. |
| **Frontend Web** | HTML5 / CSS3 / Vanilla JS | Estrutura semântica e UI responsiva em Dark Mode. |
| **Testes de Software**| Pytest Framework | Suíte de testes unitários para as funções cruciais. |
| **Garantia de Qualidade**| Flake8 (Linting) | Validador estático de boas práticas de código. |
| **Pipeline Automatizado**| GitHub Actions (CI) | Automação de compilação, testes e deploys rápidos. |

---

## 🧪 Suíte de Testes e Qualidade de Código

Para garantir a confiabilidade matemática das rotinas de cálculo do sistema, o projeto conta com cobertura de testes unitários automatizados.

### Executando Testes Locais:
```bash
# Certifique-se de instalar as dependências
pip install -r requirements.txt

# Execute os testes unitários
pytest
