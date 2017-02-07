import os
import shlex
from nmap import *
import subprocess

class FindPi:

  def __init__(self, ip):
    self.ip = ip

  def nmap_awk_results(self):
    results = []
    nm = nmap.PortScanner()
    nm.scan(self.ip, arguments= '-sP')
    for h in nm.all_hosts():
      if 'mac' in nm[h]['addresses']:
        for x in nm[h]['vendor'].keys():
          if x.startswith('B8:27:EB'):
            #print(nm[h]['vendor'])
            mac = (nm[h]['addresses']['mac'])
            ip = (nm[h]['addresses']['ipv4'])
            results.append([mac, ip])
    x = len(results)
    if x == 1: 
      print results[0]
    elif x == 2:
      print results[0], results[1]
    elif x == 3:
      print results[0], results[1], results[2]
    elif x == 4:
      print results[0], results[1], results[2], results[3]    
    elif x == 5:
      print results[0], results[1], results[2], results[3], results[4]
