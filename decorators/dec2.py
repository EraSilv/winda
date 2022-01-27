
def get_web_site():
    import requests

    webpage = requests.get('http://super.kg')

    print(webpage.text)

get_web_site()