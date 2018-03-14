#!/usr/bin python3

import pyVim
from pyVim import connect

my_cluster = connect.ConnectNoSSL("192.168.100.9", 443,"amckenzie", "Excellent123$")
searcher = my_cluster.content.searchIndex
vm = searcher.FindByIp(ip="192.168.100.141", vmSearch=True)
print (my_cluster.PortGroup)
connect.Disconnect(my_cluster)

exit(0)

