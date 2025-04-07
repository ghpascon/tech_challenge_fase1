# 📊 Projeto FastAPI - Análise de Dados de Vitivinicultura da Embrapa

Este projeto fornece uma API construída com FastAPI para acessar, processar e visualizar dados relacionados à vitivinicultura disponibilizados pela Embrapa.

---

## 🔐 Autenticação

### 1. Registro de Usuário

Acesse a rota `/auth/register` e informe os seguintes campos:

- `username`
- `password`
- `secret_key` (use `fiap_tech_challenge`)

<img src="https://i.postimg.cc/TwrJV4vx/6-c-Pz9q-Zl.png" alt="Cadastro" width="800"/>

---

### 2. Autenticação do Usuário

#### Passo 1: Clique em **Authorize**

<img src="https://i.postimg.cc/KjxrJDmM/1-XFa4l-Mg.png
" alt="Authorize" width="400"/>

#### Passo 2: Insira as credenciais registradas

<img src="https://i.postimg.cc/t4TkKkWd/2-an-K2m-Lj.png" alt="Login" width="400"/>

#### Passo 3: Teste seu token na rota `/auth/me`

<img src="https://i.postimg.cc/ydqTSz5n/3-IWIM7u-V.png" alt="Token Test" width="800"/>

---

## 🍇 Consumo das APIs da Embrapa
### Rotas de chamada:

<img src="https://i.postimg.cc/LsgTXsyn/4-gbykcd2.png" alt="Chamada Embrapa" width="600"/>

Você pode filtrar os dados por ano usando o parâmetro `ano` (opcional).  
✅ Válido de **1970 até 2023**  
🔁 Se não informado ou estiver fora do intervalo, o ano padrão será **2023**.

<img src="https://i.postimg.cc/g2TsmhHC/5-9r-J9-OL5.png" alt="Filtro de ano" width="600"/>

---

## 📬 Dúvidas ou sugestões?

Entre em contato pelo e-mail: **gh.pascon@gmail.com**

