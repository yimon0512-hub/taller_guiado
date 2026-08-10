import yfinance as yf
aapl = yf.Ticker("AAPL")
datos = aapl.history(period="1mo")
print(datos)
datos.to_csv("aapl.csv")