import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib #sending emails using the Simple Mail Transfer Protocol (SMTP).
import speedtest

EMAIL = 'me.ankittiwariid@gmail.com'
PASSWORD = 'vykkfajzstztqbxn'

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = round(st.download() / 1_000_000)  # convert to megabits per second
    upload_speed = round(st.upload() / 1_000_000)  # convert to megabits per second
    ping = st.results.ping
    
    print(f"Download speed: {download_speed} Mbps")
    print(f"Upload speed: {upload_speed} Mbps")
    print(f"Ping: {ping:.2f} ms")
    
    return download_speed, upload_speed




def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
