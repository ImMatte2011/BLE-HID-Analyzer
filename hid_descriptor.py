"""
USB HID Report Descriptor parser.

Decodes HID short items:
- Main
- Global
- Local

Supports:
- Report ID
- Report size
- Report count
- Usage Page
- Usage
- Input / Output / Feature fields
"""


# ==========================================================
# HID Item Types
# ==========================================================

ITEM_MAIN = 0
ITEM_GLOBAL = 1
ITEM_LOCAL = 2


MAIN_INPUT = 8
MAIN_OUTPUT = 9
MAIN_COLLECTION = 10
MAIN_FEATURE = 11
MAIN_END_COLLECTION = 12


GLOBAL_USAGE_PAGE = 0
GLOBAL_LOGICAL_MIN = 1
GLOBAL_LOGICAL_MAX = 2
GLOBAL_PHYSICAL_MIN = 3
GLOBAL_PHYSICAL_MAX = 4
GLOBAL_UNIT_EXPONENT = 5
GLOBAL_UNIT = 6
GLOBAL_REPORT_SIZE = 7
GLOBAL_REPORT_ID = 8
GLOBAL_REPORT_COUNT = 9


LOCAL_USAGE = 0
LOCAL_USAGE_MIN = 1
LOCAL_USAGE_MAX = 2


# ==========================================================
# Helpers
# ==========================================================

def signed(value, bits):

    if value & (1 << (bits - 1)):
        return value - (1 << bits)

    return value


def item_value(data):

    value = 0

    for i, b in enumerate(data):
        value |= b << (8 * i)

    return value


# ==========================================================
# Parser
# ==========================================================


class HIDReportDescriptorParser:


    def __init__(self):

        self.reset()


    def reset(self):

        self.usage_page = None

        self.report_id = 0
        self.report_size = 0
        self.report_count = 0

        self.fields = []

        self.collections = []

        self.local_usage = []



    def parse(self, descriptor):

        self.reset()

        index = 0


        while index < len(descriptor):

            prefix = descriptor[index]
            index += 1


            # Long item

            if prefix == 0xFE:

                if index + 1 >= len(descriptor):
                    break

                size = descriptor[index]
                index += 2

                index += size

                continue


            size_code = prefix & 0x03
            item_type = (prefix >> 2) & 0x03
            tag = (prefix >> 4) & 0x0F


            if size_code == 0:
                size = 0
            elif size_code == 1:
                size = 1
            elif size_code == 2:
                size = 2
            else:
                size = 4


            data = descriptor[index:index+size]

            index += size


            value = item_value(data)


            self.process(
                item_type,
                tag,
                value,
                data
            )


        return self.fields



    def process(self, item_type, tag, value, raw):


        # -------------------------
        # GLOBAL
        # -------------------------

        if item_type == ITEM_GLOBAL:


            if tag == GLOBAL_USAGE_PAGE:

                self.usage_page = value


            elif tag == GLOBAL_REPORT_SIZE:

                self.report_size = value


            elif tag == GLOBAL_REPORT_COUNT:

                self.report_count = value


            elif tag == GLOBAL_REPORT_ID:

                self.report_id = value



        # -------------------------
        # LOCAL
        # -------------------------

        elif item_type == ITEM_LOCAL:


            if tag == LOCAL_USAGE:

                self.local_usage.append(value)



        # -------------------------
        # MAIN
        # -------------------------

        elif item_type == ITEM_MAIN:


            if tag == MAIN_COLLECTION:

                self.collections.append(
                    {
                        "type": value,
                        "usage_page": self.usage_page,
                        "usage": self.local_usage[:]
                    }
                )

                self.local_usage.clear()



            elif tag == MAIN_INPUT:

                self.add_field(
                    "INPUT",
                    value
                )


            elif tag == MAIN_OUTPUT:

                self.add_field(
                    "OUTPUT",
                    value
                )


            elif tag == MAIN_FEATURE:

                self.add_field(
                    "FEATURE",
                    value
                )


            elif tag == MAIN_END_COLLECTION:

                if self.collections:
                    self.collections.pop()



    def add_field(self, direction, flags):


        field = {

            "direction": direction,

            "report_id": self.report_id,

            "usage_page": self.usage_page,

            "usages": self.local_usage[:],

            "report_size": self.report_size,

            "report_count": self.report_count,

            "flags": flags,
        }


        self.fields.append(field)

        self.local_usage.clear()