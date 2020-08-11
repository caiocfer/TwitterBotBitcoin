# TwitterBotBitcoin
Bot simples que tweeta caso o Bitcoin altere o valor.

Utilizado as bibliotecas:
   pycoingecko, para solicitar o valor da moeda, 
   threading, para dar um intervalo de tempo na execução da função e 
   tweepy para que a mensagem seja postada no twitter.
Para usar é simples, após criar um conta de desenvolvedor no Twitter, apenas substitua as váriaveis:
  consumer_key = ''
  consumer_secret = ''
  access_token = ''
  access_token_secret = ''
para as que foi lhe fornecido.

Para mudar o intervalo entre uma execução e outra apenas altera a variavel "espera", a mesma aceita valores em segundos.



