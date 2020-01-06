import re
import time
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings()
import requests
from lxml import etree
from fake_useragent import UserAgent
ua = UserAgent().random
from bs4 import BeautifulSoup


class Amazon(object):

    def __init__(self):
        self.session = requests.session()
        self.url = "https://www.amazon.com/Best-Sellers-Office-Products-Drafting-Chairs/zgbs/office-products/1069142/ref=zg_bs_pg_2?_encoding=UTF8&pg=1"
        self.headers = {
            'authority': 'www.amazon.com',
            'method': 'GET',
            'path': '/gp/bestsellers/office-products/1069142/ref=pd_zg_hrsr_office-products',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8,en-US;q=0.9,en-GB;q=0.7,en;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1567579170389-406435; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=670F60FBB4C843DF-0F47DA9E551B2341; regStatus=pre-register; session-id=137-4066636-7694008; session-id-time=2082787201l; ubid-main=133-6579693-7864468; x-wl-uid=1XMQgy4JCyu0vPnAbu1NxiBYGjRqqMabWN/y2Negv7hdqWSucoNeifi1nLgcHqiE4i1lz0UdFDDw=; s_vn=1599115170803%26vn%3D2; aws-target-visitor-id=1567579170393-581387.22_45; s_dslv=1576813760650; s_nr=1576813760654-New; lc-main=en_US; i18n-prefs=USD; session-token=zP2PIAyP1CQY3h6EJR2Vd6ThBA4qk/EnPNGpexwAt6eYBnFmnLVgRVyXOezIK2uxDp8/PRzJqFCyapXW/A7pU251jFT3umv0tsjT18az0VfdIyZgP9YwtsvYHsvhORg8RhWu+bX1f/nBDIrc+VsR2+jR7ulZ2U8Ah0aPAIePJQwO97ml+Vst6QIMQOfSPywO; csm-hit=tb:s-Z0598RRJ1CX7V8N2H2NK|1578026937760&t:1578026937762&adb:adblk_no',
            'upgrade-insecure-requests': '1',
            'user-agent': ua
        }

        self.proxy_id = { "http": "http://61.135.155.82:443"}


    def parse_detail_page(self,urls):
        # try:
        for url in urls:
            time.sleep(5)
            detail_page_url = "https://www.amazon.com"+url
            print(detail_page_url)
            headers2 = {
                'authority': 'www.amazon.com',
                'method': 'GET',
                'path': url,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.8,en-US;q=0.9,en-GB;q=0.7,en;q=0.6',  # 设置英文权重 q
                'cache-control': 'max-age=0',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'upgrade-insecure-requests': '1',
                'user-agent': ua
            }
            cookie = {
                'x-wl-uid': '18oxX+wjus/n3+hF8W5yuIHtdtR8XY2M4zu3+ft4fbGS9zY8Am/jBZsjZSbanOI1dDjnbr9wlOso=',
                'i18n-prefs': 'USD',
                'sp-cdn': '"L5Z9:CN"',
                'csm-hit': 's-FPXZ5SSASHRF8RJRGK1Q|1577973946771',
                'session-token': 'tB5HBzmgSDyYUd8J726O/uYzvTwpi7q0Sea+EXysWkfYj/dzy1JSsSRT2w9/I/IykDZQL5MK2d6RRa4x/HVmESaKUKkC3XK2cRj7PSbQbIToA6p4NRLTPnfWa4kKQXB8G/WL1hSWS4ck8V6TcbygKl/G9m+VHY8fToSxc7Jc7rTwqhNobBtojbn6sagwQRx6U9fxhHidQoAcFTlH2VDmYdHYtyVgtXyOGhC0cIHGQnoQD0JNBBTI2hNHryDR8m4d',
                'ubid-main': '135-0544219-3333037',
                'session-id-time': '2082787201l',
                'session-id': '133-4057333-9935534',

            }

            response = self.session.get(detail_page_url, headers=headers2, cookies=cookie, timeout=10)
            time.sleep(5)
            detail_html = response.content.decode()


            with open('item.html','w+',encoding='utf-8') as f:
                f.write(detail_html)

            with open('item.html','r',encoding='utf-8') as f:
                detail_html = f.read()
            e = etree.HTML(detail_html)
            soup = BeautifulSoup(detail_html, 'lxml')
            # 商品名称
            #title = e.xpath('//h1[@id="title"]/span/text()')[0].strip()
            title = soup.select('#productTitle')[0].get_text().strip()

            # 商家
            soldby = re.findall('sellerProfileTriggerId">(.*?)<',detail_html,re.S)
            if soldby:
                soldby = soldby[0].strip().replace(' ','')
            else:
                soldby = re.findall('merchant-info.*?sold by (.*?)"',detail_html,re.S)
                if soldby:
                    soldby = soldby[0].strip().replace(' ','').replace('<spanclass=','').replace('</span></div><divclass=','').replace('\\r','')
                else:
                    soldby = re.findall('a-spacing-top-small a-link-normal.*?>(.*?)<',detail_html,re.S)
                    if soldby:
                        soldby = soldby[0].strip().replace(' ','')
                    else:
                        soldby = ''

            # 商品价格
            price = e.xpath('//tr[@id="comparison_price_row"]/td[1]/span/span[1]/text()')
            if price:
                price = price[0]
            else:
                # //*[@id="priceblock_ourprice"]/text()
                price = e.xpath('//span[@id="priceblock_ourprice"]/text()')
            # price = soup.select('#priceblock_ourprice')
            # if price:
            #     price = [0].get_text()
            # else:
            #     price = soup.select('#comparison_price_row > td.comparison_baseitem_column > span > span.a-offscreen')[0].get_text()

            # 评分
            rating = e.xpath('//span[@id="acrPopover"]/span[1]/a/i[1]/span/text()')
            rating = rating[0] if rating else ''
            #rating = soup.select('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star.a-star-4-5 > span')[0].get_text()

            # 用户评级数
            counts = e.xpath('//span[@id="acrCustomerReviewText"]/text()')
            counts = counts[0].strip() if counts else ''

            #counts = soup.select('#acrCustomerReviewText')[0].get_text()

            # 已回答数
            answer = e.xpath('//a[@id="askATFLink"]/span/text()')
            if answer:
                answer = e.xpath('//a[@id="askATFLink"]/span/text()')[0].strip()
                answer = re.findall('\d+', answer)[0]
            else:
                answer = ''

            # answer = soup.find('#askATFLink > span')
            # answer = answer[0].get_text() if answer else ''
            # print(soldby)
            print(soldby, price, rating, counts, answer,title)

        # except Exception as e:
        #     print(e)


    def get_detail_page_url(self):
        # 获取列表页
        response = self.session.get(self.url,headers=self.headers,timeout=10,verify=False)
        list_html = response.content.decode()
        e = etree.HTML(list_html)
        #print(list_html)
        time.sleep(5)
        urls = e.xpath('//*[@id="zg-ordered-list"]/li/span/div/span/a/@href')
        urls = set(urls)
        self.parse_detail_page(urls)

if __name__ == '__main__':
    amazon = Amazon()
    amazon.get_detail_page_url()

