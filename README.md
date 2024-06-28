# Projeto Pro-Filer

<details>
<summary><strong>🧑‍💻 O que doi desenvolvido:</strong></summary>

Uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

Para executar a aplicação:

1. Crie um [**🏕️ Ambiente Virtual**]
2. Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal;
3. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

```bash
pro-filer . preview
```

![pro-filer preview](./images/pro-filer-preview.gif)

A aplicação já está funcional, mas existiam dois problemas:

1. alguns bugs precisavam ser corrigidos;
2. mais testes precisavam ser implementados.

Foi necessário corrigir os bugs da aplicação e implementar alguns testes! 🧐

</details>

# Pessoas envolvidas no projeto: 🧑‍💻

Eu fui o único desenvolvedor do projeto, porém, a Trybe forneceu a base do projeto, como
Arquivos a serem testados e arquivos propositalmente incompletos e "Bugados" para que fossem feitas as correções

# Arquivos alterados: 📔

⚫ pro_filer/actions/beta_actions.py

⚫ tests/actions/test_show_preview.py

⚫ tests/actions/test_show_details.py

⚫ tests/actions/test_show_disk_usage.py
