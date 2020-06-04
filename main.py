from scapy.all import *
import pickle

def http_header(packet):
    # incomming https://stackoverflow.com/questions/24664893/python-scapy-sniff-only-incoming-packets
    if packet[Ether].src != Ether().src:
        # print("nope")
        return
    try:
        handle = open('data.pickle', 'rb')
        data = pickle.load(handle)
        handle.close()
    except:
        print("file not found")
        data = {}
    if DNS in packet:
        print(packet[DNS].qd.qname)
        dns = packet[DNS].qd.qname.decode()
        if dns in data:
            data[dns] +=1
        else:
            data[dns] = 1
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    elif IP in packet:
        pass
        # print(packet.getlayer(IP).src)
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    # http_packet=str(packet)
    # if http_packet.find('GET'):
    #         return GET_print(packet)

def GET_print(packet1):
    ret = "***************************************GET PACKET****************************************************\n"
    ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    ret += "*****************************************************************************************************\n"
    return ret

# sniff(iface='enp3s0', prn=http_header, filter="tcp or ip host 8.8.8.8",lfilter=lambda pkt: pkt[Ether].src != Ether().src)
sniff(iface='enp3s0', prn=http_header, filter="tcp or ip host 8.8.8.8")


# import matplotlib.pyplot as plt 
# labels = [k for k,v in data.items()]
# ax1.pie([v for k,v in data.items()],labels=labels)
# plt.show()