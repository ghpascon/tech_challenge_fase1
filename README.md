# 📊 Projeto FastAPI - Análise de Dados de Vitivinicultura da Embrapa

Este projeto fornece uma API construída com FastAPI para acessar, processar e visualizar dados relacionados à vitivinicultura disponibilizados pela Embrapa.

---

## 🔐 Autenticação

### 1. Registro de Usuário

Acesse a rota `/auth/register` e informe os seguintes campos:

- `username`
- `password`
- `secret_key` (use `fiap_tech_challenge`)

<img src="http://localhost:8000/images/register1.png" alt="Cadastro" width="800"/>

---

### 2. Autenticação do Usuário

#### Passo 1: Clique em **Authorize**

<img src="http://localhost:8000/images/autenticar1.png" alt="Authorize" width="400"/>

#### Passo 2: Insira as credenciais registradas

<img src="http://localhost:8000/images/autenticar2.png" alt="Login" width="400"/>

#### Passo 3: Teste seu token na rota `/auth/me`

<img src="http://localhost:8000/images/autenticar3.png" alt="Token Test" width="800"/>

---

## 🍇 Consumo das APIs da Embrapa
### Rotas de chamada:

<img src="http://localhost:8000/images/embrapa1.png" alt="Chamada Embrapa" width="600"/>

Você pode filtrar os dados por ano usando o parâmetro `ano` (opcional).  
✅ Válido de **1970 até 2023**  
🔁 Se não informado ou estiver fora do intervalo, o ano padrão será **2023**.

<img src="http://localhost:8000/images/embrapa2.png" alt="Filtro de ano" width="600"/>

---

## 📬 Dúvidas ou sugestões?

Entre em contato pelo e-mail: **gh.pascon@gmail.com**

