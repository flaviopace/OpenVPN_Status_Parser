from openvpn_status import parse_status

with open('/etc/openvpn/openvpn-status.log') as logfile:
    status = parse_status(logfile.read())

table  = ("<html><table border='1'<tr> <th>IP</th> <th>Cert Name</th> <th>Rcv Bytes</th> \
<th>Sent Bytes</th> <th>Connected Sinze</th> </tr>")

print(" - Date {}".format(status.updated_at))  # datetime.datetime(2015, 6, 18, 8, 12, 15)

def printDetails(ipaddr, client):
    print "------"
    print "Client IP: {:>21} " . format(ip)
    print "Cert Name: {:>10}" .format(client.common_name)
    print "Client Rcv Bytes: {}" .format(client.bytes_received)
    print "Client Snd Bytes: {}" .format(client.bytes_sent)
    print "Client Connected: {}" .format(client.connected_since)
    print "------"


def addHTMLRowTable(ipaddr, client):
    table = "<tr>"
    table += "<th>{}</th>". format(ip)
    table += "<th>{}</th>". format(client.common_name)
    table += "<th>{}</th>". format(client.bytes_received)
    table += "<th>{}</th>". format(client.bytes_sent)
    table += "<th>{}</th>". format(client.connected_since)
    table += "</tr>"
    return table

for ip, client in status.client_list.iteritems():
    #printDetails(ip, client)
    table += addHTMLRowTable(ip, client)

table += ("</table></html>")

print table
