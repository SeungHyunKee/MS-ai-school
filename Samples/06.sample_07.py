import requests 

from bs4 import BeautifulSoup  # BeautifulSoup : 웹크롤링 해주는 패키지

# 특정사이트내용중 환율부분만 크롤링해서 가져오겠다
def get_exchange_rate(target1, target2): 

    headers = { 

        'User-Agent': 'Mozilla/5.0',   # User-Agent, mozilla : 최초브라우저 웹 이름

        'Content-Type': 'text/html; charset=utf-8' # 내가요청하는 정보 : txt이며 html이고 글자는 utf-8이다.


    } 

    # {}{} : 타겟1,과 타켓2 쓰겠다는뜻
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers) 

    content = BeautifulSoup(response.content, 'html.parser') 
 
     #여기 가로 안 항목들에 환율정보 들어있음
    containers = content.find('span', {'data-test': 'instrument-price-last'}) 

    print(containers.text) 

 

get_exchange_rate('usd', 'krw') 