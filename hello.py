"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask
import os


from flask import request
import multiprocessing
import threading
import time
import subprocess





app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    
  from coincurve import PublicKey
  from sha3 import keccak_256
  import os
  import time
  import etherscan
  import time
  start_time = time.time()
  es = etherscan.Client(api_key='HB88FQKBAIKSSVX1BQWDP1KJ9BKTUSJVT2',)
  addrss=[]
  pvkeys=[]
  bolfnd=0
  x=0
  y=0
  while y<50:
   y=y+1
   x=0
   while x<20:
    x=x+1
    private_key = keccak_256(os.urandom(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    addr=addr.hex()
    private_key=private_key.hex()
    addrss.append("0x"+str(addr))
    pvkeys.append(str(private_key))
   eth_balance = es.get_eth_balances(addrss)
   aa=list (eth_balance.values())  
   for bl in aa:
    if bl!=0:
     bolfnd=1
   if bolfnd!=0 :
    break
   time.sleep(500/1000) 
   addrss=[]
   pvkeys=[]
    
  return "<xmp>" +  "bl:"+str(bolfnd)+"\n" +str(addrss)+ "\n"+str(pvkeys)+"</xmp>"

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
