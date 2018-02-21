### Exemplos apresentados na palestra "Usando BDs NoSQL com Python", no evento "SQL Saturday Salvador 2017", em 18/11/2017. ###

O objetivo dos programas aqui apresentados é tanto trabalhar com os conceitos dos bancos de dados NoSQL quanto apresentar código em Python que possa ser compreendido por pessoas iniciantes na linguagem e servir de fonte básica de estudo. Todos os programas devem ser executados com Python 3. O conteúdo se divide em:

1. **Pasta "exemplos_bds_nosql"**
    
    Exemplos básicos dos quatro tipos de bancos NoSQL (chave-valor, orientado a documentos, colunar e orientado a grafo). São apresentados também arquivos de testes para cada banco e aplicações tipo linha de comando (CLI) utilizando os bancos chave-valor e orientado a documentos.  
   
2. **Pasta "sql"**
    
    Aplicação tipo linha de comando (CLI) utilizando um banco relacional (SQLite), para servir como parâmetro de comparação. O arquivo "criar_banco.py" deve ser executado primeiro e criará um arquivo chamado "dados.sqlite".  
 
3. **Pasta "mongo"**

    Aplicação tipo linha de comando (CLI) utilizando o banco MongoDB. O exemplo busca acessar um servidor instalado na própria máquina (127.0.0.1). Caso seja utilizado um servidor em uma máquina remota, os parâmetros de conexão e controle de acesso precisarão ser alterados.  

4. **Pasta "redis"**

    Programa com uma lista de comandos executados contra um banco Redis. O exemplo busca acessar um servidor instalado na própria máquina (127.0.0.1). Caso seja utilizado um servidor em uma máquina remota, os parâmetros de conexão e controle de acesso precisarão ser alterados.   

5. **Dockerfile**

    Para os conhecedores da ferramenta Docker, o arquivo "Dockerfile" contem os comandos para a criação de um container ("python3_redis_mongo") com todo o conteúdo necessário para executar os programas, inclusive um banco Redis e um banco MongoDB. O tamanho final é aproximandamente 670 MB. Siga os seguintes passos:

    - Crie o container:
    
        ```docker build . -t python3_redis_mongo```
    
    - Inicie o container (todos os arquivos ficarão disponíveis e atualizáveis no container em "/home/code"):

    ```docker run -i -t -v $(pwd)/:/home/code:rw python3_redis_mongo```
    
    - Inicie os bancos de dados (na ordem e quando achar melhor):

    ```service redis-server start```

    ```service mongodb start```

