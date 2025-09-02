# Todoify API

Uma API RESTful para gerenciamento de tarefas (To-Do list), construída com Python, FastAPI e Pydantic. Este projeto foi desenvolvido como parte do "Guia de Estudos Completo para Engenharia de Backend".

## ✨ Funcionalidades

A API oferece funcionalidades completas de CRUD (Create, Read, Update, Delete) para tarefas.

* **Criar** uma nova tarefa.
* **Listar** todas as tarefas existentes.
* **Buscar** uma tarefa específica pelo seu ID.
* **Atualizar** uma tarefa existente.
* **Deletar** uma tarefa.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **FastAPI**: Para a construção da API.
* **Pydantic**: Para validação e serialização de dados.
* **Uvicorn**: Como servidor ASGI para rodar a aplicação.

## 🚀 Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar
    python -m venv env

    # Ativar (Windows)
    .\env\Scripts\activate

    # Ativar (Linux/macOS)
    source env/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o servidor:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Acesse a documentação interativa** para testar os endpoints no seu navegador:
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

##  API Endpoints

| Método HTTP | Endpoint                 | Descrição                      |
|-------------|--------------------------|--------------------------------|
| `GET`       | `/todos`                 | Lista todas as tarefas.        |
| `POST`      | `/todos`                 | Cria uma nova tarefa.          |
| `GET`       | `/todos/{todo_id}`       | Busca uma tarefa pelo ID.      |
| `PUT`       | `/todos/{todo_id}`       | Atualiza uma tarefa pelo ID.   |
| `DELETE`    | `/todos/{todo_id}`       | Deleta uma tarefa pelo ID.     |
