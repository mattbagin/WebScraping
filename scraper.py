from requests_html import HTML, HTMLSession
import smtplib
import HashPassword as Hash


def scrape_page(url,):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    session = HTMLSession()
    r = session.get(url, headers=headers,)
    # page_html = r.text

    # print(r.text.encode("utf-8"))

    with open("page_raw_html.html", "rb+") as html_file:

        # html_file.write(page_html.encode("utf-8"))

        source = html_file.read()
        html = HTML(html=source)

        # for li in html.find(".simple li", _encoding="utf-8"):
        #     print(li.text.encode("utf-8"))

    hd_prods = {
        "MicroPro Sienna 1 x 6 x 6'": "micropro-sienna-1-x-6-x-6-treated-wood-fence-board/1000790632",
    }

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

    print(f"user name is {user}")
    # print(f"password is {pw}")

    # send_mail(user, pw)
