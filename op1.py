from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'youtube link'])

for article in soup.find_all('article'):
    try:
        headline = article.h2.a.text
        print(f'---{headline}---')
        summary = article.find('div', class_='entry-content').p.text
        print(summary)
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
        print(yt_link)
    except Exception as e:
        yt_link = None
    print()
    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()