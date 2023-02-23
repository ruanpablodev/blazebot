import time
import schedule
import sys
from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import telebot
import buttons
import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynotifier import Notification
import os

import mysql.connector


def inserir(wins, winssemg, winsg1, winsg2, brancos, seguidos, loss, atualizacao):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="blazebot"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO dados (wins, winssemg, winsg1, winsg2, brancos, seguidos, loss, atualizacao)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (wins, winssemg, winsg1, winsg2, brancos, seguidos, loss, atualizacao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "[!] - database atualizada")




def notificar(titulo, desc, duracao):
    Notification(
        title=titulo,
        description=desc,
        icon_path='./icones/blaze.ico', # On Windows .ico is required, on Linux - .png
        duration=duracao,                                   # Duration in seconds
        urgency="critical"
    )


notificar("Alerta", "BOT INICIADO",  5)
print('''\033[36m
  _______ _    _ _    _ _   _ _____  ______ _____  
 |__   __| |  | | |  | | \ | |  __ \|  ____|  __ \ 
    | |  | |__| | |  | |  \| | |  | | |__  | |__) |
    | |  |  __  | |  | | . ` | |  | |  __| |  _  / 
    | |  | |  | | |__| | |\  | |__| | |____| | \ \ 
    |_|  |_|  |_|\____/|_| \_|_____/|______|_|  \_\
                                                   
                          @ThunderSinaisTG                         \033[37m''')


# Por informações do seu bot.########
api_key = '6059262917:AAHQ5aS0VEWyrDLOYT0_08vZCL9oCNO7VjU'  # TOKEN DO SEU BOT
chat_id = '-1001899381447' # ID DO CANAL pladix
grupo_id = '-1001899381447'
#####################################
bot = telebot.TeleBot(token=api_key)


options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')

analisar = 0
gale_atual = 0
analisar_open = 0
resultsDouble = []
win = 'CAACAgEAAxkBAAEBQs5jBL9vuTvNT3Ovdvhgo3IUFTnmCgACbAMAAvC_2EcDGSgReENv2CkE'
los = 'CAACAgEAAxkBAAEBQupjBMFhcot6f95xRwhtzSacfFMAAdQAAlIDAAJwfdlH1YM_v41FYAUpBA'
#win_sen_gale = 'CAACAgEAAxkBAAEBQtJjBMCGCUtABPrX1VA3NqLBOzTIDAACbAMAAvC_2EcDGSgReENv2CkE'
win_g1 = 'CAACAgEAAxkBAAEBQtZjBMCr0b21q0Ind26w2vUStl_iFgACcwIAAqel2Ed2CRv68cyUbikE'
win_g2 = 'CAACAgEAAxkBAAEBQtpjBMDQh2JVAAFdBNaWBrpIR-w3a3oAAnYEAAKbhthHAAFiscNNvf_DKQQ'
brc = 'CAACAgEAAxkBAAEBQt5jBMDi-AUh9rmk8iccEQU_8coQ1gAC-gIAAs652EeOmG7Xu_XtZCkE'
brc_gale1 = 'CAACAgEAAxkBAAEBQuJjBMENPUW7BK0gIJJplQVKZ9GUkQACxgIAArat4EcHZxpl5Mo-TSkE'
brc_gale2 = 'CAACAgEAAxkBAAEBQuZjBMFMLfxAsaHYQywmDS5EBYNhbwACQQIAAn5k2UfhDmIr6Q53SCkE'

# variaveias
#nomebot = input("Informe qual quer valor: ")
winsa = input("Infome a quantidade de wins total: ")
winsemga = input("Infome a quantidade de wins sem gale: ")
wing1a = input("Infome a quantidade de wins gale 1: ")
wing2a = input("Infome a quantidade de wins gale 2: ")
seguidosa = input("Infome a quantidade de wins seguidos: ")
brancoa = input("Infome a quantidade de brancos: ")
lossa = input("Infome a quantidade de loss: ")

wins = int(winsa)
winsemg = int(winsemga)
wing1 = int(wing1a)
wing2 = int(wing2a)
seguidos = int(seguidosa)
branco = int(brancoa)
loss = int(lossa)



print("")
print("")
print("Carregando...")
time.sleep(5)
os.system('cls')
print("Carregando...")
time.sleep(3)
os.system('cls')
print('''\033[36m
  _______ _    _ _    _ _   _ _____  ______ _____  
 |__   __| |  | | |  | | \ | |  __ \|  ____|  __ \ 
    | |  | |__| | |  | |  \| | |  | | |__  | |__) |
    | |  |  __  | |  | | . ` | |  | |  __| |  _  / 
    | |  | |  | | |__| | |\  | |__| | |____| | \ \ 
    |_|  |_|  |_|\____/|_| \_|_____/|______|_|  \_\
                                                   
                          @ThunderSinaisTG                         \033[37m''')



while True:
    def qualnum(x):
        if x == '0':
            return 0

        if x == '1':
            return 1

        if x == '2':
            return 2

        if x == '3':
            return 3

        if x == '4':
            return 4

        if x == '5':
            return 5

        if x == '6':
            return 6

        if x == '7':
            return 7

        if x == '8':
            return 8

        if x == '9':
            return 9

        if x == '10':
            return 10

        if x == '11':
            return 11

        if x == '12':
            return 12

        if x == '13':
            return 13

        if x == '14':
            return 14
    def qualcor(x):
        if x == '0':
            return 'B'

        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'V'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'P'
    def qualcor2(x):
        if x == '0':
            return '⚪️'

        if x == '1':
            return '🟥'

        if x == '2':
            return '🟥'

        if x == '3':
            return '🟥'

        if x == '4':
            return '🟥'

        if x == '5':
            return '🟥'

        if x == '6':
            return '🟥'

        if x == '7':
            return '🟥'

        if x == '8':
            return '⬛️'

        if x == '9':
            return '⬛️'

        if x == '10':
            return '⬛️'

        if x == '11':
            return '⬛️'

        if x == '12':
            return '⬛️'

        if x == '13':
            return '⬛️'

        if x == '14':
            return '⬛️'
       
    try: 
        resulROOL = nav.find_element(
        By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        oie = 1
    except Exception as erro:
        laiea = 1


    analisar_open = 0
    if resulROOL == 'Girando...':
        analisar_open = 1
        print('\033[33m[!] - Procurando sinal...\033[37m')
        time.sleep(13) 
        c = nav.page_source
        resultsDouble.clear()
        
        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                resultsDouble.append(i.getText())
            else:
                resultsDouble.append('0')
        
        resultsDouble = resultsDouble[:-1]
        
        if analisar_open == 1:

            default = resultsDouble[0:10]
            ultimonum = resultsDouble[0:1]
            ultimos6numeros = resultsDouble[0:20]
            ultimos20numeros = resultsDouble[0:6]
            ultimas6coress = map(qualcor2, ultimos6numeros)
            ultimas6cores = list(ultimas6coress)


            

               

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)

            finalnum = list(mapeando)
            finalcor = list(mapeando2)
            agora = datetime.datetime.now()
            agora_string = agora.strftime("%d/%m/%y - %H:%M:%S")
            hora = agora.strftime("%H:%M:%S")
            atualizaçaoinfo = agora.strftime("%y/%m/%d %H:%M:%S")
            atualizacao = agora_string

            soma1 = wins + branco + loss
            somawin1 = wins + branco
            divisao1 = somawin1 / soma1
            p1 = divisao1 * 100
            a1 = (f"{p1:.2f}%")

            def imagemEnv(wins, loss, branco):
                    img = Image.open("status.png")
                    draw = ImageDraw.Draw(img) 
                    font = ImageFont.truetype("good times rg.otf", 70) 
                    draw.text((145, 490), wins, (255, 255, 255), font=font) 
                    draw.text((575, 490), loss, (255, 255, 255), font=font) 
                    draw.text((1050, 490), branco, (255, 255, 255), font=font) 
                    aaaa = img.convert('RGB')
                    aaaa.save('imagemEnviar.jpg')
                    #print("imagem atualizada")


                    bot.send_photo(chat_id=grupo_id, photo=open('imagemEnviar.jpg', 'rb'), caption=('''📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a1, atualizacao)))


                    

            

            
            
        

            
            bot.edit_message_text(chat_id=chat_id, text='''
            ULTIMOS 20 NUMEROS:
                 1° : %s(%s)
                 2° : %s(%s)
                 3° : %s(%s)
                 4° : %s(%s)
                 5° : %s(%s)
                 6° : %s(%s)
                 7° : %s(%s)
                 8° : %s(%s)
                 9° : %s(%s)
                 10° : %s(%s)
                 11° : %s(%s)
                 12° : %s(%s)
                 13° : %s(%s)
                 14° : %s(%s)
                 15° : %s(%s)
                 16° : %s(%s)
                 17° : %s(%s)
                 18° : %s(%s)
                 19° : %s(%s20° : %s(%s)
            Data Atualizaçao: %s
                           ''' % (ultimas6cores[0], ultimos6numeros[0], ultimas6cores[1], ultimos6numeros[1], ultimas6cores[2], ultimos6numeros[2], ultimas6cores[3], ultimos6numeros[3], ultimas6cores[4], ultimos6numeros[4], ultimas6cores[5], ultimos6numeros[5], ultimas6cores[6], ultimos6numeros[6], ultimas6cores[7], ultimos6numeros[7], ultimas6cores[8], ultimos6numeros[8], ultimas6cores[9], ultimos6numeros[9], ultimas6cores[10], ultimos6numeros[10],ultimas6cores[11], ultimos6numeros[11], ultimas6cores[12], ultimos6numeros[12], ultimas6cores[13], ultimos6numeros[13],ultimas6cores[14], ultimos6numeros[14],ultimas6cores[15], ultimos6numeros[15],ultimas6cores[16], ultimos6numeros[16],ultimas6cores[17], ultimos6numeros[17],ultimas6cores[18], ultimos6numeros[18], ultimas6cores[19], ultimos6numeros[19], atualizacao), message_id=5, parse_mode="HTML") 



            def CHECK_VERSION(num):
                global analisar
                global gale_atual
                global wins
                global loss
                global winsemg
                global wing1
                global wing2
                global branco
                global atualizacao
                global seguidos
                global imagemEnv

                if analisar == 0:
                    if num[0:3] == ['V', 'V', 'P']:
                        analisar = 1
                        
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO:⬛️(PRETO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 2546

</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>                     
                        ''' % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())

                        return
                    if num[0:3] == ['P', 'P', 'V']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 9658
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>

                        '''  % ultimonum[0] ,parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return
                

                    if num[0:3] == ['P', 'V', 'P']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 1073
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] ,parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return

                    if num[0:3] == ['V', 'P', 'V']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: ⬛️(PRETO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: ⬛️(PRETO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 9378
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return
                    
                    if num[0:3] == ['B', 'V', 'V']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬛️(PRETO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 6387
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return

                    if num[0:3] == ['B', 'P', 'P']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 7836
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return
                    
                    if num[0:3] == ['B', 'V', 'P']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 8936
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return
                        
                    if num[0:3] == ['B', 'P', 'V']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: ⬛️(PRETO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: ⬛️(PRETO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 3582
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return

                        #------------------------
                        #
                        #
                        #ESTRETEGIAS DE MAIS CORES
                        #
                        #
                        #
                        #---------------

                    if num[0:8] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 4384
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())
                        return

                    if num[0:7] == ['V', 'V', 'V', 'V', 'V', 'V', 'V']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: ⬛️(PRETO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: ⬛️(PRETO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 8363
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())

                        return

                    #if num[0,5] == ['P', 'P', 'P', 'P', 'V']:
                    if num[0:5] == ['P', 'P', 'P', 'P', 'V']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO:  🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 4387
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())

                        return

                    if num[0:5] == ['V', 'V', 'V', 'P', 'V']:
                        analisar = 1 #4387
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: ⬛️(PRETO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: ⬛️(PRETO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 5748
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())

                        return

                    if num[0:6] == ['P', 'V', 'V', 'P', 'V', 'P']:
                        analisar = 1
                        print("\033[33m[!!] - Sinal encontrado e enviado!\033[37m ")
                        notificar("[!] - Sinal encontrado", ("ENTRAR NO: 🟥(VERMELHO)\nPROTEGER NO: ⬜(BRANCO)\nAPOSTAR DEPOIS DO %s"   % ultimonum[0]), 10)
                        bot.send_message(chat_id=chat_id, text='''
<b>🚨ENTRADA CONFIRMADA🚨
[🎯] - ENTRAR NO: 🟥(VERMELHO)
[🎰] - PROTEGER NO: ⬜(BRANCO)
[🃏] - APOSTAR DEPOIS DO %s
[♟] - COD. ESTRATEGIA:</b><code> 1187
</code><b>🎱<a href='https://t.me/ThunderSinaisTG'>MELHOR BOT DA BLAZE</a>🎱</b>'''  % ultimonum[0] , parse_mode="HTML", reply_markup=buttons.linkdouble())

                        return

                
                    


                elif analisar == 1:
                   
                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num[0:3] == ['P', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            winsemg += 1
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            
                            
                            bot.send_sticker(
                                chat_id=chat_id, sticker=win)
                            seguidos += 1


                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
  

                            return
                        if num[0:3] == ['V', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            winsemg += 1
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim
                            bot.send_sticker(
                                chat_id=chat_id, sticker=win)
                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)

                            return
                        if num[0:3] == ['B', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return

                        if num[0:3] == ['V', 'V', 'V']:
                            gale_atual = gale_atual+1
                            print("\033[35m[!] - GALE 1\033[37m")
                            bot.send_message(chat_id=chat_id, text='''
[⚠️] - VAMOS PARA O GALE 1
    Dobre sua aposta
                        ''')
                            return
                        if num[0:3] == ['P', 'P', 'P']:
                            gale_atual = gale_atual+1
                            print("\033[35m[!] - GALE 1\033[37m")
                            bot.send_message(chat_id=chat_id, text='''
[⚠️] - VAMOS PARA O GALE 1
    Dobre sua aposta
                        ''')
                            return

                    if gale_atual == 1:
                        if num[0:3] == ['P' ,'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")
                            wing1 += 1

                            # soma
                            soma = wins + branco + loss
                            
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=win_g1)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['V', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")
                            wing1 += 1

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim
          
                            bot.send_sticker(
                                chat_id=chat_id, sticker=win_g1)

                            seguidos += 1

                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc_gale1)

                            seguidos += 1
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")
                            str
                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc_gale1)

                            seguidos += 1

                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return

                        if num[0:3] == ['V', 'V', 'V']:
                            gale_atual = gale_atual+1
                            print("\033[35m[!] - GALE 2\033[37m")
                            bot.send_message(chat_id=chat_id, text='''
[⚠️] - VAMOS PARA O GALE 2
    Dobre sua aposta
                        ''')
                            return
                        if num[0:3] == ['P', 'P', 'P']:
                            gale_atual = gale_atual+1
                            print("\033[35m[!] - GALE 2\033[37m")
                            bot.send_message(chat_id=chat_id, text='''
[⚠️] - VAMOS PARA O GALE 2
    Dobre sua aposta
                        ''')
                            return

                    if gale_atual == 2:
                        if num[0:3] == ['P' ,'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")
                            wing2 += 1

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=win_g2)

                            seguidos += 1

                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['V', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")
                            wing2 += 1

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=win_g2)

                            
                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc_gale2)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc_gale2)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return

                        if num[0:3] == ['V', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            loss += 1
                            notificar("Alerta", "❌❌❌❌DEU LOSS❌❌❌❌",  5)
                            print("\033[31m[!] - LOSS\033[37m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=los)

                            seguidos = 0
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['P', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            loss += 1
                            notificar("Alerta", "❌❌❌❌DEU LOSS❌❌❌❌",  5)
                            print("\033[31m[!] - LOSS\033[37m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=los)

                            seguidos = 0
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return

                        if num[0:3] == ['V', 'V', 'V']:
                            gale_atual = gale_atual+1
                            print("\033[35m[!] - GALE 3\033[37m")
                            bot.send_message(chat_id=chat_id, text='''
[⚠️] - VAMOS PARA O GALE 2
    Dobre sua aposta
                        ''')
                            return
                        if num[0:3] == ['P', 'P', 'P']:
                            gale_atual = gale_atual+1
                            print("\033[35m[!] - GALE 3\033[37m")
                            bot.send_message(chat_id=chat_id, text='''
[⚠️] - VAMOS PARA O GALE 2
    Dobre sua aposta
                        ''')
                            return


                    if gale_atual == 3:
                        if num[0:3] == ['P' ,'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")
                            wing2 += 1

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=win_g2)

                            seguidos += 1

                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['V', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            wins += 1
                            notificar("Alerta", "✔️✔️✔️✔️DEU GREEN✔️✔️✔️✔️",  5)
                            print("\033[32m[!] - WIN\033[37m")
                            wing2 += 1

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=win_g2)

                            
                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc_gale2)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['B', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            branco += 1
                            notificar("Alerta", "⬜⬜⬜⬜DEU BRANCO⬜⬜⬜⬜",  5)
                            print("\033[1m[!] - BRANCO\033[0;0m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=brc_gale2)

                            seguidos += 1
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return

                        if num[0:3] == ['V', 'V', 'V']:
                            analisar = 0
                            gale_atual = 0
                            loss += 1
                            notificar("Alerta", "❌❌❌❌DEU LOSS❌❌❌❌",  5)
                            print("\033[31m[!] - LOSS\033[37m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=los)

                            seguidos = 0
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        if num[0:3] == ['P', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            loss += 1
                            notificar("Alerta", "❌❌❌❌DEU LOSS❌❌❌❌",  5)
                            print("\033[31m[!] - LOSS\033[37m")

                            # soma
                            soma = wins + branco + loss
                            somawin = wins + branco
                            divisao = somawin / soma
                            p = divisao * 100
                            a = (f"{p:.2f}%")
                            # fim

                            bot.send_sticker(
                                chat_id=chat_id, sticker=los)

                            seguidos = 0
                            
                            imagemEnv(str(wins), str(loss), str(branco))
                            bot.edit_message_text(chat_id=chat_id, text=(
                                '''<b>📊 ESTATISTICAS 📊
  ✅WINS TOTAL: %s
  ✅WINS SEM GALE: %s
  ✅WINS GALE 1: %s
  ✅WINS GALE 2: %s
  ✅WINS SEGUIDOS: %s
  ⚪️BRANCOS: %s
  ❌LOSS: %s
  🏆PERCENTUAL DE GANHOS: %s
  Data atualizaçao: %s</b>''' % (wins, winsemg, wing1,wing2,seguidos, branco, loss, a, atualizacao)), message_id=4, parse_mode="HTML")
                            inserir(wins, winsemg, wing1,wing2, branco, seguidos, loss, atualizaçaoinfo)
                            return
                        

            checkVersion = CHECK_VERSION(finalcor)
            
