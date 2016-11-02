library(lme4)
library(lmerTest)
wholeENG = read.csv("/Users/chongzhang/Onedrive/Data-Analyses-R-Python-mySQL/csv files/ENG.csv")
summary(wholeENG)
head(wholeENG)
SS = subset(wholeENG, RCtype == "SS")
SS
SO = subset(wholeENG, RCtype == "SO")
OS = subset(wholeENG, RCtype == "OS")
OO = subset(wholeENG, RCtype == "OO")

#ARC_EQUI_INANIM_NP2=subset(xMain, Rctype == "ACTIVE" & Plausibility == "EQUI" & Animacy == "inanimate")$NP2RT
#l20 = lmer(PRE_TAR ~ Plausibility*Rctype*Animacy + (1|Subjects)+(1|Items), xMainDem)

lR3 = lmer (log_R3 ~ RCtype*Matching + (1|Participant)+(1|Item), wholeENG)
lR3

lR34withCorr = lmer (log_R34+log_R78 ~ CORR * RC1 * RC2 + (1|Participant)+(1|Item), wholeENG)
summary(lR34withCorr)

lR34withCorr = lmer (log_R34 ~ CORR * RC1 * RC2 + (1|Participant)+(1|Item), wholeENG)
summary(lR34withCorr)

#V1 in RC1, S vs. O
S_V_in_RC1 = subset(wholeENG, RC1 == "S")$log_R3
O_V_in_RC1 = subset(wholeENG, RC1 == "O")$log_R4
t.test(S_V_in_RC1, O_V_in_RC1) #significant

#V2 in RC2, S vs. O
S_V_in_RC2 = subset(wholeENG, RC2 == "S")$log_R7
O_V_in_RC2 = subset(wholeENG, RC2 == "O")$log_R8
t.test(S_V_in_RC2, O_V_in_RC2) #significant

#V1 in RC1
SS_V_in_RC1 = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R3
SO_V_in_RC1 = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R3
OS_V_in_RC1 = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R4
OO_V_in_RC1 = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R4
t.test(SS_V_in_RC1, SO_V_in_RC1) #not significant
t.test(OS_V_in_RC1, OO_V_in_RC1) #not significant
t.test(SO_V_in_RC1, OS_V_in_RC1) #significant
t.test(SS_V_in_RC1, OS_V_in_RC1) #significant
t.test(SO_V_in_RC1, OO_V_in_RC1) #significant
t.test(SS_V_in_RC1, OO_V_in_RC1) #significant

#V2 in RC2
SS_V_in_RC2 = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R7
SO_V_in_RC2 = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R8
OS_V_in_RC2 = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R7
OO_V_in_RC2 = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R8
t.test(SS_V_in_RC2, SO_V_in_RC2) #significant
t.test(OS_V_in_RC2, OO_V_in_RC2) #not significant
t.test(SO_V_in_RC2, OS_V_in_RC2) #not significant
t.test(SS_V_in_RC2, OS_V_in_RC2) #not significant
t.test(SO_V_in_RC2, OO_V_in_RC2) #not significant

#V2 in RC2 (not logged)
SS_V_in_RC2 = SS$regionExp_response_7.rt
SO_V_in_RC2 = SO$regionExp_response_8.rt
OS_V_in_RC2 = OS$regionExp_response_7.rt
OO_V_in_RC2 = OO$regionExp_response_8.rt
t.test(SS_V_in_RC2, SO_V_in_RC2) #significant
t.test(OS_V_in_RC2, OO_V_in_RC2) #significant
t.test(SO_V_in_RC2, OS_V_in_RC2) #significant
t.test(SS_V_in_RC2, OS_V_in_RC2) #not significant
t.test(SO_V_in_RC2, OO_V_in_RC2) #not significant
t.test(OO_V_in_RC2, SS_V_in_RC2) #significant

#Edge of RC2
SS_edge_RC2 = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R6
SO_edge_RC2 = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R6
OS_edge_RC2 = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R6
OO_edge_RC2 = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R6
t.test(SS_edge_RC2, SO_edge_RC2) #not significant
t.test(OS_edge_RC2, OO_edge_RC2) #not significant
t.test(SO_edge_RC2, OS_edge_RC2) #not significant
t.test(SS_edge_RC2, OO_edge_RC2) #not significant

#main verb
SS_main_verb = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R10
SO_main_verb = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R10
OS_main_verb = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R10
OO_main_verb = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R10
t.test(SS_main_verb, SO_main_verb) #not significant
t.test(SO_main_verb, OS_main_verb) #significant
t.test(OS_main_verb, OO_main_verb) #not significant
t.test(SS_main_verb, OO_main_verb) #not significant
t.test(SS_main_verb, OS_main_verb) #not significant
t.test(SO_main_verb, OO_main_verb) #not significant

#sentence without head NP, AdvP
SS_sentence = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R23467810
SO_sentence = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R23467810
OS_sentence = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R23467810
OO_sentence = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R23467810
t.test(SS_sentence, SO_sentence) #not significant
t.test(OS_sentence, OO_sentence) #not significant
t.test(SS_sentence, OS_sentence) #significant
t.test(SS_sentence, OO_sentence) #significant

#sentence without head NP, AdvP, final main verb.
SS_sentence_noMainV = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R234678
SO_sentence_noMainV = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R234678
OS_sentence_noMainV = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R234678
OO_sentence_noMainV = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R234678
t.test(SS_sentence_noMainV, SO_sentence_noMainV) #not significant
t.test(OS_sentence_noMainV, OO_sentence_noMainV) #not significant
t.test(SS_sentence_noMainV, OS_sentence_noMainV) #significant
t.test(SS_sentence_noMainV, OO_sentence_noMainV) #significant

#RC1, 3 regions
SS_RC1_rt = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_RC1_rt
SO_RC1_rt = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_RC1_rt
OS_RC1_rt = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_RC1_rt
OO_RC1_rt = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_RC1_rt
t.test(SS_RC1_rt, SO_RC1_rt)
t.test(OS_RC1_rt, OO_RC1_rt)
t.test(SO_RC1_rt, OO_RC1_rt)

#RC2, 3 regions
SS_RC2_rt = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_RC2_rt
SO_RC2_rt = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_RC2_rt
OS_RC2_rt = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_RC2_rt
OO_RC2_rt = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_RC2_rt
t.test(SS_RC2_rt, SO_RC2_rt)
t.test(OS_RC2_rt, OO_RC2_rt)

#RC1verb+NP and RC2verb+NP (R3478)
lR3478 = lmer (log_R3478 ~ RCtype*Matching + (1|Participant)+(1|Item), wholeENG)
summary(lR3478)
SS_R3478_rt = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R3478
SO_R3478_rt = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R3478
OS_R3478_rt = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R3478
OO_R3478_rt = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R3478
t.test(SS_R3478_rt, SO_R3478_rt)
t.test(OS_R3478_rt, OO_R3478_rt)
t.test(SS_R3478_rt, OO_R3478_rt)

#RC2, R78 only
lR78 = lmer (log_R78 ~ log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG)
summary(lR78)
SS_R78_rt = subset(wholeENG, RC1 == "S" & RC2 == "S")$log_R78
SO_R78_rt = subset(wholeENG, RC1 == "S" & RC2 == "O")$log_R78
OS_R78_rt = subset(wholeENG, RC1 == "O" & RC2 == "S")$log_R78
OO_R78_rt = subset(wholeENG, RC1 == "O" & RC2 == "O")$log_R78
t.test(SS_R78_rt, SO_R78_rt)
t.test(OS_R78_rt, OO_R78_rt)
t.test(SS_R78_rt, OO_R78_rt)

lR78 = lmer (log_R78 ~ log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG)
summary(lR78)

lR78withoutR34 = lmer (log_R78 ~ RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG)
summary(lR78)

###10/12###
SS_SO = subset(wholeENG, RC1 == "S")
OS_OO = subset(wholeENG, RC1 == "O")
SS_OS = subset(wholeENG, RC2 == "S")
SO_OO = subset(wholeENG, RC2 == "O")
SO_OS = subset(wholeENG, RCtype == "SO" | RCtype == "OS")
SS_OO = subset(wholeENG, RCtype == "SS" | RCtype == "OO")
#SS vs. SO #not sig.
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SS_SO))
#OO vs. OS #sig.
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), OS_OO))
#SS vs. SO #not sig.
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SS_OS))
#OO vs. SO #not sig.
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SO_OO))
#SO vs. OS #not sig.
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SO_OS))
#SS vs. OO #sig.
summary(lmer(log_R78 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SS_OO))
#-----------------------------------------------------------------------------------#
summary(lmer(log_R8 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SO_OO)) #not sig
summary(lmer(log_R7 ~ RCtype + (1+log_R34|Participant)+(1+log_R34|Item), SS_OS)) #sig

#-----------------------------------------------------------------------------------#
#10/12
lR78 = lmer (log_R78 ~ dprimeT * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG)
summary(lR78)
lR78 = lmer (log_R78 ~ dprimeT * log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG)
summary(lR78)
