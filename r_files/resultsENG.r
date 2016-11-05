library(lme4)
library(lmerTest)
wholeENG = read.csv("/Users/chongzhang/Onedrive/SelfPacedReading_PsychoPy/ENG.csv")
summary(wholeENG)


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
m_Region3 = lmer(log_R3 ~ RC1fac * RC2fac + (1+dprimeT|Participant)+(1+dprimeT|Item), wholeENG)
summary(m_Region3) #RC1fac        -0.06107    0.01187 75.71000  -5.145 2.04e-06 ***

#------------------------------------------------------------------------------------------------------#
m_Region4 = lmer(log_R4 ~ RC1fac * RC2fac + (1+dprimeT|Participant)+(1+dprimeT|Item), wholeENG)
summary(m_Region4) # RC1fac         -0.11782    0.01423 935.60000  -8.278 4.44e-16 ***

m_Region34 = lmer(log_R34 ~ RC1fac * RC2fac + (1+dprimeT|Participant)+(1+dprimeT|Item), wholeENG)
summary(m_Region34)
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
m_Region7 = lmer(log_R7 ~ RC1fac * RC2fac + (1+log_R4*dprimeT|Participant)+(1+log_R4*dprimeT|Item), wholeENG)
summary(m_Region7) # failed to converge
m_Region7 = lmer(log_R7 ~ RC1fac * RC2fac + (1+log_R4*dprimeT|Participant)+(1+log_R4+dprimeT|Item), wholeENG)
summary(m_Region7) # failed to converge  
m_Region7 = lmer(log_R7 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4*dprimeT|Item), wholeENG)
summary(m_Region7)  # failed to converge 
m_Region7 = lmer(log_R7 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4+dprimeT|Item), wholeENG)
summary(m_Region7) # RC1fac          0.03098    0.01199 135.59000   2.584   0.0108 *

#------------------------------------------------------------------------------------------------------#
m_Region8 = lmer(log_R8 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4+dprimeT|Item), wholeENG)
summary(m_Region8) # RC2fac          0.048127   0.011412 166.530000   4.217 4.05e-05 ***
m_Region8 = lmer(log_R8 ~ RC1fac * RC2fac + (1*log_R4+dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region8)  # RC2fac         0.05346    0.01112 73.16000   4.808 7.93e-06 ***
                    # RC1fac:RC2fac -0.04532    0.02224 73.16000  -2.038   0.0452 *  
m_Region8 = lmer(log_R8 ~ RC1fac * RC2fac + (1|Participant)+(1|Item), wholeENG)
summary(m_Region8)

m_Region78 = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region78) # RC2fac         0.025201   0.009754 73.930000   2.584   0.0117 *
m_Region89 = lmer(log_R89 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region89) # RC1fac:RC2fac -0.0475380  0.0177715 70.9800000  -2.675  0.00927 ** 

m_Region789 = lmer(log_R789 ~ RC1fac * RC2fac + (1+log_R4*dprimeT|Participant)+(1+log_R4*dprimeT|Item), wholeENG)
summary(m_Region789)

#------------------------------------------------------------------------------------------------------#
m_Region9 = lmer(log_R9 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4+dprimeT|Item), wholeENG)
summary(m_Region9) #RC1fac          0.02260    0.01031 154.87000   2.192 0.029838 *  
  #RC2fac         -0.04063    0.01019 145.71000  -3.986 0.000106 ***
  #RC1fac:RC2fac  -0.03978    0.02039 146.54000  -1.951 0.052960 .

m_Region9 = lmer(log_R9 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), wholeENG)
summary(m_Region9)  # RC2fac        -0.043866   0.009771 72.610000  -4.489 2.63e-05 ***
                    # RC1fac:RC2fac -0.041879   0.019543 72.610000  -2.143   0.0355 *  
#------------------------------------------------------------------------------------------------------#
 
m_Region10 = lmer(log_R10 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4+dprimeT|Item), wholeENG)
summary(m_Region10)  
  
#------------------------------------------------------------------------------------------------------#
m_Region78 = lmer(log_R78 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4+dprimeT|Item), wholeENG)
summary(m_Region78) 


#------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------#
OS_SO = subset(wholeENG, RC1fac==-0.5 & RC2fac==0.5| RC1fac==0.5 & RC2fac==-0.5)
summary(OS_SO)
m_Region78_OS_SO = lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OS_SO)
summary(m_Region8910_OS_SO)

SS_SO = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==0.5 & RC2fac==-0.5)
m_Region78_SS_SO= lmer(log_R78 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_SO)
summary(m_Region78_SS_SO) #not sig.
m_Region78_SS_SO= lmer(log_R78 ~ RC1fac * RC2fac + (1|Participant)+(1|Item), SS_SO)
summary(m_Region78_SS_SO)

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
#------------------------------------------------------------------------------------------------------#
mean = aggregate(log_R789 ~ RCtype, wholeENG, mean)
mean
OS_SO = subset(wholeENG, RC1fac==-0.5 & RC2fac==0.5| RC1fac==0.5 & RC2fac==-0.5)
summary(OS_SO)
m_Region789_OS_SO = lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OS_SO)
summary(m_Region789_OS_SO) #not sig.

SS_OO = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==-0.5)
m_Region789_SS_OO= lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OO)
summary(m_Region789_SS_OO) # not sig.

SS_OS = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==0.5)
m_Region789_SS_OS = lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_Region789_SS_OS) # not sig. -0.265 

SO_OO = subset(wholeENG, RC1fac==0.5 & RC2fac==-0.5| RC1fac==-0.5 & RC2fac==-0.5)
m_Region789_SO_OO = lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SO_OO)
summary(m_Region789_SO_OO) # not sig. 0.932 

OS_OO = subset(wholeENG, RC1fac==-0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==-0.5)
m_Region789_OS_OO = lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OS_OO)
summary(m_Region789_OS_OO) # not sig

SS_SO = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==0.5 & RC2fac==-0.5)
m_Region789_SS_SO = lmer(log_R789 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_SO)
summary(m_Region789_SS_SO) # not sig

#------------------------------------------------------------------------------------------------------#



SS_OS = subset(wholeENG, RC1fac==0.5 & RC2fac==0.5| RC1fac==-0.5 & RC2fac==0.5)
OO_SO = subset(wholeENG, RC1fac==-0.5 & RC2fac==-0.5| RC1fac==0.5 & RC2fac==-0.5)
#------------------------------------------------------------------------------------------------------#
m_SS_OS = lmer(log_R7 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), SS_OS)
summary(m_SS_OS) #RC1fac      3.388e-02  1.548e-02 1.025e+03   2.189   0.0288 *  
m_OO_SO = lmer(log_R7 ~ RC1fac * RC2fac + (1*log_R4*dprimeT|Participant)+(1*log_R4*dprimeT|Item), OO_SO)
summary(m_OO_SO) #not significant
#------------------------------------------------------------------------------------------------------#
m_SS_OS = lmer(log_R8 ~ RC1fac * RC2fac + (1+log_R4+dprimeT|Participant)+(1+log_R4+dprimeT|Item), SS_OS)
summary(m_SS_OS) # with all stars: RC1fac      -0.03727    0.01854 35.40000   -2.01   0.0521 . 
                 # with all plus: nothing sig.
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

m_Region78_P_again = lmer(log_R78 ~ ParFac * RC2fac + (1+ParFac + RC2fac|Participant)+(1+ParFac + RC2fac|Item), wholeENG)
summary(m_Region78_P_again) 

m_Region789_P_again = lmer(log_R789 ~ ParFac * RC2fac + (1*ParFac * RC2fac|Participant)+(1|Item), wholeENG)
summary(m_Region789_P_again)
