import time
import pyshark
from packet_handler import PacketHandler

capture = pyshark.FileCapture('session_from_ecss_linphone.pcap', display_filter='sdp')

def get_rtcp(packet):
    field_names = packet.sip._all_fields
    field_values = packet.sip._all_fields.values()
    return dict(zip(field_names, field_values))

for packet in capture:
    #time.sleep(1)
    print('\n', get_rtcp(packet), '\n')
