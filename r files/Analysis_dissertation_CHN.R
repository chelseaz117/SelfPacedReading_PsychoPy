library(lme4)
wholeCHN = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/CHN.csv")
summary(wholeCHN)
head(wholeCHN)
SS = subset(wholeCHN, RCtype == "SS")
SS
SO = subset(wholeCHN, RCtype == "SO")
OS = subset(wholeCHN, RCtype == "OS")
OO = subset(wholeCHN, RCtype == "OO")

#ARC_EQUI_INANIM_NP2=subset(xMain, Rctype == "ACTIVE" & Plausibility == "EQUI" & Animacy == "inanimate")$NP2RT
#l20 = lmer(PRE_TAR ~ Plausibility*Rctype*Animacy + (1|Subjects)+(1|Items), xMainDem)

lR11 = lmer (log_R11 ~ RCtype*Matching + (1|Participant)+(1|Item), whole)
summary(lR11)

lR34 = lmer (log_R34 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN)
summary(lR34)

lR34withCorr = lmer (log_R34 ~ CORR * RC1 * RC2 + (1|Participant)+(1|Item), wholeCHN)
summary(lR34withCorr)

#Verb in RC1, SS+SO compared with OS+OO
S_V_in_RC1 = subset(wholeCHN, RC1 == "S")$log_R3
O_V_in_RC1 = subset(wholeCHN, RC1 == "O")$log_R4
t.test(S_V_in_RC1, O_V_in_RC1) #not significant
#Verb in RC1, SS compared with OO
SS_V_in_RC1 = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R3
OO_V_in_RC1 = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R4
t.test(SS_V_in_RC1, OO_V_in_RC1) #not significant
#Verb in RC1, SO compared with OS
SO_V_in_RC1 = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3
OS_V_in_RC1 = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R4
t.test(SO_V_in_RC1, OS_V_in_RC1) #not significant
#Verb in RC1, SS compared with OS
SS_V_in_RC1 = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R3
OS_V_in_RC1 = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R4
t.test(SS_V_in_RC1, OS_V_in_RC1) #not significant
#Verb in RC1, SO compared with OO
SO_V_in_RC1 = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3
OO_V_in_RC1 = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R4
t.test(SO_V_in_RC1, OO_V_in_RC1) #not significant

#-------------------------------------------------------------#
#Verb in RC2, SS+OS compared with SO+OO
S_V_in_RC2 = subset(wholeCHN, RC2 == "S")$log_R8
O_V_in_RC2 = subset(wholeCHN, RC2 == "O")$log_R9
t.test(S_V_in_RC2, O_V_in_RC2) #significant
#Verb in RC2, SS compared with OO
SS_V_in_RC2 = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R8
OO_V_in_RC2 = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R9
t.test(SS_V_in_RC2, OO_V_in_RC2) #significant
#Verb in RC2, SO compared with OS
SO_V_in_RC2 = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R9
OS_V_in_RC2 = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R8
t.test(SO_V_in_RC2, OS_V_in_RC2) #significant, but smaller
#Verb in RC2,  OS compared with OO
OS_V_in_RC2 = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R8
OO_V_in_RC2 = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R9
t.test(OS_V_in_RC2, OO_V_in_RC2) #not significant
#Verb in RC2,  SS compared with SO
SS_V_in_RC2 = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R8
SO_V_in_RC2 = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R9
t.test(SS_V_in_RC2, SO_V_in_RC2) #significant
#Verb in RC2,  SO compared with OO
SO_V_in_RC2 = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R9
OO_V_in_RC2 = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R9
t.test(SO_V_in_RC2, OO_V_in_RC2) #significant
#Verb in RC2,  SO compared with OO
SS_V_in_RC2 = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R8
OS_V_in_RC2 = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R8
t.test(SS_V_in_RC2, OS_V_in_RC2)
#------important------
#Verb in RC1: nothing is significant
#Verb in RC2: everything is significant, except for OS vs. OO.
#------important------

#Edge of RC1, S compared with O
S_edge_RC1_PP = subset(wholeCHN, RC1 == "S")$log_R2
O_edge_RC1_PP = subset(wholeCHN, RC1 == "O")$log_R2
t.test(S_edge_RC1_PP, O_edge_RC1_PP) #not significant
#Edge of RC1, S compared with O
S_edge_RC1_noPP = subset(wholeCHN, RC1 == "S")$log_R3
O_edge_RC1_noPP = subset(wholeCHN, RC1 == "O")$log_R3
t.test(S_edge_RC1_noPP, O_edge_RC1_noPP) #significant
#Edge of RC1, SS compared with OS
OO_edge_RC1_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R3
OS_edge_RC1_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R3
t.test(OO_edge_RC1_noPP, OS_edge_RC1_noPP) #significant
#Edge of RC1, SS compared with OO
SS_edge_RC1_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R3
OO_edge_RC1_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R3
t.test(SS_edge_RC1_noPP, OO_edge_RC1_noPP) #significant
#Edge of RC1, SO compared with OS
SO_edge_RC1_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3
OS_edge_RC1_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R3
t.test(SO_edge_RC1_noPP, OS_edge_RC1_noPP) #small significant
#Edge of RC1, SO compared with OO
SO_edge_RC1_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3
OO_edge_RC1_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R3
t.test(SO_edge_RC1_noPP, OO_edge_RC1_noPP) #small significant
#Edge of RC1, SS compared with SO
SS_edge_RC1_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R3
SO_edge_RC1_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3
t.test(SS_edge_RC1_noPP, SO_edge_RC1_noPP) #small significant
#----------------------------------------------------------------------------------------
#Edge of RC2, S compared with O
S_edge_RC2_PP = subset(wholeCHN, RC2 == "S")$log_R7
O_edge_RC2_PP = subset(wholeCHN, RC2 == "O")$log_R7
t.test(S_edge_RC2_PP, O_edge_RC2_PP) #not significant
#Edge of RC2, S compared with O
S_edge_RC2_noPP = subset(wholeCHN, RC2 == "S")$log_R8
O_edge_RC2_noPP = subset(wholeCHN, RC2 == "O")$log_R8
t.test(S_edge_RC2_noPP, O_edge_RC2_noPP) #significant
#Edge of RC2, SS compared with SO
SS_edge_RC2_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R8
SO_edge_RC2_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R8
t.test(SS_edge_RC2_noPP, SO_edge_RC2_noPP)  #significant
#Edge of RC2, SS compared with OO
SS_edge_RC2_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R8
OO_edge_RC2_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R8
t.test(SS_edge_RC2_noPP, OO_edge_RC2_noPP)  #significant
#Edge of RC2, SO compared with OS
SO_edge_RC2_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R8
OS_edge_RC2_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R8
t.test(SO_edge_RC2_noPP, OS_edge_RC2_noPP)  #significant
#Edge of RC2, OS compared with OO
OS_edge_RC2_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R8
OO_edge_RC2_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R8
t.test(OS_edge_RC2_noPP, OO_edge_RC2_noPP)  #significant
#Edge of RC2, SS compared with OS
SS_edge_RC2_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R8
OS_edge_RC2_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R8
t.test(SS_edge_RC2_noPP, OS_edge_RC2_noPP)  #small significant
#Edge of RC2, SO compared with OO
SO_edge_RC2_noPP = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R8
OO_edge_RC2_noPP = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R8
t.test(SO_edge_RC2_noPP, OO_edge_RC2_noPP)  #not significant
#------important------
#Edge of RC1: S is faster than O.
#Edge of RC2: S is faster than O.
#------important------

#head NP
SS_head = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R11
SO_head = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R11
OS_head = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R11
OO_head = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R11
S_head_RC1 = subset(wholeCHN, RC1 == "S")$log_R11
O_head_RC1 = subset(wholeCHN, RC1 == "O")$log_R11
S_head_RC2 = subset(wholeCHN, RC2 == "S")$log_R11
O_head_RC2 = subset(wholeCHN, RC2 == "O")$log_R11
#-------important--------
t.test(SS_head, SO_head) #significant
t.test(SS_head, OS_head) #significant
t.test(SS_head, OO_head) #not significant
t.test(SO_head, OS_head) #not significant
t.test(SO_head, OO_head) #significant
t.test(OS_head, OO_head) #marginally significant
#it looks like parallelism wins 
#-------important--------

#difference in heads when first RC is S or O, regardless of the second RC.
t.test(S_head_RC1, O_head_RC1) #not significant
#difference in heads when second RC is S or O, regardless of the first RC.
t.test(S_head_RC2, O_head_RC2) #not significant
#this makes sense coz we need the combination of two RCs.

#RC1, 3 regions-346
SS_RC1_rt = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_RC1_rt
SO_RC1_rt = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_RC1_rt
OS_RC1_rt = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_RC1_rt
OO_RC1_rt = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_RC1_rt
t.test(SS_RC1_rt, SO_RC1_rt) #not significant
t.test(OS_RC1_rt, OO_RC1_rt) #not significant
t.test(SO_RC1_rt, OS_RC1_rt) #not significant
t.test(SS_RC1_rt, OO_RC1_rt) #significant
t.test(SO_RC1_rt, OO_RC1_rt) #significant
t.test(OS_RC1_rt, SS_RC1_rt) #not significant

#RC2, 3 regions-8910
SS_RC2_rt = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_RC2_rt
SO_RC2_rt = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_RC2_rt
OS_RC2_rt = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_RC2_rt
OO_RC2_rt = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_RC2_rt
t.test(SS_RC2_rt, SO_RC2_rt) #significant
t.test(OS_RC2_rt, OO_RC2_rt) #not significant
t.test(SS_RC2_rt, OO_RC2_rt) #significant
t.test(OO_RC2_rt, SO_RC2_rt) #not significant

#RC1+RC2, 6 regions-3468910
SS_R3468910_rt = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R3468910
SO_R3468910_rt = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3468910
OS_R3468910_rt = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R3468910
OO_R3468910_rt = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R3468910
t.test(SS_R3468910_rt, SO_R3468910_rt) #significant
t.test(OS_R3468910_rt, OO_R3468910_rt) #not significant
t.test(SS_R3468910_rt, OO_R3468910_rt) #not significant
t.test(SO_R3468910_rt, OS_R3468910_rt) #not significant
t.test(SS_R3468910_rt, OS_R3468910_rt) #not significant
t.test(SO_R3468910_rt, OO_R3468910_rt) #not significant

#RC1verb+NP and RC2verb+NP (R3489)
lR3489 = lmer (log_R3489 ~ RCtype*Matching + (1|Participant)+(1|Item), wholeCHN)
summary(lR3489)
SS_R3489_rt = subset(wholeCHN, RC1 == "S" & RC2 == "S")$log_R3489
SO_R3489_rt = subset(wholeCHN, RC1 == "S" & RC2 == "O")$log_R3489
OS_R3489_rt = subset(wholeCHN, RC1 == "O" & RC2 == "S")$log_R3489
OO_R3489_rt = subset(wholeCHN, RC1 == "O" & RC2 == "O")$log_R3489
t.test(SS_R3489_rt, SO_R3489_rt) #not significant
t.test(OS_R3489_rt, OO_R3489_rt) #not significant
t.test(SS_R3489_rt, OO_R3489_rt) #not significant
t.test(OS_R3489_rt, SO_R3489_rt) #not significant
