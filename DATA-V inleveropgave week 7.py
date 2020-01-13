import numpy as np
import matplotlib.pyplot as plt
import scipy.odr as odr


t = np.array([0.25,0.75,1.25,2.5,3.0,3.75,4.5,5.5,7.0,8.5])
d = np.array([1.43,2.06,2.09,2.66,3.31,3.52,3.79,4.12,4.35,4.95])
sig_d = np.array([0.20,0.20,0.20,0.20,0.20,0.20,0.20,0.20,0.20,0.20])

#plt.figure()
#plt.plot(t,d, label='.')
#plt.errorbar(t,d,xerr=0.0,yerr=sig_d,fmt='y.', label='.')
#plt.legend()

f,ax = plt.subplots(1)
ax.errorbar(t,d,xerr=0.0,yerr=sig_d,fmt='y.')
#ax.show()
A_start=2.6
B_start=1.5

def d(B, t):
    return np.sqrt(B[0] + B[1]*t)

odr_model = odr.Model(d)
odr_data  = odr.RealData(t,d,sy=sig_d)

## (2) Definieer het model-object om te gebruiken in odr
odr_model = odr.Model(d)

odr_obj   = odr.ODR(odr_data,odr_model,beta0=[A_start,B_start])
odr_obj.set_job(fit_type=2)

odr_res   = odr_obj.run()

par_best = odr_res.beta
par_sig_ext = odr_res.sd_beta
par_cov = odr_res.cov_beta 
print(" De (INTERNE!) covariantiematrix  = \n", par_cov)
chi2 = odr_res.sum_square
print("\n Chi-squared         = ", chi2)
chi2red = odr_res.res_var
print(" Reduced chi-squared = ", chi2red, "\n")

odr_res.pprint()

# Hier plotten we ter controle de aanpassing met de dataset (niet opgemaakt)
xplot=np.arange(-1,13,1)
ax.plot(xplot,np.sqrt(par_best[0] + par_best[1]*xplot),'r-')
plt.show()

#def d(t):
#    return np.sqrt(A+B*t)

#plt.plot(t,d(t))
#plt.show()