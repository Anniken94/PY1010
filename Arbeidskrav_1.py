# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:04:22 2024

@author: Anniken
"""

km = 25000              #Årlig kjørelengde
F_el = 5000             #Forsikring per år elbil
F_bensin = 7500         #Forsikring per år bensinbil
TA = 8.38               #Trafikkforsikringsavgift per dag
D_el = 0.2              #Drivstoff elbil kWh/km
Lading = 2              #Lading i kr/kWh
D_bensin = 1            #Drivdroff bensinbili kr/km
B_el = 0.1              #Bomavgift i kr/km
B_bensin = 0.3          #Bomavgift i kr/km

Elbil = F_el + (TA*365) + (D_el*km)*Lading + (B_el*km)
Bensin = F_bensin + (TA*365) + (D_bensin*km) + (B_bensin*km)

Diff = Bensin - Elbil

print("Årlige kostnader for elbil er", Elbil, "kr")
print("Årlige kostnader for bensinbil er", Bensin, "kr")
print(f"Det er {Diff:.2f} kr dyrere å kjøre bensinbil")