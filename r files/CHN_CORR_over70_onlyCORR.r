library(lme4)
wholeCHN_CORR_over70_onlyCORR = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/CHN_CORR_over70_onlyCORR.csv")
summary(wholeCHN_CORR_over70_onlyCORR)

lR34withCorr = lmer (log_R34 ~ CORR * RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70_onlyCORR)
summary(lR34withCorr)
lR34 = lmer (log_R34 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70_onlyCORR)
summary(lR34)

RC1_S = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S")$log_R34
RC1_O = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O")$log_R34
t.test(RC1_S, RC1_O)# t = 3.5073, df = 1285.3, p-value = 0.0004682

#RC2 on four levels:
SS_R89_rt = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R89
SO_R89_rt = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R89
OS_R89_rt = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R89
OO_R89_rt = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R89
t.test(SS_R89_rt, SO_R89_rt) #sig. t = -2.8457, df = 647.56, p-value = 0.004571
t.test(OS_R89_rt, OO_R89_rt) #not sig. ;3.245063  3.216498 
#SS *>> OO >> SO >> OS
t.test(OS_R89_rt, SO_R89_rt) #not sig.
t.test(SS_R89_rt, OO_R89_rt) #sig.t = -2.4491, df = 687.35, p-value = 0.01457
t.test(SO_R89_rt, OO_R89_rt) #not sig.

#compare SS+OS and OO+SO in RC2:
lR89 = lmer (log_R89 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70_onlyCORR)
summary(lR89)

lR89_onRC1 = lmer (log_R89 ~ log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeCHN_CORR_over70_onlyCORR)
summary(lR89_onRC1)

RC2_S = subset(wholeCHN_CORR_over70_onlyCORR, RC2 == "S")$log_R89
RC2_O = subset(wholeCHN_CORR_over70_onlyCORR, RC2 == "O")$log_R89
t.test(RC2_S, RC2_O) #not sig. t = -0.78983, df = 1347.1, p-value = 0.4298

#RC1+RC2, i.e. R3489
lR3489 = lmer (log_R3489 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN_CORR_over70_onlyCORR)
summary(lR3489)
RCs_SS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R3489
RCs_SO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R3489
RCs_OS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R3489
RCs_OO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R3489
t.test(RCs_SS, RCs_SO) #not sig. t = -1.8329, df = 656.18, p-value = 0.06727 
t.test(RCs_OS, RCs_OO) #not sig.;3.514294  3.491944 
#SS >> OO >> OS >> SO
t.test(RCs_SS, RCs_OO) #not sig.
t.test(RCs_OS, RCs_SO) #not sig.
t.test(RCs_SS, RCs_OS) #not sig.
t.test(RCs_SO, RCs_OO) #sig. t = 1.8031, df = 642.16, p-value = 0.07185
t.test(RCs_OS, RCs_OO)

#Verb in RC1:
RC1_verb_S = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S")$log_R3
RC1_verb_O = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O")$log_R4
t.test(RC1_verb_S, RC1_verb_O) #not sig.
RC1_verb_SS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R3
RC1_verb_SO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R3
RC1_verb_OS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R4
RC1_verb_OO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R4
t.test(RC1_verb_SS, RC1_verb_SO) #not sig.
t.test(RC1_verb_OS, RC1_verb_OO) #not sig.
t.test(RC1_verb_SS, RC1_verb_OO) #not sig.

#Verb in RC2:
RC2_verb_S = subset(wholeCHN_CORR_over70_onlyCORR, RC2 == "S")$log_R8
RC2_verb_O = subset(wholeCHN_CORR_over70_onlyCORR, RC2 == "O")$log_R9
t.test(RC2_verb_S, RC2_verb_O) #t = -4.7638, df = 1330.1, p-value = 2.108e-06
RC2_verb_SS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R8
RC2_verb_SO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R9
RC2_verb_OS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R8
RC2_verb_OO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R9
t.test(RC2_verb_SS, RC2_verb_SO) #sig. t = -5.0878, df = 603.25, p-value = 4.845e-07 
t.test(RC2_verb_OS, RC2_verb_OO) #not sig. t = -1.3522, df = 771.56, p-value = 0.1767;  2.833016  2.860857 
#SS *>> OS >> OO >> SO
t.test(RC2_verb_SO, RC2_verb_OO) #not sig.
t.test(RC2_verb_SS, RC2_verb_OS) #not sig. t = -1.9149, df = 670.25, p-value = 0.05593
t.test(RC2_verb_SO, RC2_verb_OS) #sig. t = 2.3605, df = 777.1, p-value = 0.0185

#edge of RC1
RC1_edge_S = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S")$log_R3
RC1_edge_O = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O")$log_R3
t.test(RC1_edge_S, RC1_edge_O) #t = -4.3852, df = 1348.1, p-value = 1.249e-05
RC1_edge_SS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R3
RC1_edge_SO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R3
RC1_edge_OS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R3
RC1_edge_OO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R3
t.test(RC1_edge_SS, RC1_edge_SO) #not sig.
t.test(RC1_edge_OS, RC1_edge_OO) #not sig.
#SS >> SO *>> OO >> OS
t.test(RC1_edge_SS, RC1_edge_OS) #sig.
t.test(RC1_edge_SS, RC1_edge_OO) #sig. 
t.test(RC1_edge_SO, RC1_edge_OO) #sig. 

#edge of RC2
RC2_edge_S = subset(wholeCHN_CORR_over70_onlyCORR, RC2 == "S")$log_R8
RC2_edge_O = subset(wholeCHN_CORR_over70_onlyCORR, RC2 == "O")$log_R8
t.test(RC2_edge_S, RC2_edge_O) #sig. t = -4.26, df = 1325.1, p-value = 2.189e-05
RC2_edge_SS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R8
RC2_edge_SO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R8
RC2_edge_OS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R8
RC2_edge_OO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R8
t.test(RC2_edge_SS, RC2_edge_SO) #sig. t = -3.2949, df = 609.29, p-value = 0.001042
t.test(RC2_edge_OS, RC2_edge_OO) #sig. t = -2.6906, df = 687.99, p-value = 0.007307
#SS *>> OS *>> SO > OO
t.test(RC2_edge_SS, RC2_edge_OS) #not sig.
t.test(RC2_edge_SO, RC2_edge_OS) #not sig.
t.test(RC2_edge_SO, RC2_edge_OO) #not sig.

#head_NP
head_NP_SS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "S")$log_R11
head_NP_SO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "S" & RC2 == "O")$log_R11
head_NP_OS = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "S")$log_R11
head_NP_OO = subset(wholeCHN_CORR_over70_onlyCORR, RC1 == "O" & RC2 == "O")$log_R11
t.test(head_NP_SS, head_NP_SO) #sig. t = -4.8423, df = 616.73, p-value = 1.625e-06
t.test(head_NP_OS, head_NP_OO) #sig. t = 2.5256, df = 685.27, p-value = 0.01178
#SS >> OO *>> OS >> SO
t.test(head_NP_SS, head_NP_OO) #not sig.
t.test(head_NP_OS, head_NP_SO) #not sig.



