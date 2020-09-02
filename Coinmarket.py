import tkinter as tk
import tweepy
import threading
from pycoingecko import CoinGeckoAPI

win = tk.Tk()
win.geometry("400x120")
win.title("TwitterBot")

consumer_key_label = tk.Label(win, text="API key: ")
consumer_key = tk.Entry(win, width=40)
consumer_key_label.grid(row=0)
consumer_key.grid(row=0,column=1)

consumer_secret_label = tk.Label(win, text="API key secret: ")
consumer_secret = tk.Entry(win, width=40)
consumer_secret_label.grid(row=1)
consumer_secret.grid(row=1,column=1)

access_token_label = tk.Label(win, text="Access Token:  ")
access_token = tk.Entry(win, width=40)
access_token_label.grid(row=2)
access_token.grid(row=2,column=1)

access_token_secret_label = tk.Label(win, text="Access Token Secret")
access_token_secret = tk.Entry(win, width=40)
access_token_secret_label.grid(row=3)
access_token_secret.grid(row=3,column=1)


cg = CoinGeckoAPI()
espera = 60
bitcoin_antes = cg.get_price(ids='bitcoin', vs_currencies='BRL')

def startbot():
    cg = CoinGeckoAPI()
    espera = 60
    bitcoin_antes = cg.get_price(ids='bitcoin', vs_currencies='BRL')
    auth = tweepy.OAuthHandler(consumer_key.get(), consumer_secret.get())
    auth.set_access_token(access_token.get(), access_token_secret.get())
    api = tweepy.API(auth)
    update_coin()



def update_coin():
    auth = tweepy.OAuthHandler(consumer_key.get(), consumer_secret.get())
    auth.set_access_token(access_token.get(), access_token_secret.get())
    api = tweepy.API(auth)
    threading.Timer(espera, update_coin).start()
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

button_start = tk.Button(win, text="Calculate", command=startbot())
button_start.grid(row=4,column=0)

win.mainloop()