## Si el pais es Rusia, y el codigo es 200: es un ataque
def russiaAttackDetector(data):
    for item in data:
        if item["code"] == '200' and item["country"] == "Russia":
            print(f"Se ha presentado un ataque desde {item['Country']}: {item['code']}")