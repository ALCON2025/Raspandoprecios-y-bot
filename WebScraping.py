from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://listado.mercadolibre.com.ec/como-actualizacion-pc-amd-ryzen-3-3200g-%C3%BE-a320-%C3%BE-8gb#D[A:como%20actualizacion%20pc%20amd%20ryzen%203%203200g%20+%20A320%20+%208GB]")


soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find("span", {"class":"price-tag-fraction"})
precionInicio_text = resultado.text
precioInicial = float(precionInicio_text)

precioDeseado = 560

if precioInicial < precioDeseado:
    print("Hay oferta")
else:
    print("No hay oferta")
