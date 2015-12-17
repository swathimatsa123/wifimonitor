class device:
    def __init__(self, mac_addr, ip_addr=None):
        self.mac_address = mac_addr
        self.ip_address = ip_addr
        self.last_conn_time = 0
        self.total_packet_set = 0
        self.bandwidth = 0

    def __str__(self):
        return 'MAC address:%s BW sofar is %s' %(self.mac_address, self.bandwidth)
        
    def consume_bandwidth(self, byte_count):
        self.bandwidth += byte_count 

    def get_bandwidth(self):
        return self.bandwidth

    def reset_bandwidth(self):
        self.bandwidth = 0

    def show_bandwidth(self):
        pass
        #print 'I am in show bandwidth'

if __name__=="__main__":
    device = device(22,99)
    device.consume_bandwidth(1500)
    print device
    device.consume_bandwidth(2500)
    print device
    device.show_bandwidth()
