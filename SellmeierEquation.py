import numpy as np
import matplotlib.pyplot as plt

def Sellmeier(wavelength, B, C):
    nsquared = 1
    for k in range(len(B)):
        quant = (B[k]*wavelength*wavelength)/(wavelength*wavelength - C[k])
        nsquared += quant

    n = np.sqrt(nsquared)
    return n


wavelengths = np.linspace(400e-9, 700e-9, 50)
B = np.array([0.6962, 0.40794, 0.89748])
C = np.array([4.679e-15, 1.3512e-14, 97.934e-12])
n = []

for i in range(len(wavelengths)):
    n.append(Sellmeier(wavelengths[i], B, C))

delta_n = n[49] - n[0]
print(delta_n)
print(len(n))

plt.figure()
plt.plot(wavelengths, n, '-b')
plt.xlabel('Wavelength')
plt.ylabel('Index of Refraction')
plt.title('Sellmeier Equation')
plt.grid()
plt.show()