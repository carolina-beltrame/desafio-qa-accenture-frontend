Desafio de Automação Front-End

Este projeto automatiza e valida o fluxo de testes frontend de um site. Ele utiliza o padrão Page Object Model e dados dinâmicos para garantir que os testes sejam robustos e confiáveis.

Tecnologias Utilizadas
  - Python: Linguagem principal.
  - Selenium: Biblioteca para automação web.
  - Pytest: Framework de testes.
  - WebDriver-manager: Gerencia e atualiza o driver do navegador.
  - Faker: Geração de dados de teste dinâmicos.

Requisitos Alcançados
  - Web Tables:
    - Navega para a página de Web Tables.
    - Cria, edita e deleta um novo registro.

  - Browser Windows:
    - Navega para a página de janelas.
    - Abre uma nova janela, valida a mensagem "This is a sample page" e a fecha.

  - Progress Bar:
    - Navega para a página da barra de progresso.
    - Inicia a barra, para-a antes de 25% e valida o valor.
    - Inicia novamente a barra, espera chegar a 100% e a reseta.

  - Sortable:
    - Navega para a página de ordenação.
    - Usando drag and drop, ordena os elementos de forma decrescente e, em seguida, em ordem crescente.

  - Practice Form:
    - Navega para a página do formulário.
    - Preenche todos os campos com dados aleatórios, faz o upload de um arquivo, submete o formulário e valida que um pop-up é exibido.

Para Rodar

  - Instale as dependências: pip install -r requirements.txt
  - Rode os testes: pytest -s 
