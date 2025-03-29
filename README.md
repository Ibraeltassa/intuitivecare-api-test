# IntuitiveCare - Teste de API

Este repositório contém a solução para o desafio de **API com busca textual** do processo seletivo da **IntuitiveCare**.

## 📄 Descrição

O sistema realiza as seguintes etapas automaticamente:

1. Lê o arquivo CSV `Relatorio_cadop.csv` com o cadastro de operadoras da ANS.
2. Expõe uma API em Flask com uma rota `/buscar` que recebe um termo de busca.
3. A API retorna os registros mais relevantes contendo esse termo.
4. Os resultados podem ser visualizados diretamente ou consumidos via front-end.
5. Uma coleção Postman foi criada para testar e demonstrar o funcionamento da API.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask
- Pandas
- Vue.js 3 + Vite
- Postman

---

## ▶️ Como Executar

### Back-End

```bash
# Clone o repositório
git clone https://github.com/Ibraeltassa/intuitivecare-api-test.git

# Navegue até a pasta do projeto
cd intuitivecare-api-test

# Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r backend/requirements.txt

# Execute a API
python backend/app.py
```
### Front-End

```bash
# Acesse a pasta do front
cd frontend/frontend

# Instale as dependências
npm install

# Rode o projeto
npm run dev
