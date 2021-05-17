# vagas_catho
Este projeto em python foi desenvolvido por Leandro Alves da Silva (leandro@3brs.com.br) pela 3 Bears Data Consulting

Através da execução do script ws.py, um web-scraping será feito no site da catho para obter a lista de 3 profissões, sendo elas: engenheiro de dados, analista de bi e cientista de dados.

Ao término da execução, na pasta do projeto será criado 3 arquivos que se referem a extração (dentro da pasta scrap) e mais 3 arquivos que se referem a aplicação do nltk para remoção das preposições e palavras indesejadas (pasta nltk).

Os testes foram feitos com o interpretador python 3.7 no navegador Google Chrome versão 90.
Dependendo da versão do seu google chrome, será necessário trocar o webdriver fazendo o download no site: https://chromedriver.chromium.org/downloads

Bibliotecas utilizadas: 
> pandas (pip install pandas)
> nltk (pip install nltk)
> selenium (pip install selenium)

Observação:
Dentro do script neural.py, há uma lista por nome de "outras" onde você pode adicionar as palavras que deseja que NÃO conste na word-cloud da sua ferramenta de dataviz.

Caso você altere essa relação de palavras não autorizadas após o web-scraping, você pode executar o script just_neural.py somente para gerar os arquivos nltk. Desta forma não será necessário realizar a extração dos dados novamente para aplicar a sua regra de exceções.
