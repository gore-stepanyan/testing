import pyshark
from packet_handler import PacketHandler

capture = pyshark.LiveCapture(interface="any", display_filter="rtcp.pt==200 || sip || rtp")
#capture.sniff(packet_count=1)
packet_handler = PacketHandler()
 
def on_packet_arrive(packet):
    packet_handler.on_packet_arrive(packet)

for packet in capture.sniff_continuously():
    if hasattr(packet, 'rtcp'):
        on_packet_arrive(packet)

#capture.apply_on_packets(on_packet_arrive)