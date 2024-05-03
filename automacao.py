import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

def selecionaIntervalo(iniX, iniY, fimX,fimY):
    pyautogui.moveTo(iniX,iniY)
    pyautogui.mouseDown()
    pyautogui.moveTo(fimX,fimY)
    pyautogui.mouseUp()

def ctrlC ():
    pyautogui.hotkey('ctrl','c')
    conteudo = pyperclip.paste()
    return conteudo

def mandaMensagem(qnt, mensagem):
    for i in range(qnt):
        pyautogui.click(141,15,duration=0.2)
        pyautogui.click(536,284,duration=0.2)
        sleep(0.1)
        for h in range(i):
            pyautogui.press('down')
        numero = ctrlC()
        pyautogui.scroll(1000)
        pyautogui.click(401,12)
        numero = "wa.me/+55" + numero
        pyautogui.click(273,64,clicks=3)
        sleep(0.1)
        pyautogui.write(numero)
        pyautogui.press('enter')
        sleep(2)
        #clica no 'abrir no wpp'
        pyautogui.click(1058,247,duration=0.2)
        sleep(0.8)
        
        #caso nao existir o numero, clica em ok
        pyautogui.click(582,556,duration=0.2)
        sleep(0.2)
        
        #manda a mensagem
        pyautogui.click(538,1015,duration=0.2)
        sleep(0.1)
        pyautogui.write(mensagem)
        sleep(0.1)
        pyautogui.press('enter')
        
        #clica na minha conversa
        pyautogui.click(190,196,duration=0.2)
        sleep(0.2)
        
        #clica para minimizar a aba do wpp
        pyautogui.click(843,14,duration=0.2)


mandaMensagem(100, "Bom dia, tudo bem?")
