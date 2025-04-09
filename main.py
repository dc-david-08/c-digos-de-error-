from regexCoders import *
from AttackDetector import *

if __name__ == '__main__':
    resultado = captureData(
        "https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs")
    respuesta = apiRequestData(resultado)
    russiaAttackDetector(respuesta)

