 Automação de Login com Playwright

Este projeto é um exemplo simples de automação de teste usando [Playwright](https://playwright.dev/) em Python. O script realiza um login automático no site [SauceDemo](https://www.saucedemo.com/) e verifica se o login foi bem-sucedido.

O que este projeto faz

- Abre o navegador (modo não headless)
- Acessa a página de login do SauceDemo
- Preenche as credenciais de usuário e senha
- Clica no botão de login
- Verifica se a lista de produtos aparece na tela
- Imprime uma mensagem de sucesso no terminal

 📁 Estrutura dos arquivos

```
📂 automacao-playwright
│
├── test_playwright.py   # Script principal do teste
└── README.md            # Este arquivo
```

 Pré-requisitos

- Python 3.8+
- Playwright instalado

Instalação do Playwright:

```bash
pip install playwright
playwright install
```

Como executar

No terminal, use:

```bash
python "test_playwright.py"
```
 Dica: se o nome da pasta tiver espaços, coloque o caminho entre aspas como no exemplo acima.

 💡 Próximos passos

- Adicionar testes de login inválido
- Automatizar a adição de itens no carrinho
- Medir tempo de carregamento
- Organizar com `pytest`
- Subir em um repositório GitHub público

 🧑‍💻 Autor

**Rogerio**  
Projeto criado para fins de aprendizado e prática com testes automatizados utilizando Playwright.

---

