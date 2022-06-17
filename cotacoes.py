import requests
from datetime import datetime
import xlsxwriter

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizadas. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")

workbook = xlsxwriter.Workbook('cots.xlsx')
worksheet = workbook.add_worksheet()


worksheet.write(0, 0, "Data/Hora")        
worksheet.write(0, 1, "Dolar") 
worksheet.write(0, 2, "Euro")   
worksheet.write(0, 3, "Bitcoin") 

worksheet.write(1, 0, str(datetime.now())) 
worksheet.write(1, 1, cotacao_dolar) 
worksheet.write(1, 2,cotacao_euro) 
worksheet.write(1, 3,cotacao_btc)

workbook.close()

