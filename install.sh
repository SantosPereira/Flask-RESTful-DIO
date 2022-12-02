# Criação do ambiente virtual
python3 -m venv env

# Ativação do ambiente:
# Windows
.\/env/Scripts/Activate.ps1

# Linux/Mac
source ./env/bin/activate

# Instalação das dependências do projeto
pip install -r requirements.txt

# Fazendo as migrations do banco de dados
python3 ./src/util/Cursor.py