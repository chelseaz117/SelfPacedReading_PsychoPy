library(lme4)
library(lmerTest)
wholeENG = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/ENG.csv")
wholeENG_CORR = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/ENG_CORR.csv")
summary(wholeENG)
summary(wholeENG_CORR)

#------------------------------------------------------------------------------------------------------#
m_Region1 = lmer(log_R1 ~ RC1fac * RC2fac + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG)
summary(m_Region1) #nothing is significant
m_Region1_CORR = lmer(log_R1 ~ RC1fac * RC2fac + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG_CORR)
summary(m_Region1_CORR) #nothing is significant
#------------------------------------------------------------------------------------------------------#
m_Region2 = lmer(log_R2 ~ RC1fac * RC2fac + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG)
summary(m_Region2) #nothing is significant
m_Region2_CORR = lmer(log_R2 ~ RC1fac * RC2fac + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG_CORR)
summary(m_Region2_CORR) #nothing is significant
#------------------------------------------------------------------------------------------------------#
m_Region3 = lmer(log_R3 ~ RC1fac * RC2fac + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG)
summary(m_Region3) # RC1fac        -0.061187   0.011870 75.620000  -5.155 1.97e-06 ***
m_Region3_nonfac = lmer(log_R3 ~ RC1 * RC2 + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG)
summary(m_Region3_nonfac) # RC1S        -0.04320    0.01679 75.62000  -2.573    0.012 *   
m_Region3_CORR = lmer(log_R3 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region3_CORR) # RC1fac        -0.049952   0.012915 75.140000  -3.868 0.000232 ***
#------------------------------------------------------------------------------------------------------#
m_Region4 = lmer(log_R4 ~ RC1fac * RC2fac + (1*dprimeT|Participant)+(1*dprimeT|Item), wholeENG)
summary(m_Region4) # RC1fac        -1.171e-01  1.419e-02  2.103e+03  -8.253 2.22e-16 ***
m_Region4_CORR = lmer(log_R4 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region4_CORR) # RC1fac          -0.11595    0.01676 1534.50000  -6.916 6.77e-12 ***
#------------------------------------------------------------------------------------------------------#
m_Region5 = lmer(log_R5 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region5) #nothing is significant
m_Region5_CORR = lmer(log_R5 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region5_CORR) #nothing is significant
#------------------------------------------------------------------------------------------------------#
m_Region6 = lmer(log_R6 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region6) #nothing is significant
m_Region6_CORR = lmer(log_R6 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region6_CORR) #nothing is significant
#------------------------------------------------------------------------------------------------------#
m_Region7 = lmer(log_R7 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region7) # RC1fac         0.02612    0.01172 74.33000   2.228   0.0289 *  
m_Region7_CORR = lmer(log_R7 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region7_CORR) # RC1fac         0.03719    0.01384 73.49000   2.688   0.0089 **
#------------------------------------------------------------------------------------------------------#
m_Region8 = lmer(log_R8 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region8) # RC2fac         0.05345    0.01106 73.27000   4.831 7.25e-06 ***
                   # RC1fac:RC2fac -0.04532    0.02213 73.27000  -2.048   0.0441 *  
m_Region8_CORR = lmer(log_R8 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region8_CORR) # RC2fac        -0.04825    0.01304 75.67000  -3.701 0.000405 ***
#------------------------------------------------------------------------------------------------------#
m_Region9 = lmer(log_R9 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region9) # RC2fac        -0.043866   0.009771 72.610000  -4.489 2.63e-05 ***
                   # RC1fac:RC2fac -0.041879   0.019543 72.610000  -2.143   0.0355 * 
m_Region9_CORR = lmer(log_R9 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region9_CORR) # RC2fac        -0.05253    0.01143 72.10000  -4.596 1.79e-05 ***
#------------------------------------------------------------------------------------------------------#
m_Region10 = lmer(log_R10 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region10) # RC1fac         0.015505   0.007164 74.120000   2.164   0.0337 *  
m_Region10_CORR = lmer(log_R10 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG_CORR)
summary(m_Region10_CORR) # RC1fac         1.662e-02  8.376e-03  1.538e+03   1.984   0.0474 *  
#------------------------------------------------------------------------------------------------------#
m_Region78 = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region78) # RC2fac         0.025201   0.009754 73.930000   2.584   0.0117 * 
m_Region789 = lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region789) #nothing sig
m_Region89 = lmer(log_R89 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region89) # RC1fac:RC2fac -0.0475380  0.0177715 70.9800000  -2.675  0.00927 ** 

OS_SO = subset(wholeENG, RC1fac==-0.5 & RC2fac==0.5| RC1fac==0.5 & RC2fac==-0.5)
summary(OS_SO)
m_Region78_OS_SO = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OS_SO)
summary(m_Region8910_OS_SO)

SS_SO = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==0.5 & RC2fac==-0.5)
m_Region78_SS_SO= lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_SO)
summary(m_Region78_SS_SO) #not sig.

SS_OO = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==-0.5)
m_Region78_SS_OO= lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OO)
summary(m_Region78_SS_OO) #sig.

SS_OS = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==0.5)
m_Region78_SS_OS = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_Region78_SS_OS) # not sig. -0.265 

SO_OO = subset(wholeENG, RC1fac==0.5 & RC2fac==-0.5| RC1fac==-0.5 & RC2fac==-0.5)
m_Region78_SO_OO = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SO_OO)
summary(m_Region78_SO_OO) # not sig. 0.932 

OS_OO = subset(wholeENG, RC1fac==-0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==-0.5)
m_Region78_OS_OO = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OS_OO)
summary(m_Region78_OS_OO) #sig
#------------------------------------------------------------------------------------------------------#

SS_OS = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==0.5)
OO_SO = subset(wholeENG, RC1fac==-0.5 & RC2fac==-0.5| RC1fac==0.5 & RC2fac==-0.5)
#------------------------------------------------------------------------------------------------------#
m_SS_OS = lmer(log_R7 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_SS_OS) #RC1fac      3.388e-02  1.548e-02 1.025e+03   2.189   0.0288 *  
m_OO_SO = lmer(log_R7 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OO_SO)
summary(m_OO_SO) #not significant
#------------------------------------------------------------------------------------------------------#
m_SS_OS = lmer(log_R8 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_SS_OS) #RC1fac      -0.03727    0.01854 35.40000   -2.01   0.0521 .  
m_OO_SO = lmer(log_R8 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OO_SO)
summary(m_OO_SO) #not significant
#------------------------------------------------------------------------------------------------------#
m_SS_OS = lmer(log_R9 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_SS_OS) #not significant 
m_OO_SO = lmer(log_R9 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OO_SO)
summary(m_OO_SO) #RC1fac       0.03897    0.01536 36.95000   2.537   0.0155 *  
#------------------------------------------------------------------------------------------------------#
m_SS_OS = lmer(log_R10 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_SS_OS) # not sig. RC1fac       0.01927    0.01031 36.69000    1.87   0.0695 .   
m_OO_SO = lmer(log_R10 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OO_SO)
summary(m_OO_SO) # not sig.
#------------------------------------------------------------------------------------------------------#
#Checking if parallelism is significant
#------------------------------------------------------------------------------------------------------#

m_Region7_P_again = lmer(log_R7 ~ ParFac * RC2fac + (1*dprimeT*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region7_P_again) # ParFac:RC2fac  0.052242   0.023445 74.330000   2.228   0.0289 *  
#------------------------------------------------------------------------------------------------------#
m_Region8_P_again = lmer(log_R8 ~ ParFac * RC2fac + (1*dprimeT*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region8_P_again)# ParFac        -0.02266    0.01106 73.27000  -2.048   0.0441 *  
                          # RC2fac         0.05345    0.01106 73.27000   4.831 7.25e-06 ***
#------------------------------------------------------------------------------------------------------#
m_Region9_P_again = lmer(log_R9 ~ ParFac * RC2fac + (1*dprimeT*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region9_P_again) # ParFac        -0.020940   0.009771 72.610000  -2.143   0.0355 *  
                           # RC2fac        -0.043866   0.009771 72.610000  -4.489 2.63e-05 ***
#------------------------------------------------------------------------------------------------------#
m_Region10_P_again = lmer(log_R10 ~ ParFac * RC2fac + (1*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region10_P_again) # ParFac:RC2fac  0.031009   0.014329 74.120000   2.164   0.0337 *  
#------------------------------------------------------------------------------------------------------#
m_Region78_P_again = lmer(log_R78 ~ ParFac * RC2fac + (1*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region78_P_again) 

m_Region789_P_again = lmer(log_R789 ~ ParFac * RC2fac + (1*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region789_P_again)
