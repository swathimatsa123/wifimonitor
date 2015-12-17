import Device
from scapy.all import *
import threading
from pylab import *
import matplotlib.pyplot as plt
import time
import os

class Network:
    num_devices = 0
    device_list = {}
    bwUsageHistory = {}

    def Join_device(self, mac_addr, ip_addr=None):
        dev = Device.device(mac_addr, ip_addr)
        self.device_list[mac_addr] = dev 
        print 'Join the device %s' %(mac_addr)

    def Does_Device_Exist (self, mac_addr) :
        if self.device_list.has_key(mac_addr):
            return True
        else:
            return False

    def Delete_device(self, mac_addr):
        del self.device_list[mac_addr]
        print 'Delete the device'

    def plotUSage (self, sleepCount ) :
        xdata = []
        ydata = []
        positions = []
        count = 0
        totalBandwidth = 0
        for mac, device in self.device_list.items():
            xdata.append(mac)
            deviceBandwidth = device.get_bandwidth()
            device.reset_bandwidth()
            totalBandwidth = totalBandwidth + deviceBandwidth
            ydata.append(deviceBandwidth)
            positions.append(count+0.5)
            count = count + 0.5

        bar(positions,ydata, align='center')
        xticks(positions, xdata)
        ylabel('Bandwidth')
        title('Total bandwidth usage in last 5 min')
        grid(True)
        savefig("usage5Min.png")
        plt.clf()
        print 'Plot image is ready. Name %s' %('usage5Min.png')
        if (sleepCount % 6 == 0): 
            print '## Printing total usage %s' %(totalBandwidth)
            self.bwUsageHistory[sleepCount/6] = totalBandwidth
            times = self.bwUsageHistory.keys()
            totals = self.bwUsageHistory.values()
            
            plt.plot(times, totals)
            grid(True)
            os.system('/bin/mv totalUsage.png totalUsageSofar.png')
            savefig("totalUsage.png")
            plt.clf()
        
        
    def Display_devices(self):
        pass

    def Process_packet(self, pkt = None):
        for key, value in pkt.items():
            self.device_list[key].consume_bandwidth(value)

def PktHeaderParser (pkt):
    if pkt.haslayer(Dot11):
        wrlsHdr = pkt[Dot11] 
        dst = wrlsHdr.fields['addr1']
        src = wrlsHdr.fields['addr2']
        addr3 = wrlsHdr.fields['addr3']
        if src != None:
            if not network.Does_Device_Exist (src):
                network.Join_device (src)
            network.Process_packet({ src: len(pkt)})
            
def startMonitor():
     sniff(iface="mon0", prn = PktHeaderParser)
    
global network
if __name__=="__main__":
    network = Network()
    t=  threading.Thread(target=startMonitor)
    t.start()
    sleepCount = 0
    while  True:
        time.sleep(3)
        sleepCount +=1
        network.plotUSage(sleepCount)
        

