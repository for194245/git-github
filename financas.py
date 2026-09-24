import pandas as pd
import yfinance as yf

# Baixar dados históricos de ações da Apple usando yfinance
df = yf.download('AAPL', start='2026-01-01', end='2026-08-31')
print(df.head())
print()
print(df.tail())
print()

# Calcular a média móvel simples de 20 dias
df['SMA_20'] = df['Close'].rolling(window=20).mean()
print(df[['Close', 'SMA_20']].tail())