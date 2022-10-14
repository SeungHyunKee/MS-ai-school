from currency_converter import CurrencyConverter   # 패키지설치 : pip install CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')    # CurrencyConverter객체를 만들때 뒤의 zip파일 가져와서 만든다

print(cc.convert(1, 'USD', 'KRW'))   # USD를 KRW로!
