# boot.py -- run on boot-up
import bluetooth
import gc

# Accendiamo subito la radio sulla RAM totalmente vergine
print("Inizializzazione preventiva BLE...")
ble = bluetooth.BLE()
ble.active(True)

# Puliamo la memoria residua
gc.collect()
print("BLE Attivo. Avvio del sistema...")