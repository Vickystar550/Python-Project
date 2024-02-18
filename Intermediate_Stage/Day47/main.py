from bs4 import BeautifulSoup
import requests
import smtplib
import lxml

PASSWORD = "enter here"
EMAIL = "enter here"

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
    }

r = requests.get(url=URL, headers=headers)

# saved this when the site worked, that is return the actual html of the tracked product instead
# of the reCaptcha page

# with open("amazon.html", 'w') as file:
#     file.write(r.text)


soup = BeautifulSoup(r.text, 'html.parser')


price_tag = soup.find(name='span', class_="a-offscreen")


if price_tag is None:
    # this is because Amazon may return a reCaptcha page which would contain our search tags....
    # thus returning a None to price_tag
    print("this worked")

    with open('amazon.html') as file:
        content = file.read()

    soup2 = BeautifulSoup(content, 'html.parser')
    price = float(soup2.find(name='span', class_="a-offscreen").get_text().split('$')[-1])
else:
    price = float(price_tag.get_text().split('$')[-1])


if price < 100:
    print("sending mail now")

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: Amazon Purchase"
                                f"\nYour tracked product price is now {price} below $100"
                                f"\nHead over to {URL} and make your purchase")
