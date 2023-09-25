# Remove Files from Git History 🗑️📜

Este projeto contém scripts para remover arquivos específicos do histórico de commits de um repositório Git. Os scripts estão disponíveis em Python e Batch.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Batch](https://img.shields.io/badge/Batch-4B0082?style=for-the-badge&logo=windows&logoColor=white)

## Sistemas Operacionais 🎛️

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Requisitos 📋

* Python 3.8+
* Git instalado e configurado

## Scripts do Projeto 📜

O projeto possui dois scripts com propósitos idênticos, mas em linguagens diferentes:

1. `./remove_files_from_git_history.bat`: Este script é um arquivo Batch para usuários do Windows. Ele remove arquivos específicos do histórico de commits e força o push das alterações para o repositório remoto.

2. `./remove_files_from_git_history.py`: Este script é um arquivo Python que faz a mesma coisa que o arquivo Batch, mas é mais portátil e pode ser executado em diferentes sistemas operacionais.

## Funcionalidades 🎯

* **Identifica** os arquivos a serem removidos do histórico de commits.
* **Utiliza** o `git-filter-repo` para reescrever o histórico de commits.
* **Força** o push das alterações para o repositório remoto.

## Configuração ⚙️

1. Coloque os nomes dos arquivos que você deseja remover no arquivo `.env`.
2. Execute o script correspondente ao seu sistema operacional.

## Como usar o script

1. Salve o script em um diretório de sua escolha.
2. Abra o terminal e navegue até o diretório onde o script foi salvo.
3. Execute o script:
   - Para o script Batch: `remove_files_from_git_history.bat`
   - Para o script Python: `python remove_files_from_git_history.py`

**Criado por Rodrigo Santos**

[![LinkedIn](https://img.icons8.com/nolan/50/linkedin.png)](https://www.linkedin.com/in/rodrigodasilvasantos/) [![GitHub](https://img.icons8.com/nolan/50/github.png)](https://github.com/Rod-Santos)
