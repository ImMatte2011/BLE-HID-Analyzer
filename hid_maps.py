"""
USB HID Usage Tables

Reference:
USB HID Usage Tables Specification

This module contains lookup tables used by the BLE HID Analyzer.

Everything here is static data and helper functions.
"""

# ==========================================================
# Report Types
# ==========================================================

_REPORT_TYPE = {
    0x01: "INPUT",
    0x02: "OUTPUT",
    0x03: "FEATURE",
}

# ==========================================================
# Keyboard Modifiers
# ==========================================================

_HID_MODIFIERS = {
    0x01: "LEFT_CTRL",
    0x02: "LEFT_SHIFT",
    0x04: "LEFT_ALT",
    0x08: "LEFT_GUI",
    0x10: "RIGHT_CTRL",
    0x20: "RIGHT_SHIFT",
    0x40: "RIGHT_ALT",
    0x80: "RIGHT_GUI",
}

# ==========================================================
# HID Usage Pages
# ==========================================================

_HID_USAGE_PAGES = {

    0x00: "Undefined",

    0x01: "Generic Desktop",

    0x02: "Simulation Controls",

    0x03: "VR Controls",

    0x04: "Sport Controls",

    0x05: "Game Controls",

    0x06: "Generic Device Controls",

    0x07: "Keyboard / Keypad",

    0x08: "LED",

    0x09: "Button",

    0x0A: "Ordinal",

    0x0B: "Telephony",

    0x0C: "Consumer",

    0x0D: "Digitizer",

    0x0E: "Haptics",

    0x0F: "Physical Interface Device",

    0x10: "Unicode",

    0x11: "SoC",

    0x12: "Eye and Head Trackers",

    0x14: "Auxiliary Display",

    0x20: "Sensors",

    0x40: "Medical Instruments",

    0x41: "Braille Display",

    0x59: "Lighting and Illumination",

    0x80: "Monitor",

    0x84: "Power",

    0x8C: "Bar Code Scanner",

    0x8D: "Scale",

    0x8E: "Magnetic Stripe Reader",

    0x8F: "Camera Control",

    0x90: "Arcade",

    0x91: "Gaming Device",

    0x92: "FIDO Alliance",

}

# ==========================================================
# Keyboard Helpers
# ==========================================================

def shifted(modifier):
    return bool(modifier & 0x22)


def modifier_str(modifier):

    parts = []

    for bit, name in _HID_MODIFIERS.items():
        if modifier & bit:
            parts.append(name)

    return " + ".join(parts) if parts else "NONE"


def decode_key(keycode, modifier=0):

    entry = _HID_KEYBOARD_MAP.get(keycode)

    if entry is None:
        return "0x%02X" % keycode

    return entry[1] if shifted(modifier) else entry[0]


def decode_consumer(usage):

    return _HID_CONSUMER_MAP.get(
        usage,
        "0x%04X" % usage
    )


def decode_generic_desktop(usage):

    return _HID_GENERIC_DESKTOP_MAP.get(
        usage,
        "0x%02X" % usage
    )


def decode_system(usage):

    return _HID_SYSTEM_CONTROL_MAP.get(
        usage,
        "0x%02X" % usage
    )


def decode_led(usage):

    return _HID_LED_MAP.get(
        usage,
        "0x%02X" % usage
    )

# ==========================================================
# Keyboard / Keypad Usage Page (0x07)
# ==========================================================

_HID_KEYBOARD_MAP = {

    # Reserved
    0x00: (None, None),

    # Error codes
    0x01: ("ERROR_ROLLOVER", "ERROR_ROLLOVER"),
    0x02: ("POST_FAIL", "POST_FAIL"),
    0x03: ("ERROR_UNDEFINED", "ERROR_UNDEFINED"),

    # Alphabet
    0x04: ("a", "A"),
    0x05: ("b", "B"),
    0x06: ("c", "C"),
    0x07: ("d", "D"),
    0x08: ("e", "E"),
    0x09: ("f", "F"),
    0x0A: ("g", "G"),
    0x0B: ("h", "H"),
    0x0C: ("i", "I"),
    0x0D: ("j", "J"),
    0x0E: ("k", "K"),
    0x0F: ("l", "L"),
    0x10: ("m", "M"),
    0x11: ("n", "N"),
    0x12: ("o", "O"),
    0x13: ("p", "P"),
    0x14: ("q", "Q"),
    0x15: ("r", "R"),
    0x16: ("s", "S"),
    0x17: ("t", "T"),
    0x18: ("u", "U"),
    0x19: ("v", "V"),
    0x1A: ("w", "W"),
    0x1B: ("x", "X"),
    0x1C: ("y", "Y"),
    0x1D: ("z", "Z"),

    # Numbers
    0x1E: ("1", "!"),
    0x1F: ("2", "@"),
    0x20: ("3", "#"),
    0x21: ("4", "$"),
    0x22: ("5", "%"),
    0x23: ("6", "^"),
    0x24: ("7", "&"),
    0x25: ("8", "*"),
    0x26: ("9", "("),
    0x27: ("0", ")"),

    # Basic keys
    0x28: ("ENTER", "ENTER"),
    0x29: ("ESC", "ESC"),
    0x2A: ("BACKSPACE", "BACKSPACE"),
    0x2B: ("TAB", "TAB"),
    0x2C: ("SPACE", "SPACE"),

    # Symbols
    0x2D: ("-", "_"),
    0x2E: ("=", "+"),
    0x2F: ("[", "{"),
    0x30: ("]", "}"),
    0x31: ("\\", "|"),

    # Non-US key
    0x32: ("NONUS_#", "NONUS_~"),

    0x33: (";", ":"),
    0x34: ("'", "\""),
    0x35: ("`", "~"),
    0x36: (",", "<"),
    0x37: (".", ">"),
    0x38: ("/", "?"),

    0x39: ("CAPSLOCK", "CAPSLOCK"),

    # Function keys
    0x3A: ("F1", "F1"),
    0x3B: ("F2", "F2"),
    0x3C: ("F3", "F3"),
    0x3D: ("F4", "F4"),
    0x3E: ("F5", "F5"),
    0x3F: ("F6", "F6"),
    0x40: ("F7", "F7"),
    0x41: ("F8", "F8"),
    0x42: ("F9", "F9"),
    0x43: ("F10", "F10"),
    0x44: ("F11", "F11"),
    0x45: ("F12", "F12"),

    # Navigation
    0x46: ("PRINTSCREEN", "PRINTSCREEN"),
    0x47: ("SCROLLLOCK", "SCROLLLOCK"),
    0x48: ("PAUSE", "PAUSE"),
    0x49: ("INSERT", "INSERT"),
    0x4A: ("HOME", "HOME"),
    0x4B: ("PAGEUP", "PAGEUP"),
    0x4C: ("DELETE", "DELETE"),
    0x4D: ("END", "END"),
    0x4E: ("PAGEDOWN", "PAGEDOWN"),
    0x4F: ("RIGHT", "RIGHT"),
    0x50: ("LEFT", "LEFT"),
    0x51: ("DOWN", "DOWN"),
    0x52: ("UP", "UP"),

    # Keypad
    0x53: ("NUMLOCK", "NUMLOCK"),

    0x54: ("KP/", "KP/"),
    0x55: ("KP*", "KP*"),
    0x56: ("KP-", "KP-"),
    0x57: ("KP+", "KP+"),
    0x58: ("KPENTER", "KPENTER"),

    0x59: ("KP1", "KP1"),
    0x5A: ("KP2", "KP2"),
    0x5B: ("KP3", "KP3"),
    0x5C: ("KP4", "KP4"),
    0x5D: ("KP5", "KP5"),
    0x5E: ("KP6", "KP6"),
    0x5F: ("KP7", "KP7"),
    0x60: ("KP8", "KP8"),
    0x61: ("KP9", "KP9"),
    0x62: ("KP0", "KP0"),
    0x63: ("KP.", "KP."),

    0x64: ("NONUS_\\", "NONUS_|"),
    0x65: ("APPLICATION", "APPLICATION"),
    0x66: ("POWER", "POWER"),
    0x67: ("KP=", "KP="),

    # Extended Function Keys
    0x68: ("F13", "F13"),
    0x69: ("F14", "F14"),
    0x6A: ("F15", "F15"),
    0x6B: ("F16", "F16"),
    0x6C: ("F17", "F17"),
    0x6D: ("F18", "F18"),
    0x6E: ("F19", "F19"),
    0x6F: ("F20", "F20"),
    0x70: ("F21", "F21"),
    0x71: ("F22", "F22"),
    0x72: ("F23", "F23"),
    0x73: ("F24", "F24"),

    # ======================================================
    # Keyboard extended controls
    # ======================================================

    0x74: ("EXECUTE", "EXECUTE"),
    0x75: ("HELP", "HELP"),
    0x76: ("MENU", "MENU"),
    0x77: ("SELECT", "SELECT"),
    0x78: ("STOP", "STOP"),
    0x79: ("AGAIN", "AGAIN"),
    0x7A: ("UNDO", "UNDO"),
    0x7B: ("CUT", "CUT"),
    0x7C: ("COPY", "COPY"),
    0x7D: ("PASTE", "PASTE"),
    0x7E: ("FIND", "FIND"),
    0x7F: ("MUTE", "MUTE"),
    0x80: ("VOLUME_UP", "VOLUME_UP"),
    0x81: ("VOLUME_DOWN", "VOLUME_DOWN"),

    0x82: ("LOCKING_CAPS_LOCK", "LOCKING_CAPS_LOCK"),
    0x83: ("LOCKING_NUM_LOCK", "LOCKING_NUM_LOCK"),
    0x84: ("LOCKING_SCROLL_LOCK", "LOCKING_SCROLL_LOCK"),

    0x85: ("KP_COMMA", "KP_COMMA"),
    0x86: ("KP_EQUAL_SIGN", "KP_EQUAL_SIGN"),

    # International keyboard
    0x87: ("INTERNATIONAL1", "INTERNATIONAL1"),
    0x88: ("INTERNATIONAL2", "INTERNATIONAL2"),
    0x89: ("INTERNATIONAL3", "INTERNATIONAL3"),
    0x8A: ("INTERNATIONAL4", "INTERNATIONAL4"),
    0x8B: ("INTERNATIONAL5", "INTERNATIONAL5"),
    0x8C: ("INTERNATIONAL6", "INTERNATIONAL6"),
    0x8D: ("INTERNATIONAL7", "INTERNATIONAL7"),
    0x8E: ("INTERNATIONAL8", "INTERNATIONAL8"),
    0x8F: ("INTERNATIONAL9", "INTERNATIONAL9"),

    # Language keys
    0x90: ("LANG1", "LANG1"),
    0x91: ("LANG2", "LANG2"),
    0x92: ("LANG3", "LANG3"),
    0x93: ("LANG4", "LANG4"),
    0x94: ("LANG5", "LANG5"),
    0x95: ("LANG6", "LANG6"),
    0x96: ("LANG7", "LANG7"),
    0x97: ("LANG8", "LANG8"),
    0x98: ("LANG9", "LANG9"),

    # Alternate erase / editing
    0x99: ("ALTERNATE_ERASE", "ALTERNATE_ERASE"),
    0x9A: ("SYSREQ", "SYSREQ"),
    0x9B: ("CANCEL", "CANCEL"),
    0x9C: ("CLEAR", "CLEAR"),
    0x9D: ("PRIOR", "PRIOR"),
    0x9E: ("RETURN", "RETURN"),
    0x9F: ("SEPARATOR", "SEPARATOR"),

    0xA0: ("OUT", "OUT"),
    0xA1: ("OPER", "OPER"),
    0xA2: ("CLEAR_AGAIN", "CLEAR_AGAIN"),
    0xA3: ("CRSEL", "CRSEL"),
    0xA4: ("EXSEL", "EXSEL"),

    # ======================================================
    # Keypad extended functions
    # ======================================================

    0xB0: ("KP00", "KP00"),
    0xB1: ("KP000", "KP000"),

    0xB2: ("THOUSANDS_SEPARATOR", "THOUSANDS_SEPARATOR"),
    0xB3: ("DECIMAL_SEPARATOR", "DECIMAL_SEPARATOR"),
    0xB4: ("CURRENCY_UNIT", "CURRENCY_UNIT"),
    0xB5: ("CURRENCY_SUBUNIT", "CURRENCY_SUBUNIT"),

    0xB6: ("KP_LEFT_PAREN", "KP_LEFT_PAREN"),
    0xB7: ("KP_RIGHT_PAREN", "KP_RIGHT_PAREN"),

    0xB8: ("KP_LEFT_BRACE", "KP_LEFT_BRACE"),
    0xB9: ("KP_RIGHT_BRACE", "KP_RIGHT_BRACE"),

    0xBA: ("KP_TAB", "KP_TAB"),
    0xBB: ("KP_BACKSPACE", "KP_BACKSPACE"),

    0xBC: ("KP_A", "KP_A"),
    0xBD: ("KP_B", "KP_B"),
    0xBE: ("KP_C", "KP_C"),
    0xBF: ("KP_D", "KP_D"),
    0xC0: ("KP_E", "KP_E"),
    0xC1: ("KP_F", "KP_F"),

    0xC2: ("KP_XOR", "KP_XOR"),
    0xC3: ("KP_POWER", "KP_POWER"),
    0xC4: ("KP_PERCENT", "KP_PERCENT"),

    0xC5: ("KP_LESS_THAN", "KP_LESS_THAN"),
    0xC6: ("KP_GREATER_THAN", "KP_GREATER_THAN"),
    0xC7: ("KP_AMPERSAND", "KP_AMPERSAND"),
    0xC8: ("KP_DOUBLE_AMPERSAND", "KP_DOUBLE_AMPERSAND"),

    0xC9: ("KP_VERTICAL_BAR", "KP_VERTICAL_BAR"),
    0xCA: ("KP_DOUBLE_VERTICAL_BAR", "KP_DOUBLE_VERTICAL_BAR"),

    0xCB: ("KP_COLON", "KP_COLON"),
    0xCC: ("KP_HASH", "KP_HASH"),
    0xCD: ("KP_SPACE", "KP_SPACE"),
    0xCE: ("KP_AT", "KP_AT"),
    0xCF: ("KP_EXCLAMATION", "KP_EXCLAMATION"),

    0xD0: ("KP_MEMORY_STORE", "KP_MEMORY_STORE"),
    0xD1: ("KP_MEMORY_RECALL", "KP_MEMORY_RECALL"),
    0xD2: ("KP_MEMORY_CLEAR", "KP_MEMORY_CLEAR"),
    0xD3: ("KP_MEMORY_ADD", "KP_MEMORY_ADD"),
    0xD4: ("KP_MEMORY_SUBTRACT", "KP_MEMORY_SUBTRACT"),

    0xD5: ("KP_MEMORY_MULTIPLY", "KP_MEMORY_MULTIPLY"),
    0xD6: ("KP_MEMORY_DIVIDE", "KP_MEMORY_DIVIDE"),

    0xD7: ("KP_PLUS_MINUS", "KP_PLUS_MINUS"),
    0xD8: ("KP_CLEAR", "KP_CLEAR"),
    0xD9: ("KP_CLEAR_ENTRY", "KP_CLEAR_ENTRY"),
    0xDA: ("KP_BINARY", "KP_BINARY"),
    0xDB: ("KP_OCTAL", "KP_OCTAL"),
    0xDC: ("KP_DECIMAL", "KP_DECIMAL"),
    0xDD: ("KP_HEXADECIMAL", "KP_HEXADECIMAL"),
}

# ==========================================================
# Consumer Page (0x0C)
# ==========================================================

_HID_CONSUMER_MAP = {

    # ------------------------------------------------------
    # Consumer Control
    # ------------------------------------------------------

    0x0001: "CONSUMER_CONTROL",

    # ------------------------------------------------------
    # Numeric keypad / selection
    # ------------------------------------------------------

    0x0030: "10",
    0x0031: "100",
    0x0032: "AM_PM",

    # ------------------------------------------------------
    # Generic device controls
    # ------------------------------------------------------

    0x0040: "POWER",
    0x0041: "RESET",
    0x0042: "SLEEP",

    0x0043: "SLEEP_AFTER",
    0x0044: "SLEEP_MODE",
    0x0045: "ILLUMINATION",
    0x0046: "FUNCTION_BUTTONS",

    # ------------------------------------------------------
    # Menu controls
    # ------------------------------------------------------

    0x0048: "MENU",
    0x0083: "MENU_PICK",
    0x0084: "MENU_UP",
    0x0085: "MENU_DOWN",
    0x0086: "MENU_LEFT",
    0x0087: "MENU_RIGHT",
    0x0088: "MENU_ESCAPE",
    0x0089: "MENU_VALUE_INCREASE",
    0x008A: "MENU_VALUE_DECREASE",

    # ------------------------------------------------------
    # Transport controls
    # ------------------------------------------------------

    0x00B0: "PLAY",
    0x00B1: "PAUSE",
    0x00B2: "RECORD",
    0x00B3: "FAST_FORWARD",
    0x00B4: "REWIND",
    0x00B5: "SCAN_NEXT_TRACK",
    0x00B6: "SCAN_PREVIOUS_TRACK",
    0x00B7: "STOP",
    0x00B8: "EJECT",
    0x00B9: "RANDOM_PLAY",
    0x00BA: "SELECT_DISC",
    0x00BB: "ENTER_DISC",
    0x00BC: "REPEAT",
    0x00BD: "TRACKING",
    0x00BE: "TRACK_NORMAL",
    0x00BF: "SLOW_TRACKING",

    0x00C0: "FRAME_FORWARD",
    0x00C1: "FRAME_BACK",
    0x00C2: "MARK",
    0x00C3: "CLEAR_MARK",
    0x00C4: "REPEAT_FROM_MARK",
    0x00C5: "RETURN_TO_MARK",
    0x00C6: "SEARCH_MARK_FORWARD",
    0x00C7: "SEARCH_MARK_BACKWARD",
    0x00C8: "COUNTER_RESET",

    # ------------------------------------------------------
    # Audio controls
    # ------------------------------------------------------

    0x00E0: "VOLUME",
    0x00E1: "BALANCE",
    0x00E2: "MUTE",
    0x00E3: "BASS",
    0x00E4: "TREBLE",
    0x00E5: "BASS_BOOST",
    0x00E6: "SURROUND_MODE",
    0x00E7: "LOUDNESS",
    0x00E8: "MPX",
    0x00E9: "VOLUME_INCREMENT",
    0x00EA: "VOLUME_DECREMENT",

    # ------------------------------------------------------
    # Playback selection
    # ------------------------------------------------------

    0x0180: "AL_CONSUMER_CONTROL_CONFIGURATION",
    0x0181: "AL_EMAIL_READER",
    0x0182: "AL_CALCULATOR",
    0x0183: "AL_LOCAL_BROWSER",
    0x0184: "AL_NETWORK_BROWSER",
    0x0185: "AL_NETWORK_BROWSER",
    0x0186: "AL_CONTACTS",
    0x0187: "AL_CALENDAR",
    0x0188: "AL_TASK_MANAGER",
    0x0189: "AL_CHECKBOOK",
    0x018A: "AL_EMAIL",
    0x018B: "AL_CALCULATOR",
    0x018C: "AL_MEDIA_PLAYER",
    0x018D: "AL_LOCAL_MACHINE_BROWSER",
    0x018E: "AL_NETWORK_CONNECTION",
    0x018F: "AL_WWW_BROWSER",
    0x0190: "AL_NETWORK_CHAT",
    0x0191: "AL_NETWORK_NEWS",
    0x0192: "AL_NETWORK_VOICEMAIL",
    0x0193: "AL_NETWORK_ADDRESS_BOOK",
    0x0194: "AL_NETWORK_CENTRAL",
    0x0195: "AL_NETWORK_CALENDAR",
    0x0196: "AL_TASK_MANAGER",
    0x0197: "AL_LOG_PROGRAM",
    0x0198: "AL_LOG_JOURNAL",
    0x0199: "AL_LOG_CALCULATOR",
    0x019A: "AL_LOG_CLOCK",
    0x019B: "AL_CONTROL_PANEL",
    0x019C: "AL_COMMAND_LINE",
    0x019D: "AL_PROCESS_BROWSER",
    0x019E: "AL_LOCK",

    # ------------------------------------------------------
    # Browser controls
    # ------------------------------------------------------

    0x0221: "AC_SEARCH",
    0x0222: "AC_HOME",
    0x0223: "AC_BACK",
    0x0224: "AC_FORWARD",
    0x0225: "AC_STOP",
    0x0226: "AC_REFRESH",
    0x0227: "AC_BOOKMARKS",

    # ------------------------------------------------------
    # Application controls
    # ------------------------------------------------------

    0x0200: "AC_NEW",
    0x0201: "AC_OPEN",
    0x0202: "AC_CLOSE",
    0x0203: "AC_EXIT",
    0x0204: "AC_MAXIMIZE",
    0x0205: "AC_MINIMIZE",
    0x0206: "AC_SAVE",
    0x0207: "AC_PRINT",
    0x0208: "AC_PROPERTIES",

    0x0210: "AC_UNDO",
    0x0211: "AC_COPY",
    0x0212: "AC_CUT",
    0x0213: "AC_PASTE",
    0x0214: "AC_SELECT_ALL",
    0x0215: "AC_FIND",
    0x0216: "AC_FIND_AND_REPLACE",
    0x0217: "AC_SEARCH",
}

# ==========================================================
# Generic Desktop Page (0x01)
# ==========================================================

_HID_GENERIC_DESKTOP_MAP = {

    # ------------------------------------------------------
    # Pointer / Mouse
    # ------------------------------------------------------

    0x01: "POINTER",
    0x02: "MOUSE",

    # ------------------------------------------------------
    # Joystick / Game devices
    # ------------------------------------------------------

    0x04: "JOYSTICK",
    0x05: "GAMEPAD",
    0x06: "KEYBOARD",
    0x07: "KEYPAD",
    0x08: "MULTI_AXIS_CONTROLLER",

    # ------------------------------------------------------
    # Controllers
    # ------------------------------------------------------

    0x09: "TABLET_PC_SYSTEM_CONTROLS",

    0x30: "X",
    0x31: "Y",
    0x32: "Z",

    0x33: "RX",
    0x34: "RY",
    0x35: "RZ",

    0x36: "SLIDER",
    0x37: "DIAL",
    0x38: "WHEEL",

    0x39: "HAT_SWITCH",

    0x3A: "COUNTED_BUFFER",
    0x3B: "BYTE_COUNT",
    0x3C: "MOTION_WAKEUP",
    0x3D: "START",
    0x3E: "SELECT",

    0x3F: "VX",
    0x40: "VY",
    0x41: "VZ",

    0x42: "VBRX",
    0x43: "VBRY",
    0x44: "VBRZ",

    0x45: "VNO",

    0x46: "FEATURE_NOTIFICATION",

    0x47: "RESOLUTION_MULTIPLIER",

    # ------------------------------------------------------
    # System Controls
    # ------------------------------------------------------

    0x80: "SYSTEM_CONTROL",

    0x81: "SYSTEM_POWER_DOWN",
    0x82: "SYSTEM_SLEEP",
    0x83: "SYSTEM_WAKE_UP",

    0x84: "SYSTEM_CONTEXT_MENU",
    0x85: "SYSTEM_MAIN_MENU",
    0x86: "SYSTEM_APP_MENU",
    0x87: "SYSTEM_MENU_HELP",
    0x88: "SYSTEM_MENU_EXIT",
    0x89: "SYSTEM_MENU_SELECT",
    0x8A: "SYSTEM_MENU_RIGHT",
    0x8B: "SYSTEM_MENU_LEFT",
    0x8C: "SYSTEM_MENU_UP",
    0x8D: "SYSTEM_MENU_DOWN",

    0x8E: "SYSTEM_COLD_RESTART",
    0x8F: "SYSTEM_WARM_RESTART",

    # ------------------------------------------------------
    # D-pad / Game controls
    # ------------------------------------------------------

    0x90: "D_PAD_UP",
    0x91: "D_PAD_DOWN",
    0x92: "D_PAD_RIGHT",
    0x93: "D_PAD_LEFT",

    # ------------------------------------------------------
    # Dock / Laptop controls
    # ------------------------------------------------------

    0xA0: "SYSTEM_DOCK",
    0xA1: "SYSTEM_UNDOCK",
    0xA2: "SYSTEM_SETUP",
    0xA3: "SYSTEM_BREAK",
    0xA4: "SYSTEM_DEBUGGER_BREAK",
    0xA5: "APPLICATION_BREAK",
    0xA6: "APPLICATION_DEBUGGER_BREAK",
    0xA7: "SYSTEM_SPEAKER_MUTE",
    0xA8: "SYSTEM_HIBERNATE",

    # ------------------------------------------------------
    # Display controls
    # ------------------------------------------------------

    0xB0: "SYSTEM_DISPLAY_INVERT",
    0xB1: "SYSTEM_DISPLAY_INTERNAL",
    0xB2: "SYSTEM_DISPLAY_EXTERNAL",
    0xB3: "SYSTEM_DISPLAY_BOTH",
    0xB4: "SYSTEM_DISPLAY_DUAL",
    0xB5: "SYSTEM_DISPLAY_TOGGLE",
    0xB6: "SYSTEM_DISPLAY_SWAP",

    # ------------------------------------------------------
    # Keyboard / Button helpers
    # ------------------------------------------------------

    0xC0: "SYSTEM_BUTTON_CONFIG",
    0xC1: "SYSTEM_BUTTON_HELP",
    0xC2: "SYSTEM_BUTTON_DOCUMENTS",
    0xC3: "SYSTEM_BUTTON_POWER",
    0xC4: "SYSTEM_BUTTON_SLEEP",
    0xC5: "SYSTEM_BUTTON_WAKE",

    # ------------------------------------------------------
    # Consumer application launch
    # ------------------------------------------------------

    0xC6: "SYSTEM_BUTTON_MEDIA_SELECT",
    0xC7: "SYSTEM_BUTTON_MAIL",
    0xC8: "SYSTEM_BUTTON_CALCULATOR",
    0xC9: "SYSTEM_BUTTON_MY_COMPUTER",

    0xCA: "SYSTEM_BUTTON_BROWSER_SEARCH",
    0xCB: "SYSTEM_BUTTON_BROWSER_HOME",
    0xCC: "SYSTEM_BUTTON_BROWSER_BACK",
    0xCD: "SYSTEM_BUTTON_BROWSER_FORWARD",
    0xCE: "SYSTEM_BUTTON_BROWSER_STOP",
    0xCF: "SYSTEM_BUTTON_BROWSER_REFRESH",
    0xD0: "SYSTEM_BUTTON_BROWSER_BOOKMARKS",
}

