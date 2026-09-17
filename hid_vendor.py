"""
Vendor Defined HID Usage decoder.

Handles:
- HID Usage Pages 0xFF00 - 0xFFFF
- Known vendor mappings
- Generic RAW fallback
"""


# ==========================================================
# Known Vendor Pages
# ==========================================================


VENDOR_PAGES = {


    # Logitech
    0xFF00: {
        "name": "Logitech",
        "decoder": "logitech",
    },


    # Logitech Wireless Device
    0xFF43: {
        "name": "Logitech HID++",
        "decoder": "logitech_hidpp",
    },


    # Microsoft
    0xFF01: {
        "name": "Microsoft",
        "decoder": "microsoft",
    },


    # Razer
    0xFF00: {
        "name": "Razer",
        "decoder": "generic",
    },


    # Corsair
    0xFF02: {
        "name": "Corsair",
        "decoder": "generic",
    },

}


# ==========================================================
# Generic vendor decoder
# ==========================================================


class VendorDecoder:


    def decode(self, usage_page, data, report_id=None):


        vendor = VENDOR_PAGES.get(
            usage_page,
            {
                "name": "Unknown Vendor",
                "decoder": "generic"
            }
        )


        result = {

            "vendor": vendor["name"],

            "usage_page":
                "0x%04X" % usage_page,

            "report_id": report_id,

            "raw_hex":
                " ".join("%02X" % x for x in data),

            "decoded": {}

        }


        decoder = getattr(
            self,
            "_decode_" + vendor["decoder"],
            self._decode_generic
        )


        result["decoded"] = decoder(data)


        return result



    # ------------------------------------------------------
    # Generic fallback
    # ------------------------------------------------------

    def _decode_generic(self, data):

        return {

            "type": "RAW",

            "length": len(data),

            "bytes": [
                x for x in data
            ]

        }



    # ------------------------------------------------------
    # Logitech HID++
    # ------------------------------------------------------

    def _decode_logitech_hidpp(self, data):


        if len(data) < 4:

            return {
                "type": "short_packet"
            }


        return {

            "type": "HID++",

            "device_id":
                data[0],

            "feature":
                data[1],

            "function":
                data[2],

            "params":
                data[3:]

        }



    # ------------------------------------------------------
    # Logitech legacy
    # ------------------------------------------------------

    def _decode_logitech(self, data):


        return {

            "type":
                "Logitech",

            "sub_id":
                data[0] if data else None,

            "payload":
                data[1:]

        }



    # ------------------------------------------------------
    # Microsoft
    # ------------------------------------------------------

    def _decode_microsoft(self, data):


        return {

            "type":
                "Microsoft",

            "payload":
                data

        }