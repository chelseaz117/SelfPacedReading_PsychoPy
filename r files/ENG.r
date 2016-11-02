library(lme4)
library(lmerTest)
wholeENG = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/ENG.csv")
summary(wholeENG)
head(wholeENG)

lR78 = lmer (log_R78 ~ dprimeT * log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG)
summary(lR78)

SS = subset(wholeENG, RCtype == "SS")
SO = subset(wholeENG, RCtype == "SO")
OS = subset(wholeENG, RCtype == "OS")
OO = subset(wholeENG, RCtype == "OO")

SS_SO = subset(wholeENG, RCtype == "SO" | RCtype == "SS")
OS_OO = subset(wholeENG, RCtype == "OS" | RCtype == "OO")
SS_OS = subset(wholeENG, RCtype == "OS" | RCtype == "SS")
SO_OO = subset(wholeENG, RCtype == "SO" | RCtype == "OO")
SO_OS = subset(wholeENG, RCtype == "SO" | RCtype == "OS")
SS_OO = subset(wholeENG, RCtype == "SS" | RCtype == "OO")


summary(SS) #log_R78: mean = 3.150
summary(SO) #log_R78: mean = 3.133
summary(OS) #log_R78: mean = 3.154
summary(OO) #log_R78: mean = 3.120 
#OO >> SO >> SS >> OS

#---------------------------------------------------------------------------------------------------------------------#
#SS vs. SO 
summary(lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SS_SO)) #not sig.t = 0.679
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SS_SO)) #t = 0.701
summary(lmer(log_R78 ~ RCtype + (1|Participant)+(1|Item), SS_SO)) #t = 1.227
#OO vs. OS 
summary(lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), OS_OO)) #sig. t = 1.998
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), OS_OO)) # t = 2.05
summary(lmer(log_R78 ~ RCtype + (1|Participant)+(1|Item), OS_OO)) # t = 2.419
#SS vs. SO 
summary(lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SS_OS)) #not sig. t = 0.409
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SS_OS)) #t = 0.343
summary(lmer(log_R78 ~ RCtype + (1|Participant)+(1|Item), SS_OS)) # t = -0.265
#OO vs. SO 
summary(lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SO_OO)) #not sig. t = 1.337
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SO_OO)) # t = 1.315
summary(lmer(log_R78 ~ RCtype + (1|Participant)+(1|Item), SO_OO)) # t = 0.932
#SO vs. OS #not sig. t = -0.006
summary(lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SO_OS))
#SS vs. OO #sig. t = 2.239
summary(lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SS_OO))
#-----------------------------------------------------------------------------------#
#SS vs. SO 
summary(lmer(log_R78 ~ dprimeT * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SS_SO))
summary(lmer(log_R78 ~ log_R34 * dprimeT * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SS_SO)) # SS vs. SO not sig.
#OO vs. OS 
summary(lmer(log_R78 ~ log_R34 * dprimeT * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), OS_OO)) #couldn't converge
summary(lmer(log_R78 ~ dprimeT * RCtype + (1+log_R34|Participant)+(1+log_R34|Item), OS_OO)) #???
summary(lmer(log_R78 ~ log_R34 * dprimeT * RCtype + (1|Participant)+(1|Item), OS_OO)) #???
summary(lmer(log_R78 ~ dprimeT * RCtype + (1|Participant)+(1|Item), OS_OO)) #???
summary(lmer(log_R78 ~ RCtype  + (1|Participant)+(1|Item), OS_OO))
summary(lmer(log_R78 ~ RCtype  + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), OS_OO))

#SS vs. SO 
summary(lmer(log_R78 ~ log_R34 * dprimeT * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), SS_OS)) #not sig. t = 0.409

#-----------------------------------------------------------------------------------#
summary(lmer(log_R78 ~ dprimeT * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG))
#-----------------------------------------------------------------------------------#
# OO
m.1 = lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.1)
#relevel: 0S
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "OS")
m.2 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.2)
#relevel: SO
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SO")
m.3 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.3)
#relevel: SS
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SS")
m.4 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.4)

#English
library(lme4)
library(lmerTest)
wholeENG = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/ENG.csv")
summary(wholeENG)
head(wholeENG)
SS = subset(wholeENG, RCtype == "SS")
SO = subset(wholeENG, RCtype == "SO")
OS = subset(wholeENG, RCtype == "OS")
OO = subset(wholeENG, RCtype == "OO")
#---------------------------------------------------------------------------------------------------------#
#Region78 (RC2)
summary(SS) #log_R78: mean = 3.150
summary(SO) #log_R78: mean = 3.133
summary(OS) #log_R78: mean = 3.154
summary(OO) #log_R78: mean = 3.120 
#---------------------------------------------------------------------------------------------------------#
# OO
m.1 = lmer(log_R78 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.1)
"""Fixed effects:
Estimate Std. Error        df t value Pr(>|t|)    
(Intercept)   3.14345    0.01780  48.05000 176.636   <2e-16 ***
RCtypeOS      0.02444    0.01457 151.15000   1.678   0.0954 .  
RCtypeSO      0.01891    0.01418 176.76000   1.333   0.1842    
RCtypeSS      0.02978    0.01416 174.54000   2.102   0.0369 * """
#---------------------------------------------------------------------------------------------------------#
#relevel: 0S
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "OS")
m.2 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.2)
"""Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)         3.167895   0.017856  48.240000 177.417   <2e-16 ***
RCtypeReleveledOO  -0.024444   0.014567 151.160000  -1.678   0.0954 .  
RCtypeReleveledSO  -0.005536   0.014298 173.080000  -0.387   0.6991    
RCtypeReleveledSS   0.005336   0.014282 173.060000   0.374   0.7092 """
#---------------------------------------------------------------------------------------------------------#
#relevel: SO
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SO")
m.3 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.3)
"""Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)         3.162358   0.017768  47.960000 177.982   <2e-16 ***
RCtypeReleveledOO  -0.018908   0.014183 176.770000  -1.333    0.184    
RCtypeReleveledOS   0.005536   0.014298 173.080000   0.387    0.699    
RCtypeReleveledSS   0.010872   0.013688 185.960000   0.794    0.428 """
#---------------------------------------------------------------------------------------------------------#
#relevel: SS
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SS")
m.4 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.4)
"""
Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)         3.173230   0.017767  48.380000 178.603   <2e-16 ***
RCtypeReleveledOO  -0.029780   0.014164 174.540000  -2.102   0.0369 *  
RCtypeReleveledOS  -0.005336   0.014282 173.060000  -0.374   0.7092    
RCtypeReleveledSO  -0.010872   0.013688 185.960000  -0.794   0.4281 """
#---------------------------------------------------------------------------------------------------------#
#Verb in RC2
#---------------------------------------------------------------------------------------------------------#
summary(SS) #log_R7: mean = 2.829
summary(SO) #log_R8: mean = 2.774
summary(OS) #log_R7: mean = 2.795
summary(OO) #log_R8: mean = 2.766
#---------------------------------------------------------------------------------------------------------#
# OO >> SO >> OS >> SS
|
  #----------------------
#OO vs. SO
m.1.VinRC2 = lmer(log_VinRC2 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.1.VinRC2)
"""Fixed effects:
Estimate Std. Error        df t value Pr(>|t|)    
(Intercept)   2.77247    0.01636  36.70000 169.487  < 2e-16 ***
RCtypeOS      0.02223    0.01490 229.30000   1.492    0.137    
RCtypeSO      0.01417    0.01484 356.30000   0.954    0.340    
RCtypeSS      0.06510    0.01482 362.30000   4.392 1.47e-05 *** """
#---------------------------------------------------------------------------------------------------------#
#SO vs. SS
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SO")
m.2.VinRC2 = lmer(log_VinRC2 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.2.VinRC2)
"""Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)         2.786639   0.016567  39.700000 168.207  < 2e-16 ***
RCtypeReleveledOO  -0.014166   0.014842 356.300000  -0.954 0.340487    
RCtypeReleveledOS   0.008063   0.014899 333.600000   0.541 0.588752    
RCtypeReleveledSS   0.050937   0.014571 477.900000   3.496 0.000517 *** """
#---------------------------------------------------------------------------------------------------------#
#Noun in RC2
#OO vs. SO
m.1.NinRC2 = lmer(log_NinRC2 ~ RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.1.NinRC2)
"""Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)   2.845523   0.019961  84.880000 142.553   <2e-16 ***
RCtypeOS      0.021834   0.018313 135.790000   1.192    0.235    
RCtypeSO      0.021591   0.017813 143.990000   1.212    0.227    
RCtypeSS     -0.006827   0.017799 142.160000  -0.384    0.702  """
#---------------------------------------------------------------------------------------------------------#
#SO vs. SS
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SO")
m.2.NinRC2 = lmer(log_NinRC2 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.2.NinRC2)
"""Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)         2.786639   0.016567  39.700000 168.207  < 2e-16 ***
RCtypeReleveledOO  -0.014166   0.014842 356.300000  -0.954 0.340487    
RCtypeReleveledOS   0.008063   0.014899 333.600000   0.541 0.588752    
RCtypeReleveledSS   0.050937   0.014571 477.900000   3.496 0.000517 *** """

#---------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#                               
# ADD MORE PREDICTORS-------------------------------------------------------------------------------------#  
#---------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
#Region78 (RC2)
#---------------------------------------------------------------------------------------------------------#
# OO
m.1 = lmer(log_R78 ~ dprimeT * log_R34 * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.1)
"""Fixed effects:
Estimate Std. Error         df t value Pr(>|t|)    
(Intercept)               2.225e+00  2.240e-01  7.810e+01   9.932 1.78e-15 ***
dprimeT                   4.255e-01  1.462e-01  8.930e+01   2.911 0.004544 ** 
log_R34                   2.364e-01  6.957e-02  1.107e+02   3.398 0.000944 ***
RCtypeOS                 -4.210e-02  2.356e-01  5.839e+02  -0.179 0.858238    
RCtypeSO                 -5.280e-02  2.482e-01  6.970e+02  -0.213 0.831614    
RCtypeSS                 -4.427e-01  2.575e-01  7.233e+02  -1.719 0.086041 .  
dprimeT:log_R34          -9.946e-02  4.282e-02  9.300e+01  -2.323 0.022366 *  
dprimeT:RCtypeOS         -1.179e-01  1.493e-01  1.888e+03  -0.790 0.429780    
dprimeT:RCtypeSO         -2.994e-02  1.547e-01  1.881e+03  -0.194 0.846534    
dprimeT:RCtypeSS          1.448e-01  1.563e-01  1.814e+03   0.926 0.354351    
log_R34:RCtypeOS          1.693e-02  7.299e-02  4.861e+02   0.232 0.816672    
log_R34:RCtypeSO          2.502e-02  7.823e-02  6.060e+02   0.320 0.749229    
log_R34:RCtypeSS          1.524e-01  8.101e-02  6.233e+02   1.881 0.060469 .  
dprimeT:log_R34:RCtypeOS  3.924e-02  4.484e-02  1.943e+03   0.875 0.381604    
dprimeT:log_R34:RCtypeSO  7.675e-03  4.747e-02  1.950e+03   0.162 0.871575    
dprimeT:log_R34:RCtypeSS -4.688e-02  4.783e-02  1.870e+03  -0.980 0.327185     """
#---------------------------------------------------------------------------------------------------------#
m.1again = lmer(log_R78 ~ dprimeT * RCtype + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.1again)
"""
Fixed effects:
Estimate Std. Error        df t value Pr(>|t|)    
(Intercept)      2.977e+00  4.007e-02 4.633e+01  74.290  < 2e-16 ***
dprimeT          1.252e-01  3.019e-02 4.324e+01   4.148 0.000154 ***
RCtypeOS         3.616e-03  2.604e-02 1.522e+02   0.139 0.889746    
RCtypeSO         1.763e-02  2.624e-02 1.724e+02   0.672 0.502504    
RCtypeSS         2.558e-02  2.624e-02 1.720e+02   0.975 0.331053    
dprimeT:RCtypeOS 1.726e-02  1.727e-02 7.780e+01   1.000 0.320518    
dprimeT:RCtypeSO 8.469e-04  1.751e-02 8.160e+01   0.048 0.961533    
dprimeT:RCtypeSS 3.644e-03  1.747e-02 8.136e+01   0.209 0.835322 """
#---------------------------------------------------------------------------------------------------------#
#relevel: 0S
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "OS")
m.2 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.2)

#---------------------------------------------------------------------------------------------------------#
#relevel: SO
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SO")
m.3 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.3)

#---------------------------------------------------------------------------------------------------------#
#relevel: SS
wholeENG$RCtypeReleveled = relevel(wholeENG$RCtype, "SS")
m.4 = lmer(log_R78 ~ RCtypeReleveled + (1+log_R34+dprimeT|Participant)+(1+log_R34+dprimeT|Item), wholeENG)
summary(m.4)
"""
 """
#---------------------------------------------------------------------------------------------------------#


