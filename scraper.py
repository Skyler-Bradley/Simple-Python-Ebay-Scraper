import requests
from bs4 import BeautifulSoup
keyword = 'ounce gold'
headers = {'user agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0'}
for i in range(1,11):
    ebay = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw='+keyword+'&_pgns='+str(i), headers=headers)
    soup = BeautifulSoup(ebay.text, 'html.parser')
    items = soup.select('.s-item__link')
    print(items)
    '''<h3 class="s-item__title">1 OZ 500 Millls .999 Fine Gold Buffalo Bar Bullion</h3>'''
    print('ebay.status_code=',ebay.status_code)
    for item in items:
        print('item=',item.text)
    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)
    results = []
    boxes = soup.select('.clearfix.s-item__wrapper')
    for box in boxes:
        print('---')
        result = {}
        titles = box.select('.s-item__link')
        for title in titles:
            print('title=',title.text)
            result['title'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            print('price=',price.text)
            result['price'] = price.text
        print('result=',result)
        results.append(result)
    print('len(results)=',len(results))
    import json
    j = json.dumps(results)
    print('j=',j)
