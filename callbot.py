
from WebScraping import precioInicial
from WebScraping import precioDeseado

import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '1956091947:AAFBwuu5LuItGTnMytVSvwWeebWCyOWGw_U'
    bot_chatID = '1750265330'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



if precioInicial < precioDeseado:
    test = telegram_bot_sendtext(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en: {'$' + str(precioInicial)}\nEnlace: https://listado.mercadolibre.com.ec/como-actualizacion-pc-amd-ryzen-3-3200g-%C3%BE-a320-%C3%BE-8gb#D[A:como%20actualizacion%20pc%20amd%20ryzen%203%203200g%20+%20A320%20+%208GB]")

else:
    test = telegram_bot_sendtext("No hay oferta")


