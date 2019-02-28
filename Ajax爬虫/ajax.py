from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'#请求的url的前半部分
headers = {#请求头
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
def get_page(page):
    params = {#定义参数的字典
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)#调用urlencode函数将参数转化为URL的GET请求参数
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.json(), page#将内容解析成JSON #获得源码是response.text
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json, page:int):
    if json:
        items = json.get('data').get('cards')
        for index,item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
        #for item in items:
                it = item.get('mblog',{})
                weibo = {}
                weibo['id'] = it.get('id')#微博id
                weibo['text'] = pq(it.get('text')).text()#微博正文 #借助pyquery将正文中的HTML标签去掉
                weibo['attitudes'] = it.get('attitudes_count')#赞数
                weibo['comments'] = it.get('comments_count')#评论数
                weibo['reposts'] = it.get('reposts_count')#转发数
                yield weibo

if __name__ == '__main__':
    count = 0
    for page in range(1,11):#一共有10页
        print('page : ' + str(page))
        json = get_page(page)#获得JSON
        results = parse_page(*json)#json是一个元组，加*可以拆分元组
        for result in results:#打印每条微博的信息
            print(result)
            count += 1
    print(count)