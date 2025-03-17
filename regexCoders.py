import requests, json, re

def captureData(url):
    try:
        respuesta = requests.get(url).json()
        regexExpresion = "^(\d{3}\.\d{3}\.\d{3}\.\d{3}).*?\"\s(\d{3}).*?$"
        regex = re.findall(respuesta, regexExpresion)
        return regex
    except Exception as e:
        return None

print(captureData("https://github.com/elastic/examples/raw/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs"))



