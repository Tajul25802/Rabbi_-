import requests
import os

RED = "\033[0;31m"
GREEN = "\033[0;32m"
END = "\033[0m"

os.system("clear")
print(GREEN,"_"*64)
print("")
print("""   .dMMMb  dMP dMP dMMMMb                                      
  dMP" VP dMP dMP dMP"dMP                                      
  VMMMb  dMP dMP dMMMMK"                                       
dP .dMP dMP.aMP dMP.aMF                                        
VMMMP"  VMMMP" dMMMMP"  """)                                                                                             
print(RED,"""
   dMMMMb  dMP .dMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMb 
   dMP VMP amr dMP" VP dMP"VMP dMP"dMP dMP dMP dMP     dMP.dMP 
  dMP dMP dMP  VMMMb  dMP     dMP dMP dMP dMP dMMMP   dMMMMK"  
 dMP.aMP dMP dP .dMP dMP.aMP dMP.aMP  YMvAP" dMP     dMP"AMF   
dMMMMP" dMP  VMMMP"  VMMMP"  VMMMP"    VP"  dMMMMMP dMP dMP    """)
print("")
print(GREEN,"created by team Anon404")
print(GREEN,"_"*64)
print(GREEN,"[+] Enter your terget")

domain = input("--> ")

#domain = domain.replace("https://","").replace("http://","").replace("www.","")

r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}")

print(r.text)
