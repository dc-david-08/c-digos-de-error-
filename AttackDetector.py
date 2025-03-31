import requests
## Si el pais es Rusia, y el codigo es 200: es un ataque
def russiaAttackDetector(data):
    responseData = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/Web-Servers/Apache.txt").text
    for item in data:
        if item["code"] == '200' and item["country"] == "Russia":
            print(f"Se ha presentado un ataque desde {item['country']}: {item['code']}")

        if item["path"] in responseData:
            print(f"La ruta {item["path"]} es una ruta atacada")