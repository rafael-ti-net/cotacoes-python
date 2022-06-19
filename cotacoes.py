import requests
from datetime import datetime
import smtplib
import email.message
import exportaGoogleSheets

data_hoje = datetime.now()
data_e_hora_em_texto = data_hoje.strftime('%d/%m/%Y às %H:%M')

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

def enviar_email(Data, Dolar, Euro, BTC): 
    Data = Data
    Dolar = Dolar
    Euro = Euro
    BTC = BTC

    corpo_email = f"""
    <p><b>Cotação Atualizadas em {Data} </b></p>
    <p>Dólar: R$ {Dolar}</p>
    <p>Euro: R$ {Euro}</p>
    <p>BTC: R$ {BTC}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Cotações de hoje - ' + data_e_hora_em_texto
    msg['From'] = 'robo.python.heroku@gmail.com'
    msg['To'] = 'rafael.ti.net@gmail.com'
    password = 'cpxbrmqmbhlvarjk'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email(data_e_hora_em_texto,cotacao_dolar,cotacao_euro,cotacao_btc)

print(f"Cotação Atualizadas. {data_e_hora_em_texto}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")

exportaGoogleSheets.main(data_e_hora_em_texto, cotacao_dolar,cotacao_euro,cotacao_btc)