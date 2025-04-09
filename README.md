# 🏦 Aplicativo Bancário com CustomTkinter

Este projeto é uma interface gráfica para simular um sistema bancário, desenvolvida em **Python** com a biblioteca **CustomTkinter** para um visual moderno e responsivo. A aplicação atualmente inclui uma tela de login estilizada, com campos personalizados, imagem de fundo, botão de alternância de senha e link para cadastro.

---

## 📸 Preview

> Exemplo de interface da tela de login:

![Tela de Login](images/login.png)

---

## 📁 Estrutura do Projeto

Aplicativo_Banco/
├── images/                # Imagens utilizadas na interface
│   ├── eye_closed.png
│   ├── eye_open.png
│   ├── login.png
│   └── registro.png
├── login.py               # Tela de login
├── cadastro.py            # Tela de cadastro de usuário
├── main.py                # Tela principal do sistema após login
├── requirements.txt       # Lista de dependências do projeto
└── README.md              # Documentação do projeto

---

```markdown
## ✅ Funcionalidades

- [x] Tela de login com imagem de fundo
- [x] Campos personalizados para usuário e senha
- [x] Botão para mostrar/ocultar senha com ícone
- [x] Caixa de seleção "Lembrar senha"
- [x] Botão estilizado para login
- [x] Link clicável para cadastro de novo usuário

---

## 🛠 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://pillow.readthedocs.io/)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/Aplicativo_Banco.git
cd Aplicativo_Banco
```

2. **(Opcional) Crie e ative um ambiente virtual:**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
python login.py
```

---

## 📦 Requirements

O arquivo `requirements.txt` contém as seguintes dependências:

```
customtkinter
csv
os
bcrypt
Pillow
```

Você pode gerar novamente com:

```bash
pip freeze > requirements.txt
```

---

## 🧠 Próximos Passos

- [ ] Integração com banco de dados (SQLite)
- [ ] Tela de cadastros
- [ ] Criptografar as senhas cadastradas
- [ ] Validação real de login com usuários cadastrados
- [ ] Tela principal com funcionalidades bancárias (saldo, extrato, transferências)
- [ ] Lembrar acesso

---
