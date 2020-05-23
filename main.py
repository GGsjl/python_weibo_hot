import requests
import re
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from imageio import imread
import time

url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'

def get_hot():
    def get_text():
        try:
            r = requests.get(url)
            r.raise_for_status
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print('wrong')

    text = get_text()

    #result = re.search(r'^<a href=(.+)</a>$', text)
    pattern = re.compile(r'<a href="/weibo(.+)</a>')
    results = pattern.findall(text)
    title = []
    for result in results:
        title.append(result[result.find('>')+1:])

    s = ""
    for i in title:
        s += i
        s += '。'
    
    try:
        with open(r'C:\Users\Song\Desktop\s.txt', 'a+') as f:
            f.write(s)
        print('ok')
    except:
        print('wrong')



def draw():
    with open(r'C:\Users\Song\Desktop\s.txt','r',encoding="ANSI") as file1:
        content = "".join(file1.readlines())
    ##然后使用jieba模块进行对文本分词整理
    content_after = "/".join(jieba.cut(content))
    wc = WordCloud(font_path="msyh.ttc",background_color="black",max_words=100,max_font_size=100, width=1500,height=1500).generate(content_after)
    ##使用matplotlib的pyplot来进行最后的渲染出图.
    plt.imshow(wc)
    ##目标文件另存为这个名录下
    wc.to_file('C:\\Users\\Song\\Desktop\\pic.png')

def main():
    get_hot()
    draw()

tim = time.strftime('%m.%d_%H:%M', time.localtime(time.time()))
while(tim < '05.23_15:36'):
    main()
    time.sleep(1800)
    tim = time.strftime('%m.%d_%H:%M', time.localtime(time.time()))