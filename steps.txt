# pneumatic_door_control
python program in pi zero to control pneumatic door, creating hotspot in pi zero in raspbian os and running the webserver to control the solenoids

# Reference to create hotspot in raspbian OS, below step work only for raspbian OS
https://www.raspberrypi.com/documentation/computers/configuration.html


1. sudo apt install hostapd
2. sudo systemctl unmask hostapd
3. sudo systemctl enable hostapd
4. sudo apt install dnsmasq
5. sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent
6. sudo nano /etc/dhcpcd.conf
#add in the end
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant

7. sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
8. sudo nano /etc/dnsmasq.conf

interface=wlan0 # Listening interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
                # Pool of IP addresses served via DHCP
domain=wlan     # Local wireless DNS domain
address=/gw.wlan/192.168.4.1
                # Alias for this router
           
9. sudo rfkill unblock wlan
10. sudo nano /etc/hostapd/hostapd.conf

country_code=IN
interface=wlan0
ssid=NameOfNetwork
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=AardvarkBadgerHedgehog
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP

11. sudo systemctl reboot

# once rebooted connect to the created wifi and  ssh pi@192.168.4.1 and give the password
