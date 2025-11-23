# Projeto SGHSS - Back-end

Este repositório contém o Back-end do Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS), desenvolvido como requisito parcial da disciplina de Projeto Multidisciplinar (Uninter - 2025).

O sistema foca na gestão de pacientes e consultas, atendendo aos requisitos de segurança (LGPD) e autenticação via Token.

## 🚀 Tecnologias Utilizadas

* Linguagem: Python 3
* Framework: Django
* API: Django Rest Framework (DRF)
* Banco de Dados: SQLite (Ambiente de Desenvolvimento)
* Autenticação: Token Authentication

---

## 📦 Como rodar o projeto

Siga o passo a passo abaixo para configurar e executar a aplicação em sua máquina:

### 1. Clone o repositório
Abra o terminal e execute o comando abaixo:
git clone https://github.com/Muelgia/sistema/tree/master
cd nome-da-pasta-do-projeto

### 2. Crie e ative o ambiente virtual (Recomendado)

* No Windows:
python -m venv venv
.\venv\Scripts\activate

* No Linux ou Mac:
python3 -m venv venv
source venv/bin/activate

### 3. Instale as dependências
Com o ambiente virtual ativado, instale o Django e o DRF:
pip install django djangorestframework

### 4. Configure o Banco de Dados
Execute as migrações para criar as tabelas necessárias:
python manage.py migrate

### 5. Crie um Usuário Administrador
Para acessar o painel administrativo (/admin) e gerar tokens de teste:
python manage.py createsuperuser
(O terminal pedirá para você digitar um nome de usuário, e-mail e senha)

### 6. Inicie o Servidor
Por fim, coloque a aplicação no ar:
python manage.py runserver

O servidor estará rodando em: http://127.0.0.1:8000/

---

## 🔗 Principais Endpoints da API

A API segue o padrão REST. Para consumir os dados, utilize o Postman ou Insomnia.

| Método | URL | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |
| POST | /api-login/ | Recebe username e password e retorna o Token. | Pública |
| GET | /api/pacientes/ | Lista todos os pacientes cadastrados. | Token Obrigatório |
| POST | /api/pacientes/ | Cadastra um novo paciente. | Token Obrigatório |
| GET | /api/consultas/ | Lista o histórico de consultas. | Token Obrigatório |
| POST | /api/consultas/ | Agenda uma nova consulta. | Token Obrigatório |

### Exemplo de Autenticação
Para acessar as rotas protegidas, envie o Token no cabeçalho da requisição (Header):

Authorization: Token SEU_TOKEN_AQUI

---

## 👤 Autor

Samuel Carlos Garcia
* RU: 4534424
* Curso: Análise e Desenvolvimento de Sistemas
* Instituição: Centro Universitário Internacional UNINTER
* Semestre: 2025/A1