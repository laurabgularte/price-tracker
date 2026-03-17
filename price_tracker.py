import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from datetime import datetime


URL_PRODUTO = "https://www.exemplo.com/produto-desejado"  # substituir pela url real do produto
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
PRECO_ALVO = 500.00  # valor que dispara o alerta

def iniciar_db():
    """Cria o banco de dados e a tabela se não existirem."""
    conn = sqlite3.connect('precos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            preco REAL
        )
    ''')
    conn.commit()
    return conn

def extrair_preco():
    """Acessa o site e extrai o preço atual."""
    try:
        response = requests.get(URL_PRODUTO, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')

        # ajustar conforme o site alvo 
        preco_texto = soup.find("span", class_="a-offscreen").get_text()
        
       #converte em float
        preco_limpo = preco_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()
        return float(preco_limpo)
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return None

def salvar_no_banco(conn, preco):
    """Registra o preço com data e hora."""
    cursor = conn.cursor()
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO historico_precos (data, preco) VALUES (?, ?)', (data_atual, preco))
    conn.commit()
    print(f"[{data_atual}] Preço registrado: R$ {preco}")

def verificar_alerta(preco):
    """Lógica para enviar notificação (Telegram ou E-mail)."""
    if preco <= PRECO_ALVO:
        print("⚠️ ALERTA: O produto atingiu o preço desejado!")
        # da para integrar com o bot do telegram ou smtplib
    else:
        print("ℹ️ O preço ainda está acima do alvo.")

def monitorar():
    """Loop principal de monitoramento."""
    conn = iniciar_db()
    print("Iniciando monitoramento de preços...")
    
    try:
        while True:
            preco_atual = extrair_preco()
            if preco_atual:
                salvar_no_banco(conn, preco_atual)
                verificar_alerta(preco_atual)
            
            print("Aguardando próxima verificação em 1 hora...")
            time.sleep(3600) 
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")
    finally:
        conn.close()

if __name__ == "__main__":
    monitorar()