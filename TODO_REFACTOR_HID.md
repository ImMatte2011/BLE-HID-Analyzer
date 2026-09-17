# TODO_REFACTOR_HID.md

# BLE HID Analyzer - Stato lavori

## Struttura scelta

[x] Classi principali lasciate nel file principale
[x] Separazione solo dei moduli HID grandi/statici
[x] Nessuna frammentazione inutile delle classi per MicroPython

---

# File HID aggiunti

## hid_maps.py

[x] Creato modulo mappe HID esterno

Contiene:

[x] HID Keyboard Usage Map base
[x] Consumer Control Map base

Da aggiungere:

[ ] Completare tutte le USB HID Usage Tables
[ ] Keyboard F1-F24
[ ] Keypad completo
[ ] Print Screen
[ ] Scroll Lock
[ ] Pause
[ ] Insert
[ ] Menu/Application
[ ] Modifier sinistro/destro
[ ] System Control
[ ] Generic Desktop
[ ] Gamepad
[ ] Joystick
[ ] Digitizer
[ ] Simulation

---

## hid_descriptor.py

[x] Creato modulo parser Report Descriptor

Da completare:

[ ] Gestione completa Main Items
[ ] Input
[ ] Output
[ ] Feature
[ ] Gestione Global Items
[ ] Usage Page
[ ] Logical Min/Max
[ ] Physical Min/Max
[ ] Report Size
[ ] Report Count
[ ] Report ID
[ ] Gestione Local Items
[ ] Usage
[ ] Usage Min
[ ] Usage Max
[ ] Parsing signed values

---

# Collegamento al programma principale

## hid_maps.py

[ ] Rimuovere:

```
_HID_KEYMAP
_CONSUMER_MAP
```

dal file principale.

[ ] Aggiungere import:

```python
from hid_maps import HID_KEYMAP, CONSUMER_MAP
```

[ ] Aggiornare:

```
decode_key()
_parse_consumer()
```

per usare le nuove mappe.

---

## hid_descriptor.py

[ ] Collegare durante discovery HID.

Da aggiungere:

* lettura UUID 0x2A4B Report Descriptor
* parsing descriptor
* salvataggio risultato nel JSON

---

# Parser eventi

## HIDReportParser attuale

[x] Boot Keyboard
[x] Consumer Control
[x] Mouse

Da migliorare:

[ ] NKRO Keyboard
[ ] Report ID multipli
[ ] Keyboard custom BLE
[ ] Gamepad
[ ] Joystick
[ ] Digitizer

---

# NKRO Keyboard

[ ] Implementare decoder bitmap.

Supportare:

[ ] 6KRO Boot Keyboard
[ ] NKRO bitmap
[ ] Modifier
[ ] Report ID

---

# Nuovi decoder

[ ] Gamepad decoder
[ ] Joystick decoder
[ ] Digitizer decoder
[ ] Vendor decoder

---

# HID Services

[ ] Battery Service

UUID:

```
0x180F
```

[ ] Battery Level

```
0x2A19
```

[ ] HID Information

```
0x2A4A
```

[ ] Protocol Mode

```
0x2A4E
```

---

# Report JSON

Aggiungere:

[ ] Report Descriptor analizzato
[ ] Usage Page
[ ] Usage
[ ] Report Fields
[ ] Battery
[ ] HID Information
[ ] Protocol Mode

---

# Test finali

[ ] Tastiera BLE standard
[ ] Tastiera FN
[ ] Tastiera NKRO
[ ] Tastiera gaming
[ ] Mouse BLE
[ ] Gamepad BLE
[ ] Joystick BLE
[ ] Telecomando multimediale

---

# Ordine consigliato prossimi passi

1. [ ] Finire hid_maps.py
2. [ ] Collegare hid_maps.py al parser attuale
3. [ ] Finire hid_descriptor.py
4. [ ] Collegare Report Descriptor discovery
5. [ ] Implementare NKRO
6. [ ] Aggiungere gamepad/joystick
