import time
from datetime import datetime
import os

topic= "water-reminder"
message= "bevi l'acqua"

#loop infinito
while True:
    current_time = datetime.now().hour #check time

    if 8 <= current_time < 20:
        print("Sto inviando il messaggio...")
        # Sintassi: ntfy -t "Titolo" send "Messaggio"
        os.system(f'notify-send -a "{topic}" "{message}"')       
    time.sleep(1800)
