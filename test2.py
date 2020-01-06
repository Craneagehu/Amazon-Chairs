import re
from bs4 import BeautifulSoup
from lxml import etree

with open('item.html','r',encoding='utf-8') as f:
    html = f.read().replace('<!--','').replace(' -->','')
    e = etree.HTML(html)
    soup = BeautifulSoup(html,'lxml')
    title = e.xpath('//h1[@id="title"]/span/text()')[0].strip()

    # soldby = e.xpath('//tr[@id="comparison_shipping_info_row"]//text()')
    soldby = soup.select('#comparison_sold_by_row > td.comparison_baseitem_column > span')[0].get_text()
    print(soldby)
    price = e.xpath('//tr[@id="comparison_price_row"]/td[1]/span/span[1]/text()')
    if price:
        price = price[0]
    else:
        price = e.xpath('//*[@id="priceblock_ourprice"]/text()')[0]

    rating = e.xpath('//span[@id="acrPopover"]/span[1]/a/i[1]/span/text()')
    if rating:
        rating = rating[0]
    else:
        rating = ''

    counts = e.xpath('//span[@id="acrCustomerReviewText"]/text()')
    if counts:
        counts = counts[0].strip()
        counts = re.findall('\d+',counts)[0]
    else:
        counts = ""

    answer = e.xpath('//a[@id="askATFLink"]/span/text()')
    if answer:
        answer = [0].strip()
        answer  = re.findall('\d+',answer)[0]
    else:
        answer = ""
    print(title,soldby,price,rating,counts,answer)





