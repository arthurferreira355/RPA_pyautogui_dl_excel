from platform import machine
import pyautogui
import webbrowser
import time
import os
import fnmatch
import shutil

new_download = ''
brtt_dir = r'C:\Users\arthu\Desktop\automatizando'
os.chdir(r"C:\Users\arthu\Downloads")

def posicao_mouse():
    print(pyautogui.position())

def entrar_site():
    webbrowser.open('https://ifood.niduu.com/admin/overview')
    time.sleep(5)

def clicar_menu():
    pyautogui.moveTo(108,669, duration=0.25)
    pyautogui.click(108,669, button='left', duration=0.25)
    time.sleep(1)

def clicar_excel():
    pyautogui.moveTo(1478,395, duration=0.25)
    pyautogui.click(1478,395, button='left', duration=0.25)
    time.sleep(1)
    time.sleep(5)

def buscar_arquivo():
    for entry in os.listdir():
        if fnmatch.fnmatch(entry, "listagem_de_colaboradores.xlsx"):
            new_download = entry
    if new_download != '':
        print("Movendo arquivo...", new_download)
        shutil.move(new_download, brtt_dir+'Teste.xlsx')
        time.sleep(5)

new_download = ''

def main():
    entrar_site()
    clicar_menu()
    clicar_excel()
    buscar_arquivo()

if __name__ == '__main__':
    main()

