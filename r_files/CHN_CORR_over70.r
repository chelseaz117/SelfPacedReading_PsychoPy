library(lme4)
wholeCHN_CORR_over70 = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/CHN_CORR_over70.csv")
summary(wholeCHN_CORR_over70)

lR34 = lmer (log_R34 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70)
summary(lR34)

lR34withCorr = lmer (log_R34 ~ CORR * RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70)
summary(lR34withCorr)



RC1_S = subset(wholeCHN_CORR_over70, RC1 == "S")$log_R34
RC1_O = subset(wholeCHN_CORR_over70, RC1 == "O")$log_R34
t.test(RC1_S, RC1_O)# t = 4.0657, df = 1504.9, p-value = 5.036e-05

#RC2 on four levels:
SS_R89_rt = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R89
SO_R89_rt = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R89
OS_R89_rt = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R89
OO_R89_rt = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R89
t.test(SS_R89_rt, SO_R89_rt) #sig. t = -3.531, df = 777.91, p-value = 0.0004384; 3.166057  3.229264
t.test(OS_R89_rt, OO_R89_rt) #not sig. ;3.245063  3.216498 
#SS *>> OO >> SO >> OS
t.test(OS_R89_rt, SO_R89_rt) #not sig.
t.test(SS_R89_rt, OO_R89_rt) #sig. t = -2.7894, df = 777.93, p-value = 0.00541
t.test(SO_R89_rt, OO_R89_rt) #not sig.
 
#compare SS+OS and OO+SO in RC2:
lR89 = lmer (log_R89 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70)
summary(lR89)

lR89_onRC1 = lmer (log_R89 ~ log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeCHN_CORR_over70)
summary(lR89_onRC1)

RC2_S = subset(wholeCHN_CORR_over70, RC2 == "S")$log_R89
RC2_O = subset(wholeCHN_CORR_over70, RC2 == "O")$log_R89
t.test(RC2_S, RC2_O) #not sig. t = -1.2931, df = 1542.9, p-value = 0.1962 

#RC1+RC2, i.e. R3489
lR3489 = lmer (log_R3489 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70)
summary(lR3489)
RCs_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R3489
RCs_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R3489
RCs_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R3489
RCs_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R3489
t.test(RCs_SS, RCs_SO) #sig. t = -2.309, df = 773.29, p-value = 0.02121; 3.490907  3.525842 
t.test(RCs_OS, RCs_OO) #not sig.;3.514294  3.491944 
#SS >> OO >> OS >> SO
t.test(RCs_SS, RCs_OO) #not sig.
t.test(RCs_OS, RCs_SO) #not sig.
t.test(RCs_SS, RCs_OS) #not sig.
t.test(RCs_SO, RCs_OO) #sig. t = 2.3459, df = 777.91, p-value = 0.01923
t.test(RCs_OS, RCs_OO)

#Verb in RC1:
RC1_verb_S = subset(wholeCHN_CORR_over70, RC1 == "S")$log_R3
RC1_verb_O = subset(wholeCHN_CORR_over70, RC1 == "O")$log_R4
t.test(RC1_verb_S, RC1_verb_O) #not sig.
RC1_verb_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R3
RC1_verb_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R3
RC1_verb_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R4
RC1_verb_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R4
t.test(RC1_verb_SS, RC1_verb_SO) #not sig.
t.test(RC1_verb_OS, RC1_verb_OO) #not sig.
t.test(RC1_verb_SS, RC1_verb_OO) #not sig.

#Verb in RC2:
RC2_verb_S = subset(wholeCHN_CORR_over70, RC2 == "S")$log_R8
RC2_verb_O = subset(wholeCHN_CORR_over70, RC2 == "O")$log_R9
t.test(RC2_verb_S, RC2_verb_O) #t = -4.4937, df = 1557.4, p-value = 7.516e-06
RC2_verb_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R8
RC2_verb_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R9
RC2_verb_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R8
RC2_verb_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R9
t.test(RC2_verb_SS, RC2_verb_SO) #sig. t = -5.1314, df = 760.63, p-value = 3.654e-07; 2.783514  2.882948 
t.test(RC2_verb_OS, RC2_verb_OO) #not sig. t = -1.3522, df = 771.56, p-value = 0.1767;  2.833016  2.860857 
#SS *>> OS >> OO >> SO
 t.test(RC2_verb_SO, RC2_verb_OO) #not sig.
t.test(RC2_verb_SS, RC2_verb_OS) #sig. t = -2.5043, df = 752.48, p-value = 0.01248
t.test(RC2_verb_SO, RC2_verb_OS) #sig. t = 2.3605, df = 777.1, p-value = 0.0185

#edge of RC1
RC1_edge_S = subset(wholeCHN_CORR_over70, RC1 == "S")$log_R3
RC1_edge_O = subset(wholeCHN_CORR_over70, RC1 == "O")$log_R3
t.test(RC1_edge_S, RC1_edge_O) #t = -4.4019, df = 1556.2, p-value = 1.146e-05
RC1_edge_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R3
RC1_edge_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R3
RC1_edge_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R3
RC1_edge_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R3
t.test(RC1_edge_SS, RC1_edge_SO) #not sig.
t.test(RC1_edge_OS, RC1_edge_OO) #not sig.
#SS >> SO *>> OO >> OS
t.test(RC1_edge_SS, RC1_edge_OS) #sig. t = -3.5157, df = 777.87, p-value = 0.000464
t.test(RC1_edge_SS, RC1_edge_OO) #sig. t = -3.5318, df = 777.99, p-value = 0.000437
t.test(RC1_edge_SO, RC1_edge_OO) #sig. t = -2.6927, df = 775.35, p-value = 0.00724

#edge of RC2
RC2_edge_S = subset(wholeCHN_CORR_over70, RC2 == "S")$log_R8
RC2_edge_O = subset(wholeCHN_CORR_over70, RC2 == "O")$log_R8
t.test(RC2_edge_S, RC2_edge_O) #sig. t = -5.6476, df = 1545.1, p-value = 1.933e-08
RC2_edge_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R8
RC2_edge_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R8
RC2_edge_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R8
RC2_edge_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R8
t.test(RC2_edge_SS, RC2_edge_SO) #sig. t = -5.1123, df = 750.07, p-value = 4.044e-07
t.test(RC2_edge_OS, RC2_edge_OO) #sig. t = -2.9832, df = 777.87, p-value = 0.002941
#SS *>> OS *>> SO > OO
t.test(RC2_edge_SS, RC2_edge_OS) #sig. t = -2.5043, df = 752.48, p-value = 0.01248
t.test(RC2_edge_SO, RC2_edge_OS) #sig. t = 2.411, df = 777.94, p-value = 0.01614
t.test(RC2_edge_SO, RC2_edge_OO) #not sig.

#head_NP
head_NP_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R11
head_NP_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R11
head_NP_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R11
head_NP_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R11
t.test(head_NP_SS, head_NP_SO) #sig. t = -5.4092, df = 764.09, p-value = 8.475e-08
t.test(head_NP_OS, head_NP_OO) #sig. t = 2.522, df = 774.14, p-value = 0.01187
#SS >> OO *>> OS >> SO
t.test(head_NP_SS, head_NP_OO) #not sig.
t.test(head_NP_OS, head_NP_SO) #not sig.

#region 7
r8_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R8
r8_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R8
r8_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R8
r8_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R8

#region 8
r9_SS = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "S")$log_R9
r9_SO = subset(wholeCHN_CORR_over70, RC1 == "S" & RC2 == "O")$log_R9
r9_OS = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "S")$log_R9
r9_OO = subset(wholeCHN_CORR_over70, RC1 == "O" & RC2 == "O")$log_R9


