from regexCoders import *

if __name__ == '__main__':
    # Ejecutar funciones de captura
    resultado = captureData(
        "https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs")
    apiRequestData(resultado)
