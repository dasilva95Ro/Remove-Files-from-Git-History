@echo off
REM Carrega variáveis do arquivo .env
for /f %%A in (.env) do set %%A

REM Navega até o diretório do repositório Git
cd %GIT_REPO_PATH%

REM Instala o git-filter-repo via pip
python -m pip install --user git-filter-repo

REM Atualiza o PATH para incluir o diretório do git-filter-repo
set PATH=%PATH%;C:\Users\rodrigo.santos\AppData\Roaming\Python\Python38\Scripts

REM Executa o git-filter-repo para remover os arquivos do histórico
git filter-repo --path %FILES_TO_REMOVE% --invert-paths --force

REM Força o push para o repositório remoto
git push %REMOTE_NAME% --force --all
git push %REMOTE_NAME% --force --tags
