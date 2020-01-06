import requests


# url = "https://www.amazon.com/gp/p13n-shared/faceout-partial?asinMetadataKeys=adId&featureId=Zeitgeist&reftagPrefix=zg_bs_1069142&widgetTemplateClass=PI%3A%3AP13N%3A%3AViewTemplates%3A%3AList%3A%3AInfinite%3A%3APhone&faceoutTemplateClass=PI%3A%3AP13N%3A%3AZeitgeist%3A%3AViewTemplates%3A%3AProduct%3A%3APhone%3A%3AZeitgeistList&auiDeviceType=mobile&productDetailsTemplateClass=PI%3A%3AP13N%3A%3AZeitgeist%3A%3AViewTemplates%3A%3AProductDetails%3A%3APhone%3A%3AZeitgeistList&productDataFlavor=Faceout&asins=B08237FFCT%3A%2CB07X92ZGMB%3A%2CB07QFZ95R5%3A%2CB002Y2JDVE%3A%2CB082BV68W3%3A%2CB07QPW6C9B%3A%2CB07RFSRVJC%3A%2CB01N0SKDRB%3A%2CB07L85P7JT%3A%2CB07MGSGQLY%3A%2CB07V396WT5%3A%2CB07C83DDPX%3A%2CB081QG989D%3A%2CB076B7S6KT%3A%2CB000OV48ZI%3A%2CB072JQGQFL%3A%2CB07QK8NG9P%3A%2CB07YZPK91C%3A%2CB01C35LRHO%3A%2CB07RRL67QM%3A%2CB07VX1V3BL%3A%2CB01GBSDZBU%3A%2CB01N7JWY0S%3A%2CB07WQF75Z7%3A%2CB07YTWGFTB%3A%2CB07PRSYXQL%3A%2CB06VT2RKMB%3A%2CB00658RGPS%3A%2CB01MXZYH37%3A%2CB01I3OERH6%3A%2CB07MZPPB3T%3A%2CB007ZNWEYA%3A%2CB0183UTZT0%3A%2CB07QLF6F47%3A%2CB072JQD6QY%3A%2CB07QRZVJTK%3A%2CB00HG92L2S%3A%2CB00UV5TET2%3A%2CB07S3T1MQ1%3A%2CB01NGU19BM%3A&offset=20                "
#
# params = {
#     'asinMetadataKeys':	'adId',
#     'featureId':	'Zeitgeist',
#     'reftagPrefix':	'zg_bs_1069142',
#     'widgetTemplateClass':	'PI::P13N::ViewTemplates::List::Infinite::Phone',
#     'faceoutTemplateClass':	'PI::P13N::Zeitgeist::ViewTemplates::Product::Phone::ZeitgeistList',
#     'auiDeviceType':	'mobile',
#     'productDetailsTemplateClass':	'PI::P13N::Zeitgeist::ViewTemplates::ProductDetails::Phone::ZeitgeistList',
#     'productDataFlavor':	'Faceout',
#     'asins':	'B08237FFCT:,B07X92ZGMB:,B07QFZ95R5:,B002Y2JDVE:,B082BV68W3:,B07QPW6C9B:,B07RFSRVJC:,B01N0SKDRB:,B07L85P7JT:,B07MGSGQLY:,B07V396WT5:,B07C83DDPX:,B081QG989D:,B076B7S6KT:,B000OV48ZI:,B072JQGQFL:,B07QK8NG9P:,B07YZPK91C:,B01C35LRHO:,B07RRL67QM:,B07VX1V3BL:,B01GBSDZBU:,B01N7JWY0S:,B07WQF75Z7:,B07YTWGFTB:,B07PRSYXQL:,B06VT2RKMB:,B00658RGPS:,B01MXZYH37:,B01I3OERH6:,B07MZPPB3T:,B007ZNWEYA:,B0183UTZT0:,B07QLF6F47:,B072JQD6QY:,B07QRZVJTK:,B00HG92L2S:,B00UV5TET2:,B07S3T1MQ1:,B01NGU19BM:',
#     'offset':	'20'
# }
#
# headers = {
#         'authority': 'www.amazon.com',
#         'scheme': 'https',
#         'path': '/gp/p13n-shared/faceout-partial?asinMetadataKeys=adId&featureId=Zeitgeist&reftagPrefix=zg_bs_1069142&widgetTemplateClass=PI%3A%3AP13N%3A%3AViewTemplates%3A%3AList%3A%3AInfinite%3A%3APhone&faceoutTemplateClass=PI%3A%3AP13N%3A%3AZeitgeist%3A%3AViewTemplates%3A%3AProduct%3A%3APhone%3A%3AZeitgeistList&auiDeviceType=mobile&productDetailsTemplateClass=PI%3A%3AP13N%3A%3AZeitgeist%3A%3AViewTemplates%3A%3AProductDetails%3A%3APhone%3A%3AZeitgeistList&productDataFlavor=Faceout&asins=B08237FFCT%3A%2CB07X92ZGMB%3A%2CB07QFZ95R5%3A%2CB002Y2JDVE%3A%2CB082BV68W3%3A%2CB07QPW6C9B%3A%2CB07RFSRVJC%3A%2CB01N0SKDRB%3A%2CB07L85P7JT%3A%2CB07MGSGQLY%3A%2CB07V396WT5%3A%2CB07C83DDPX%3A%2CB081QG989D%3A%2CB076B7S6KT%3A%2CB000OV48ZI%3A%2CB072JQGQFL%3A%2CB07QK8NG9P%3A%2CB07YZPK91C%3A%2CB01C35LRHO%3A%2CB07RRL67QM%3A%2CB07VX1V3BL%3A%2CB01GBSDZBU%3A%2CB01N7JWY0S%3A%2CB07WQF75Z7%3A%2CB07YTWGFTB%3A%2CB07PRSYXQL%3A%2CB06VT2RKMB%3A%2CB00658RGPS%3A%2CB01MXZYH37%3A%2CB01I3OERH6%3A%2CB07MZPPB3T%3A%2CB007ZNWEYA%3A%2CB0183UTZT0%3A%2CB07QLF6F47%3A%2CB072JQD6QY%3A%2CB07QRZVJTK%3A%2CB00HG92L2S%3A%2CB00UV5TET2%3A%2CB07S3T1MQ1%3A%2CB01NGU19BM%3A&offset=20',
#         'accept': 'text/html,*/*',
#         'x-requested-with': 'XMLHttpRequest',
#         'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; vivo X9 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.4.2',
#         'referer': 'https://www.amazon.com/gp/bestsellers/office-products/1069142/ref=pd_zg_hrsr_office-products',
#         'accept-encoding': 'gzip, deflate',
#         'accept-language': 'zh-CN,en-US;q=0.9',
#         # cookie: x-wl-uid=18oxX+wjus/n3+hF8W5yuIHtdtR8XY2M4zu3+ft4fbGS9zY8Am/jBZsjZSbanOI1dDjnbr9wlOso=
#         # cookie: i18n-prefs=USD
#         # cookie: sp-cdn="L5Z9:CN"
#         # cookie: session-token=tB5HBzmgSDyYUd8J726O/uYzvTwpi7q0Sea+EXysWkfYj/dzy1JSsSRT2w9/I/IykDZQL5MK2d6RRa4x/HVmESaKUKkC3XK2cRj7PSbQbIToA6p4NRLTPnfWa4kKQXB8G/WL1hSWS4ck8V6TcbygKl/G9m+VHY8fToSxc7Jc7rTwqhNobBtojbn6sagwQRx6U9fxhHidQoAcFTlH2VDmYdHYtyVgtXyOGhC0cIHGQnoQD0JNBBTI2hNHryDR8m4d
#         # cookie: csm-hit=tb:s-V8Z47DERK2RW8Y1EASX0|1578015066435&t:1578015068032&adb:adblk_no
#         # cookie: ubid-main=135-0544219-3333037
#         # cookie: session-id-time=2082787201l
#         # cookie: session-id=133-4057333-9935534
#
# }
# cookie = {
#         'x-wl-uid':	'18oxX+wjus/n3+hF8W5yuIHtdtR8XY2M4zu3+ft4fbGS9zY8Am/jBZsjZSbanOI1dDjnbr9wlOso=',
#         'i18n-prefs':	'USD',
#         'sp-cdn':	'"L5Z9:CN"',
#         'csm-hit':	'tb:s-V8Z47DERK2RW8Y1EASX0|1578015066435&t:1578015068032&adb:adblk_no',
#         'session-token':	'tB5HBzmgSDyYUd8J726O/uYzvTwpi7q0Sea+EXysWkfYj/dzy1JSsSRT2w9/I/IykDZQL5MK2d6RRa4x/HVmESaKUKkC3XK2cRj7PSbQbIToA6p4NRLTPnfWa4kKQXB8G/WL1hSWS4ck8V6TcbygKl/G9m+VHY8fToSxc7Jc7rTwqhNobBtojbn6sagwQRx6U9fxhHidQoAcFTlH2VDmYdHYtyVgtXyOGhC0cIHGQnoQD0JNBBTI2hNHryDR8m4d',
#         'ubid-main':	'135-0544219-3333037',
#         'session-id-time':	'2082787201l',
#         'session-id':	'133-4057333-9935534',
#
#     }
#
# response = requests.get(url,params=params,headers=headers)
# print(response.content.decode())











url = "https://www.amazon.com/Drafting-Chair-Office-Standing-Table/dp/B07XLMKXLM/ref=zg_bs_1069142_1?_encoding=UTF8&psc=1&refRID=593464RG3N0Q7P7C0MSR"

cookie = {
        'x-wl-uid':	'18oxX+wjus/n3+hF8W5yuIHtdtR8XY2M4zu3+ft4fbGS9zY8Am/jBZsjZSbanOI1dDjnbr9wlOso=',
        'i18n-prefs':	'USD',
        'sp-cdn':	'"L5Z9:CN"',
        'csm-hit':	's-FPXZ5SSASHRF8RJRGK1Q|1577973946771',
        'session-token':	'tB5HBzmgSDyYUd8J726O/uYzvTwpi7q0Sea+EXysWkfYj/dzy1JSsSRT2w9/I/IykDZQL5MK2d6RRa4x/HVmESaKUKkC3XK2cRj7PSbQbIToA6p4NRLTPnfWa4kKQXB8G/WL1hSWS4ck8V6TcbygKl/G9m+VHY8fToSxc7Jc7rTwqhNobBtojbn6sagwQRx6U9fxhHidQoAcFTlH2VDmYdHYtyVgtXyOGhC0cIHGQnoQD0JNBBTI2hNHryDR8m4d',
        'ubid-main':	'135-0544219-3333037',
        'session-id-time':	'2082787201l',
        'session-id':	'133-4057333-9935534',

    }
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; vivo X9 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.4.2'
}

response = requests.request("GET", url, headers=headers)

print(response.content.decode())










