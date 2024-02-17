from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

yc_soup = BeautifulSoup(yc_webpage, "html.parser")

anchors = [item.find("a") for item in yc_soup.find_all(name='span', attrs={"class": "titleline"})]

# --------------getting articles href links
article_link = [item.get('href') for item in anchors]
# print(article_link)

# ---------------getting articles text
article_text = [item.getText() for item in anchors]
# print(article_text)

# ---------------getting articles vote count
points = [int(score.getText().split(" ")[0]) for score in yc_soup.find_all(name='span', class_='score')]
# print(points)

# ---------------getting rank:
rank = [int(r.getText().split(".")[0]) for r in yc_soup.find_all(name='span', class_='rank')]
# print(rank)

# ---------------getting the index of the maximum vote
max_index = points.index(max(points))

print('-----------------------------------')
print(f'The popular article for today is no: {rank[max_index]}')
print(f'ARTICLE TEXT:\t{article_text[max_index]}')
print(f'ARTICLE LINK:\t{article_link[max_index]}')
print(f'POINTS:\t{max(points)} points')


# with open('website.html', 'r') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# print(soup.prettify())
#
# print("\n---------------")
# print(soup.body)
#
# all_anchor_tags = soup.find_all(name='a')
#
# print(all_anchor_tags)
#
# link = soup.find(id='name')
# print('\n________________________')
# print(link)
#
# for tag in all_anchor_tags:
#     print(tag.get('href'))
#     print(tag.getText())
#
# print('\n__________________\n')
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
# print('\n____________________')
# print(soup.select_one(selector='#name'))
#
# print('\n______________')
# print(soup.select(selector='.heading'))
