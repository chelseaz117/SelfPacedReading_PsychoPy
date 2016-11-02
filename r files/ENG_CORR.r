library(lme4)
wholeENG_CORR = read.csv("/Users/chongzhang/Desktop/ENG_CORR.csv")
summary(wholeENG_CORR)

lR34 = lmer (log_R34 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeENG_CORR)
summary(lR34)


SS_R78_rt = subset(wholeENG_CORR, RC1 == "S" & RC2 == "S")$log_R78
SO_R78_rt = subset(wholeENG_CORR, RC1 == "S" & RC2 == "O")$log_R78
OS_R78_rt = subset(wholeENG_CORR, RC1 == "O" & RC2 == "S")$log_R78
OO_R78_rt = subset(wholeENG_CORR, RC1 == "O" & RC2 == "O")$log_R78
t.test(SS_R78_rt, SO_R78_rt) #not sig.
t.test(OS_R78_rt, OO_R78_rt) #not sig.

#compare SS+OS and OO+SO in RC2:
lR78 = lmer (log_R78 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeENG_CORR)
summary(lR78)

lR78_onRC1 = lmer (log_R78 ~ log_R34 * RC1 * RC2 + (1+log_R34|Participant)+(1+log_R34|Item), wholeENG_CORR)
summary(lR78_onRC1)

RC2_S = subset(wholeENG_CORR, RC2 == "S")$log_R78
RC2_O = subset(wholeENG_CORR, RC2 == "O")$log_R78
t.test(RC2_S, RC2_O) #not sig.

#RC1+RC2, i.e. R3478
lR3478 = lmer (log_R3478 ~ RC1 * RC2 + (1|Participant)+(1|Item), wholeENG_CORR)
summary(lR3478)
RCs_SS = subset(wholeENG_CORR, RC1 == "S" & RC2 == "S")$log_R3478
RCs_SO = subset(wholeENG_CORR, RC1 == "S" & RC2 == "O")$log_R3478
RCs_OS = subset(wholeENG_CORR, RC1 == "O" & RC2 == "S")$log_R3478
RCs_OO = subset(wholeENG_CORR, RC1 == "O" & RC2 == "O")$log_R3478
t.test(RCs_SS, RCs_SO) #not sig.
t.test(RCs_OS, RCs_OO) #not sig.
t.test(RCs_SS, RCs_OO) #sig t = -2.5894, p-value = 0.009794
