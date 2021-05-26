from bs4 import BeautifulSoup
import requests
import sys


def get_article(url, line):
    page = requests.get(url)
    if page.status_code != 200:
        return str(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    article_text = ''
    for p in soup('p'):
        text = p.get_text()
        if len(text) <= line: 
            article_text += text + '\n'
        else:
            line_length_count = 0
            line_text = ''
            for word in text.split(' '):
                line_length_count+=len(word)
                if len(line_text + word) >= line:
                    article_text += line_text + '\n'
                    line_text = ''
                line_text += word+' '
            article_text += line_text + '\n'                 
    return article_text

if __name__ == '__main__':
    line = 100
    url = str(sys.argv[1])
    text = get_article(url, line)
    print(text)