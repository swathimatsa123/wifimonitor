import Device
class Network:
    num_devices = 0
    device_list = {}

    def Join_device(self, mac_addr, ip_addr):
        dev = Device.device(mac_addr, ip_addr)
        self.device_list[mac_addr] = dev 
        print 'Join the device'

    def Delete_device(self, mac_addr):
        del self.device_list[mac_addr]
        print 'Delete the device'

    def Display_devices(self):
        print self.device_list
        print 'Print all the devices in the network'

    def Process_packet(self, pkt = None):
        for key, value in pkt.items():
            print "Looking for device : %s" %key
            print 'given bandwidth: %s' %value
            self.device_list[key].consume_bandwidth(value)
            print self.device_list[key]
        print 'Number of packets in the network'

    def Print_bandwidth_statistics(self):
        total_bandwidth = 0
        for key, value in self.device_list.items():
            total_bandwidth += value.get_bandwidth()
            print 'Per device Bandwidth So far for %s is %s' %(key, value.get_bandwidth())
        print 'Total Bandwidth So far : %s' %total_bandwidth  
        

if __name__=="__main__":
    network = Network()
    network.Join_device("11:22:33:44:55:66", "192.168.42.1")
    network.Join_device("aa:bb:33:44:55:66", "192.168.42.10")
    network.Display_devices()
    #
    #  11:22:33:44:55:66 .,,,,
    #  aa:bb: ...
    #  
    # network.Delete_device("11:22:33:44:55:66")
    network.Display_devices()
    #  aa:bb: ...

    network.Process_packet({"11:22:33:44:55:66" : 1500})
    network.Process_packet({"11:22:33:44:55:66" : 2500})
    network.Process_packet({"aa:bb:33:44:55:66" : 3200})
    network.Print_bandwidth_statistics()
