#coding=utf-8
import requests
import urllib.parse
import re
# 小区名字  地址  年份 房价 房屋总数

def page_index_get(num):
    headers={'Host': 'wh.lianjia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'}
    if int(num)==1:
        url='https://wh.lianjia.com/xiaoqu/?from=rec'
    else:
        url='https://wh.lianjia.com/xiaoqu/pg'+str(num)+'/?from=rec'
    response=requests.get(url=url,headers=headers).text
    pattern=re.compile('<li.*?<a class="img" href="(.*?)".*?info.*?title',re.S)
    results=re.findall(pattern,response)
    try:
        with open('WuHanUrl.txt','a+') as f:
            for result in results:
                if result!='<%=url%>':
                    f.write(result)
                    f.write('\n')
        print('[+]Page'+str(num)+'写入成功')
    except:
        print('[-]写入失败')

def XiaoQu_page(url,num):
    headers={'Host': 'wh.lianjia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'}
    #print(url)
    response=requests.get(url=url,headers=headers).text
    #print(response)
    pattern=re.compile('<h1 class.*?detailTitle">(.*?)</h1>.*?detailDesc">(.*?)</div>.*?class="fl">.*?xiaoquUnitPrice">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>.*?xiaoquInfoContent">(.*?)</span>',re.S)
    results=re.findall(pattern,response)
    #print(results)
    with open('WuHanXiaoQu.txt','a+',encoding='utf-8') as ff:
        for result in results:
            #print("test")
            ff.write(result[0]+','+result[1]+','+result[2]+','+result[3]+','+result[5]+','+result[9]+'\n')
            print('[+]XiaoQu'+str(num)+'写入成功')

def main():
    #url='https://wh.lianjia.com/xiaoqu/?from=rec'
    #response=requests.get(url=url,headers=headers).text
    #pattern=re.compile('<h2.*?<span>(.*?)</span>',re.S)
    #results=re.findall(pattern,response)
    #print('武汉小区共',results[1],'个')
    #with open('WuHanUrl.txt','a+') as f:
    #    for result in results:
    #        if result!='<%=url%>':
    #            f.write(results[1])
    #            f.write('\n')
    #pattern2=re.compile('<h2.*?<span>(.*?)</span>',re.S)
    #results=re.findall(pattern2,response)
    #print(results[1])
    '''
    #获取所有武汉小区单独页面url
    for i in range(1,31):
        page_index_get(i)
    '''
    #XiaoQu_page('https://wh.lianjia.com/xiaoqu/3711062832746/',1)

    with open('WuHanUrl1.txt','r') as srpihot:
        j=1
        for url_name in srpihot.readlines():
            #print(url_name+'   '+str(j))
            url_name=url_name.strip('\n')
            XiaoQu_page(url_name,j)
            j+=1
    
if __name__=="__main__":
    main()