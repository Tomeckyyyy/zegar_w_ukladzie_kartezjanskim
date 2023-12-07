import math
import matplotlib.pyplot as plt
import numpy as np
import time

print(time.localtime(time.time())[3])
print(time.localtime(time.time())[4])
print(time.localtime(time.time())[5])

hours = ((2*math.pi)/12)*time.localtime(time.time())[3]
# do testów
# hours = ((2*math.pi)/12)*5
sin_hours = math.sin((math.pi/2)+hours)
cos_hours = math.cos((math.pi/2)-hours)

minutes = ((2*math.pi)/60)*time.localtime(time.time())[4]
sin_minutes = math.sin((math.pi/2)+minutes)
cos_minutes = math.cos((math.pi/2)-minutes)

seconds = ((2*math.pi)/60)*time.localtime(time.time())[5]
sin_seconds = math.sin((math.pi/2)+seconds)
cos_seconds = math.cos((math.pi/2)-seconds)

t = np.linspace(-1, 1, 1)
plt.axhline(color="gray",linestyle=':')
plt.axvline(color="gray", linestyle=':')
# godzina
plt.axhline(y=sin_hours, color="black")
plt.axvline(x=cos_hours, color="black")
# minuty
plt.axhline(y=sin_minutes, color="red")
plt.axvline(x=cos_minutes, color="red")
# sekundy
plt.axhline(y=sin_seconds, color="green")
plt.axvline(x=cos_seconds, color="green")
plt.xlim(-1, 1)
plt.ylim(-1,1)
plt.show()
