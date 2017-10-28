from openvpn_status import parse_status

with open('/etc/openvpn/openvpn-status.log') as logfile:
    status = parse_status(logfile.read())

print(status.updated_at)  # datetime.datetime(2015, 6, 18, 8, 12, 15)

def printDetails(ipaddr, client):
    print "------"
    print "Client IP: {:>21} " . format(ip)
    print "Cert Name: {:>10}" .format(client.common_name)
    print "Client Rcv Bytes: {}" .format(client.bytes_received)
    print "Client Snd Bytes: {}" .format(client.bytes_sent)
    print "Client Connected: {}" .format(client.connected_since)
    print "------"



for ip, client in status.client_list.iteritems():
    printDetails(ip, client)
