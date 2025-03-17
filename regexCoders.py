import requests, json, re

def captureData(url):
    try:
        respuesta = requests.get(url).json()
        regexExpresion = "^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\"\s(\d{3}).*?$"
        regex = re.findall(regexExpresion, respuesta)
        return regex
    except Exception as e:
        return None

def apiRequestData(data):
    URI = "https://ipinfo.io/"
    for ip, code in data:
        print(f"{ip}: {code}")


resultado = captureData("https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs")
apiRequestData(resultado)



