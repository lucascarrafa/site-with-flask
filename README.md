# Site desenvolvido utilizando Framework Flask

![Imagem](https://www.programmerbay.com/wp-content/uploads/2018/07/flask-300x168.png)

O sistema operacinal utilizado para desenvolver essa aplicação foi o Windows 10

## Instalando o virtualenv

Antes de tudo é necessario instalar o virtualenv, para isso basta executar o seguinte comando no PowerShell:

```
PS C:\> pip install virtualenv
```

## Executando a aplicação

Para usar o script, é preciso relaxar a política de execução do sistema AllSigned, significando que todos os scripts no sistema devem ser assinados digitalmente para serem executados. Como o script de ativação virtualenv é assinado por um dos autores (Jannis Leidel), esse nível da política de execução é suficiente. Como administrador, execute:

```
PS C:\> Set-ExecutionPolicy AllSigned
````

Para rodar a aplicação basta executar o comando:

```
PS C:\> venv/Script/activate
```
