import threading
from pycoingecko import CoinGeckoAPI
import tweepy

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


cg = CoinGeckoAPI()
espera = 60
bitcoin_antes = cg.get_price(ids='bitcoin', vs_currencies='BRL')

def update_bitcoin():
    threading.Timer(espera, update_bitcoin).start()
    global bitcoin_antes
    cg = CoinGeckoAPI()

    bitcoin_agora = cg.get_price(ids='bitcoin', vs_currencies='BRL')

    if bitcoin_agora != bitcoin_antes:

        if bitcoin_agora['bitcoin']['brl'] > bitcoin_antes['bitcoin']['brl']:
            status = "Bitcoin subiu R${} ".format(bitcoin_agora['bitcoin']['brl'])
            api.update_status(status=status)
            bitcoin_antes = cg.get_price(ids='bitcoin', vs_currencies='BRL')

        else:
            status = "Bitcoin caiu R${} ".format(bitcoin_agora['bitcoin']['brl'])
            api.update_status(status=status)
            bitcoin_antes = cg.get_price(ids='bitcoin', vs_currencies='BRL')

    else:
        bitcoin_agora = cg.get_price(ids='bitcoin', vs_currencies='BRL')



update_bitcoin()




