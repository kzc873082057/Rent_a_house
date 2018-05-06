#_*_coding:utf-8_*
import requests
import os
import re
def stringListSave(savepath,filename,slist):
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    path = savepath+"\\"+filename+".txt"
    with open(path,"w+") as file:
        for s in slist:
            file.write("{0} \t\t {1}.html\n".format(s[1],s[0]))

def getPageInfo(start_url):
    response = requests.get(url=start_url)
    my_page = re.findall(
        r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', response.text,)
    return my_page
def newPageInfo(new_page):
    print("download:{0},{1}".format(new_page[0],new_page[1]))
    response = requests.get(url=new_page[1])
    new_page = re.findall(r'<td class=".*?">.*?<a href="(.*?)\.html".*?>(.*?)</a></td>',response.text)
    return new_page
if __name__ == "__main__":
    print("start....")
    start_url = "http://news.163.com/rank/"
    my_page = getPageInfo(start_url)
    for link in my_page:
         info = newPageInfo(link)
         stringListSave("./",link[0],info)


