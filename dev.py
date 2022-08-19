import time
import pyshark
from packet_handler import PacketHandler

capture = pyshark.FileCapture('session_from_ecss_linphone.pcap', display_filter='sdp')

def unpack(packet):
    field_names = packet.sip._all_fields
    field_values = packet.sip._all_fields.values()
    return dict(zip(field_names, field_values))

count = 10

for packet in capture:
    print(count)
    sip = unpack(packet)
    if "sip.Method" in sip:
        if sip["sip.Method"] == "INVITE":
            print('method ', sip["sip.Method"], ' catched')

    count += 1
