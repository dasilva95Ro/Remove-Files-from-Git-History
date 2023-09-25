import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Obtém variáveis do ambiente
git_repo_path = os.getenv("GIT_REPO_PATH")
remote_name = os.getenv("REMOTE_NAME")
files_to_remove = os.getenv("FILES_TO_REMOVE")

# Navega até o diretório do repositório Git
os.chdir(git_repo_path)

# Instala o git-filter-repo via pip
os.system("python -m pip install --user git-filter-repo")

# Executa o git-filter-repo para remover os arquivos do histórico
os.system(f"git filter-repo --path {files_to_remove} --invert-paths --force")

# Força o push para o repositório remoto
os.system(f"git push {remote_name} --force --all")
os.system(f"git push {remote_name} --force --tags")
