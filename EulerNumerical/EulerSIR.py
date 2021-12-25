import matplotlib.pyplot as plt
import numpy as np
steps = 100     
step_size = 1       
inf_0 = 1 
sus_0 = 1.0 
rec_0 = 1 
beta=0.06
gamma=0.02

inf = np.zeros(steps+1)
sus = np.zeros(steps+1)
rec = np.zeros(steps+1)
inf[0] = inf_0
sus[0] = sus_0
rec[0] = rec_0
for i in range(steps):
   
    inf_new = inf[i]+(beta*sus[i]*inf[i]-(gamma)*inf[i]*step_size)
    sus_new = sus[i]-(beta*sus[i]*inf[i]*step_size)
    rec_new = rec[i]+(gamma*inf[i]*step_size)
    
    inf[i+1] = inf_new
    sus[i+1] = sus_new
    rec[i+1] = rec_new
    
print(inf,sus,rec)
plt.plot(inf,color='r',label=('infected'))
plt.plot(rec,color='g',label=('recovered/safe'))
plt.plot(sus,color='y',label='susceptible')
plt.legend()
plt.title('SIR model with the Euler Method')
plt.xlabel('Time in Days')
plt.show()
