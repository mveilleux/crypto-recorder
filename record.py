import data
import time

DATABASE_DIR = 'db'

symbols = ['BTC-ETH', 'USDT-BTC']

timestamp = str(int(time.time()))

for symbol in symbols:
    # Get the latest data
    r = data.get_crypto(symbol)

    with open(DATABASE_DIR + "/" + symbol + ".csv", "a") as mydb:
        out = timestamp + ','
        out += str(r['result']['Ask']) + ','
        out += str(r['result']['Bid']) + ','
        out += str(r['result']['Last']) + "\n"

        mydb.write(out)
