import Subnet_Calculator
import sys

class validate_ip():
    def __init__(self,arg):
      self.IP_Address = arg
      print(f"This is great this is what i was trying to do,{ self.IP_Address}")
      
    def det_class(self,IP_L):
      if len(IP_L) < 4:
        print(f"Enter Valid IP address")
        exit()
      elif int(IP_L[0]) <= 127 and int(IP_L[0]) >= 1:
        print(f"Class A: IP address,Default Subnet Mask: 255.0.0.0")
        return ['A','255.0.0.0']
      elif int(IP_L[0]) <= 191 and int(IP_L[0]) >= 128:
        print(f"Class B IP address Default Subnet Mask: 255.255.0.0")
        return ['B','255.255.0.0']
      elif int(IP_L[0]) <= 223 and int(IP_L[0]) >= 192:
        print(f"Class C IP address Default Subnet Mask: 255.255.255.0")
        return ['C','255.255.255.0']
      elif int(IP_L[0]) <= 239 and int(IP_L[0]) >= 224:
        print(f"Class D IP address, for multi-cast")
        return ['D','255.255.255.0']
      elif int(IP_L[0]) <= 255 and int(IP_L[0]) >= 240:
        print(f"Class E IP address, for Experimental Purpose")
        return ['E','255.255.255.0']
      else:
        print("This is not valid IP address")
        exit()

    def int_to_bin(self,IP_L):
      for bin_IP in IP_L:
        while len(bin_IP) < 8:
          bin_IP = '0' + bin_IP
        print(bin_IP)
        IP_L.append(bin_IP)
      return IP_L
"""
def main():
  print(f"{vars()}")
  print(f"{__name__} {sys.argv[1]}")
  print(f"{vars()}")
#validate_ip(sys.argv[1])
"""
if __name__ == '__main__':# __name__ is the variable whos name is set to main before python starts executing source code
  print({sys.argv[0]})
  print(f"python {vars()} {__name__}")
  vip = validate_ip(sys.argv[1])
  print("")
  #r = 'N'
  IP_Address = sys.argv[1]
  IP_L = IP_Address.split('.')
  IP_L = [int(x) for x in IP_L]
  print(IP_L)
  ch = vip.det_class(IP_L)
  print(f"{ch}")
  #if ch == 'A'
  no_hosts = input(f"Enter the number of hosts")
  no_host_bits = len(str(bin(int(no_hosts))[2:]))
  mask = 32 - no_host_bits
  no_network = pow(2,(32 - no_host_bits))
  print(f"{IP_Address}/{mask} Class {ch} default: {no_network} possible Networks, {pow(2,no_host_bits)} possible hosts/network Total Hosts: {no_hosts}")
  bin_IP_address = [bin(en)[2:] for en in IP_L if True]
  print(f"{bin_IP_address}")
  bin_L = vip.int_to_bin(bin_IP_address)
  print(bin_L)
"""
  for e in bin_IP_address:
    while len(e) < 8:
      e ='0' + e
    print(e)
  exit()
"""
""" 
  while len(each) < 8:
    each = '0' + each
    if len(each) == 8:
      break
    bin_IP_address.append(each)
  print(f"{bin_IP_address}")

  while r == 'Y':
    opt = input("Select Option:1.Find The Subnet Mask.\n 2.")
    if opt == 1:
      det_class(IP_L)
    r = input("Continue Y/N?")
    if r == 'N':
      break
    else:
      continue
"""