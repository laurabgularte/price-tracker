# 📈 Price Tracker Python

Um monitor de preços automatizado que realiza web scraping, armazena o histórico em base de dados SQL e envia alertas quando o preço de um produto atinge o valor desejado.

---

## 🚀 Funcionalidades

- **Extração de Dados:** Utiliza `BeautifulSoup4` e `Requests` para capturar preços de sites de e-commerce.
- **Persistência SQL:** Armazena cada verificação numa base de dados `SQLite`, permitindo futuras análises de tendência.
- **Automação:** Loop de verificação configurável com tratamento de exceções.
- **Resiliência:** Uso de Headers para simular navegação real e evitar bloqueios (HTTP 403).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Extração:** BeautifulSoup4, Requests
- **Base de Dados:** SQLite3

---

## 🔧 Como Executar

```bash
git clone [https://github.com/laurabgularte/price-tracker.git](https://github.com/laurabgularte/price-tracker.git)

pip install -r requirements.txt

python price_tracker.py
```
