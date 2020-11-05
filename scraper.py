from selenium import webdriver
from requests_html import HTML
import smtplib
import HashPassword as Hash


def scrape_page(url):

    browser = webdriver.Chrome(executable_path="chromedriver.exe")

    browser.get(url)
    page_html = browser.page_source

    # print(r.status_code)

    html = HTML(html=page_html)

    # with open("page_raw_html.html", "rb+") as html_file:

    #     html_file.write(page_html.encode("utf-8"))

    # print(html.find(".widget.product_short_description", first=True).text)

    prod_names = []
    prod_prices = []
    reg_or_disc = []
    in_stock = []

    for prod in html.find(".widget.product_preview.search"):
        for a in prod.find(".widget.product_short_description"):
            prod_names.append(a.text)

        for b in prod.find(".discount_price"):
            prod_prices.append(b.text)
            reg_or_disc.append("Regular Price")

        for c in prod.find(".regular_price"):
            prod_prices.append(c.text)
            reg_or_disc.append("Discounted Price")

        for d in prod.find(".widget.ProductPreviewNotPurchasableCustomMessage"):
            stock = True
            for e in d.find(".contactforshipping"):
                stock = False
            in_stock.append(stock)

    return in_stock[prod_names.index("AmStaff TT3102 Commercial Olympic/Standard Tree")]


def send_mail(user, pw):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user, pw)

    to = f"{user};cierrabutty@gmail.com"
    subject = "Plate Tree Stock"
    body = f"The plate tree you want is in stock! \n\nLink: https://fitnessavenue.ca/amstaff-tt3102-commercial-olympic-standard-tree"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(user, to, msg)

    print(f"Email sent to {to}")


if __name__ == "__main__":

    with open("encrypted.txt", "rb") as pw_file:
        key = pw_file.readline().strip()
        cipher_text = pw_file.readline()

    user = "matthew.bagin@gmail.com"
    pw = Hash.decrypt(key, cipher_text).decode("utf-8")

    # print(f"user name is {user}")
    # print(f"password is {pw}")

    if scrape_page("https://fitnessavenue.ca/zsr3/plate-bar-trees"):
        send_mail(user, pw)
