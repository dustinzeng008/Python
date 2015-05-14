import urllib.request
from urllib.error import URLError
import re

def visit_url(url,  domain):
    global crawler_backlog
    global crawlerDataList
    myTuple=()
    if(len(crawler_backlog) > 100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        #print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code = page.getcode()
        if(code == 200):
            content = page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_published_date = re.compile(
                '<meta name="published-date" content="(?P<published_date>(.*))" />')
            regexp_url = re.compile("http://" + domain + "[/\w+]*")

            result_title = regexp_title.search(content_string, re.IGNORECASE)
            if result_title:
                title = result_title.group("title")
                #print(title)

            result_date = regexp_published_date.search(
                content_string, re.IGNORECASE)
            if result_date:
                published_date = result_date .group("published_date")
                #print(published_date)
            if result_title and result_date:
                myTuple = (url, title, published_date)
                crawlerDataList.append(myTuple)

            for (urls) in re.findall(regexp_url, content_string):
                if(urls not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)
    except URLError as e:
        print("error")

crawlerDataList=[]
crawler_backlog = {}
seed = "http://www.newhaven.edu/"
crawler_backlog[seed] = 0
visit_url(seed, "www.newhaven.edu")

def getCrawlerData():
    return crawlerDataList
