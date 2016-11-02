library(lme4)
wholeENG_CORR_over60 = read.csv("/Users/chongzhang/Desktop/ENG_CORR_over60.csv")
summary(wholeENG_CORR_over60)

lR34 = lmer (log_R34 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeENG_CORR_over60)
summary(lR34)

SS_R78_rt = subset(wholeENG_CORR_over60, RC1 == "S" & RC2 == "S")$log_R78
SO_R78_rt = subset(wholeENG_CORR_over60, RC1 == "S" & RC2 == "O")$log_R78
OS_R78_rt = subset(wholeENG_CORR_over60, RC1 == "O" & RC2 == "S")$log_R78
OO_R78_rt = subset(wholeENG_CORR_over60, RC1 == "O" & RC2 == "O")$log_R78
t.test(SS_R78_rt, SO_R78_rt) #not sig.
t.test(OS_R78_rt, OO_R78_rt) #marginally sig. t = 1.8803, df = 938.81, p-value = 0.06038

#compare SS+OS and OO+SO in RC2:
lR78 = lmer (log_R78 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeENG_CORR_over60)
summary(lR78)

lR78_onRC1 = lmer (log_R78 ~ log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG_CORR_over60)
summary(lR78_onRC1)

RC2_S = subset(wholeENG_CORR_over60, RC2 == "S")$log_R78
RC2_O = subset(wholeENG_CORR_over60, RC2 == "O")$log_R78
t.test(RC2_S, RC2_O) #sig. 3.161372  3.135274

#RC1+RC2, i.e. R3478
lR3478 = lmer (log_R3478 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeENG_CORR_over60)
summary(lR3478)
RCs_SS = subset(wholeENG_CORR_over60, RC1 == "S" & RC2 == "S")$log_R3478
RCs_SO = subset(wholeENG_CORR_over60, RC1 == "S" & RC2 == "O")$log_R3478
RCs_OS = subset(wholeENG_CORR_over60, RC1 == "O" & RC2 == "S")$log_R3478
RCs_OO = subset(wholeENG_CORR_over60, RC1 == "O" & RC2 == "O")$log_R3478
t.test(RCs_SS, RCs_SO) #not sig.
t.test(RCs_OS, RCs_OO) #not sig.
t.test(RCs_SS, RCs_OO) #sig. t = -3.4497, df = 953.93, p-value = 0.0005857

