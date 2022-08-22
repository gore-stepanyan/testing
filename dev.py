import time
import pyshark
from packet_handler import PacketHandler
import socket

capture = pyshark.FileCapture('session_from_ecss_linphone.pcap', display_filter='sdp')

def unpack(packet):
    field_names = packet.sip._all_fields
    field_values = packet.sip._all_fields.values()
    return dict(zip(field_names, field_values))

count = 0

def get_self_ip():
    host_name = socket.gethostname()
    IP_addres = socket.gethostbyname(host_name)
    print("Computer IP Address is:" + IP_addres)

get_self_ip()

for packet in capture:
    print(count)
    sip = unpack(packet)
    if "sip.Method" in sip:
        if (sip["sip.Method"] == "INVITE" or sip["sip.Method"] == "ACK") and sip['sdp.session_name'] != 'ECSS-10':
            print('method', sip["sip.Method"], 'catched')
            print('from', sip['sdp.owner.address'])
            print('session mame', sip['sdp.session_name'])

    count += 1
