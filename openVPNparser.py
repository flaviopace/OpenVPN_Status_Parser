from openvpn_status import parse_status

with open('/etc/openvpn/openvpn-status.log') as logfile:
    status = parse_status(logfile.read())

indexArr = 0
arraycolor = ['0xeeeeee','0xdddddd']

table  = ("<html><table style='font-weight: bold' bgcolor='B0DC7A' border='1'> <tr> <th>Cert Name</th> <th>Real IP</th> <th>VPN IP</th> <th>Rcv Bytes</th> \
<th>Sent Bytes</th> <th>Connected Since</th> </tr>")

print(" - Date {}".format(status.updated_at))  # datetime.datetime(2015, 6, 18, 8, 12, 15)

def printDetails(ipaddr, client):
    print "------"
    print "Client IP: {:>21} " . format(ip)
    print "Cert Name: {:>10}" .format(client.common_name)
    print "Client Rcv Bytes: {}" .format(client.bytes_received)
    print "Client Snd Bytes: {}" .format(client.bytes_sent)
    print "Client Connected: {}" .format(client.connected_since)
    print "------"


def addHTMLRowTable(ipaddr, client, inc):
    table = "<tr bgcolor='{}'>". format(arraycolor[inc])
    table += "<th>{}</th>". format(client.common_name)
    table += "<th>{}</th>". format(ip)
    virtul_ip = ''
    for  vclient, routing in status.routing_table.iteritems():
        if( routing.common_name == client.common_name):
            virtul_ip += str(routing.virtual_address)

    table += "<th>{}</th>". format(virtul_ip)
    table += "<th>{}</th>". format(client.bytes_received)
    table += "<th>{}</th>". format(client.bytes_sent)
    table += "<th>{}</th>". format(client.connected_since)
    table += "</tr>"
    return table

for ip, client in status.client_list.iteritems():
    #printDetails(ip, client)
    if (indexArr == 2):
        indexArr = 0
    table += addHTMLRowTable(ip, client, indexArr)
    indexArr += 1

table += ("</table></html>")

print table
