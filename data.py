import json, time, requests
import hashlib, hmac
import pprint

'''
Get Stock Data
'''
def get(symbols, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        tmp_df = pdr.DataReader(name=symbol, data_source='yahoo',
                        start=start_date, end=end_date)
        # This will be for later to save the results locally
        #df.to_csv(filename, index_label="Date")
        tmp_df = tmp_df[['Adj Close']].rename(columns={'Adj Close': symbol})
        df = df.join(tmp_df, how='inner')

    # Clean the data up
    df.fillna(method="ffill",inplace="TRUE")
    df.fillna(method="bfill",inplace="TRUE")

    return df

'''
Get Crypto Data
'''
def get_crypto(symbol):
    url = "https://bittrex.com/api/v1.1/public/getticker?market=" + symbol

    response = requests.get(url)

    return response.json()
