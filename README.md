<h1 align="center"; style="font-weight: bold;">API Flask com MVC e SQLite</h1>

<h3 align="center"><img  alt="Faculdade Impacta" width = "400px" src="https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png"></h3>

<p>
    <img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status = Concluído">
    <img src="https://img.shields.io/badge/Documentação-Completa-brightgreen" alt="Documentação: Completa">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
</p>

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

<p align="center">
    <a href="#sobre">Sobre</a> • 
    <a href="#grupo">Integrantes do Grupo</a> •
    <a href="#how-it-works">Funcionalidades</a> •
    <a href="#endpoints">Endpoints da API</a> •
    <a href="#licença">Licença</a>
</p>

<h2 id="sobre" align="center">📖 Sobre</h2>
Exercício da Disciplina de Desenvolvimento de APIs e Microsserviços, ministrada pelo professor Giovani Bontempo na Faculdade Impacta, durante o terceiro semestre do curso Análise e Desenvolvimento de Sistemas cursado no 2º Semestre de 2025.
<br><br>
O objetivo deste exercício é evoluir a aplicação vista em aula: https://github.com/giovbon/MVC-flask.
<br><br>
Com base nesse esqueleto você irá construir um “Gerenciador de Tarefas” (To-Do List) onde os usuários, já existentes no seu banco de dados, podem ter tarefas associadas a eles. A aplicação utilizará a arquitetura MVC para separar as responsabilidades, o Flask como framework, o SQLAlchemy para interagir com o banco de dados SQLite, e o Jinja2 (tem-plates do Flask) para criar a interface do usuário.
<br><br>
Objetivo Principal
<br>
• Aplicar o padrão MVC de forma prática em um novo módulo da aplicação.<br>
• Criar e gerenciar relacionamentos entre tabelas no banco de dados (um Usuário tem
várias Tarefas).<br>
• Realizar operações CRUD (Create, Read, Update, Delete) completas em um novo recurso
(“Tarefas”), interagindo com o banco de dados.<br>
• Construir uma interface web simples com HTML para interagir com a aplicação.

<br>

<h2 id="grupo" align="center">👥 Integrantes do Grupo 12</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/ErickXr.png" width="100" alt="Foto"/><br>
      <b>Erick Xavier Ribeiro</b><br><br>
        <a href="https://www.linkedin.com/in/erick-xavier-0a0b572a9/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
        <a href="https://github.com/ErickXr" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/Jloren051.png" width="100" alt="Foto"/><br>
      <b>Julia Lourenço Nogueira</b><br><br>
        <a href="https://www.linkedin.com/in/julia-louren%C3%A7o-8065082ba/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/Jloren051" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/LucasAguiarN.png" width="100"  alt="Foto"/><br>
      <b>Lucas Aguiar Nunes</b><br><br>
      <a href="https://www.linkedin.com/in/lucas-aguiar-nunes" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/LucasAguiarN" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
  </tr>
</table>

<h2 id="how-it-works">⚙️ Funcionalidades</h2>
🔹 Cadastro de Usuário
<br>🔹 Cadastro de Tarefas
<br>🔹 Listagem de Usuários
<br>🔹 Listagem de Tarefas
<br>🔹 Alterar Status de Tarefas
<br>🔹 Deletar Tarefas

<h2 id="endpoints">🛠️ Endpoints da API</h2>

Listagem de Usuários
```bash
curl -X GET http://localhost:5002
```
Cadastro de Usuário
```bash
curl -X POST http://localhost:5002/create_user \
    -H "Content-Type: application/json" \
    -d '{"name":"Lucas","email":"lucas@email.com"}'
```
Listagem de Tarefas
```bash
curl -X GET http://localhost:5002/tasks
```
Cadastro de Tarefas
```bash
curl -X POST http://localhost:5002/tasks/new \
    -H "Content-Type: application/json" \
    -d '{"user_id":"1","title":"Tarefa 1", "description":"Descrição da Tarefa"}'
```
Alterar Status de Tarefas
```bash
curl -X POST http://localhost:5002/tasks/update/<int:task_id>
```
Deletar Tarefas
```bash
curl -X POST http://localhost:5002//tasks/delete/<int:task_id>
```

<h2 id="licença">📜 Licença</h2>
Este projeto é para fins educacionais e está disponível sob a <a href="./LICENSE">Licença MIT.</a>
