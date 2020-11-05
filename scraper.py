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

    with open("page_raw_html.html", "rb+") as html_file:

        html_file.write(page_html.encode("utf-8"))

    # print(html.find(".widget.product_short_description", first=True).text)

    # for a in html.find(".widget.product_short_description"):

    # print(a.text)

    for e in html.find(".discount_price"):
        print(e.text)

    for f in html.find(".regular_price"):
        print(f.text)

    return


def send_mail(user, pw):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user, pw)

    to = user
    subject = "Email Subject Line"
    body = "Email body"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(user, to, msg)

    print(f"Email sent to {to}")


if __name__ == "__main__":

    with open("encrypted.txt", "rb") as pw_file:
        key = pw_file.readline().strip()
        cipher_text = pw_file.readline()

    user = "matthew.bagin@gmail.com"
    pw = Hash.decrypt(key, cipher_text).decode("utf-8")

    scrape_page("https://fitnessavenue.ca/zsr3/plate-bar-trees")

    # print(f"user name is {user}")
    # print(f"password is {pw}")

    # send_mail(user, pw)
