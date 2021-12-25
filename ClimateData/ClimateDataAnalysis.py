%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Loading in data

GLB_time,GLB_temp=np.loadtxt('GLB.Ts.csv',skiprows=1,delimiter=',',usecols=(0,13),unpack=True)
GLB_temp=GLB_temp/100


bitanja=np.loadtxt("bintanja2008.txt",skiprows=109,unpack=True)
time_bitanja=((bitanja[0]*-100)+2018)

co2_mm_mlo=np.loadtxt("co2_mm_mlo.txt",skiprows=72,unpack=True)
co2_mm_mlo_time=co2_mm_mlo[2]
co2_mm_mlo_ppm_con=co2_mm_mlo[4] 


ch4_annmean_gl=np.loadtxt("ch4_annmean_gl.txt",skiprows=55,unpack=True)
ch4_annmean_gl_YEAR=ch4_annmean_gl[0] 
ch4_annmean_gl_CH4=ch4_annmean_gl[1]

vostok_deutnat=np.loadtxt("vostok-deutnat.txt",skiprows=111,unpack=True)
vostok_deutnat_time=((vostok_deutnat[1]*-1)+2018)
vostok_deutnat_delta_t=vostok_deutnat[3]

vostok_co2natt=np.loadtxt("vostok-co2nat.txt",skiprows=155,unpack=True)
vostok_co2natt_time=((vostok_co2natt[0]*-1)+2018)
vostok_co2natt_ppm_con=vostok_co2natt[1]


vostok_ch4nat=np.loadtxt("vostok-ch4nat.txt",skiprows=86,unpack=True)
vostok_ch4nat_time=((vostok_ch4nat[0]*-1)+2018)
vostok_ch4nat_ppm_con=vostok_ch4nat[1]

#Plotting Data

fig,(ax1, ax2,ax3)=plt.subplots(3,figsize=(8,8))
ax1.plot(GLB_time,GLB_temp,color='black')
ax1.set_xlim([1880,2020])
ax1.title.set_text('Global Temperature')
ax1.set_ylabel('Atmospheric Temperature[K]')

ax2.plot(co2_mm_mlo_time,co2_mm_mlo_ppm_con,color='r')
ax2.set_xlim([1880,2020])
ax2.set_ylabel('Atmospheric CO2 Concentration[PPM]')
ax2.title.set_text('CO2 Concentration')

ax3.plot(ch4_annmean_gl_YEAR,ch4_annmean_gl_CH4,color='b')
ax3.set_xlim([1880,2020])
ax3.title.set_text('CH4 Concentration')
ax3.set_xlabel('Gregorian Years')
ax3.set_ylabel('CH4 Concentration[PPB]')
plt.tight_layout()


fig,(ax1, ax2,ax3)=plt.subplots(3,figsize=(8,8))
ax1.plot(vostok_deutnat_time,vostok_deutnat_delta_t,color='black')
ax1.title.set_text('Global Temperature')
ax1.set_ylabel('Atmospheric Temperature[K]')
ax1.set_xlim([-420000,2020])
ax2.plot(vostok_co2natt_time,vostok_co2natt_ppm_con,color='r')
ax2.set_xlim([-420000,2020])
ax2.set_ylabel('Atmospheric CO2 Concentration[PPM]')
ax2.title.set_text('CO2 Concentration')

ax3.plot(vostok_ch4nat_time,vostok_ch4nat_ppm_con,color='b')
ax3.set_xlim([-420000,2020])
ax3.title.set_text('CH4 Concentration')
ax3.set_xlabel('Gregorian Years')
ax3.set_ylabel('CH4 Concentration[PPB]')
plt.tight_layout()

# Fitting a curve to the data 
plt.figure(figsize=(10,5))
parameters = np.polyfit(vostok_co2natt_time,vostok_co2natt_ppm_con,50)
print(parameters)
poly_function = np.poly1d(parameters)
expected_y = poly_function(vostok_co2natt_time)
plt.plot(vostok_co2natt_time,vostok_co2natt_ppm_con)
plt.plot(vostok_co2natt_time,expected_y)
new_x=[10,20,30,40,400]
poly_function(new_x)
plt.xlabel("time in years")
plt.ylabel("CO2 Concentration [PPM]")
