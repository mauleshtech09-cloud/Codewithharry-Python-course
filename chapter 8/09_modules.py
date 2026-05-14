# Two types of modules in python :
#     - built in module 
#     - external module

import math
import myModule
import requests

myModule.greet()

print(math.sqrt(200))

r=requests.get("https://www.google.com")

print(r.text)