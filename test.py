from struct import pack
import pyshark
from main import listen
from packet_handler import PacketHandler
import datetime
import time
 
capture = pyshark.LiveCapture(interface="enp5s0", display_filter='udp', decode_as={'udp.port==8000':'rtp'})

def get_data(packet):
    try:
        field_names = packet.rtp._all_fields
        field_values = packet.rtp._all_fields.values()
        return dict(zip(field_names, field_values))
    except:
        pass

while True:
    time.sleep(1)
    capture.sniff(packet_count=5)
    for packet in capture:
        print('sniffed', packet.highest_layer)
    print(capture)
    capture.clear()