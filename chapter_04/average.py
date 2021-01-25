import random
kor_score = [0,0,0,0,0]
math_score = [0,0,0,0,0]
eng_score = [0,0,0,0,0]

for i in range(5):
    kor_score[i] = random.randint(20,100)
    math_score[i] = random.randint(20,100)
    eng_score[i] = random.randint(20,100)
    print ('{}의 국어성적 : {} 수학성적 : {} 영어성적 : {}'.format(i+1,kor_score[i],math_score[i],eng_score[i]))
    print ('{}의 평균 : '.format(i+1),(kor_score[i]+math_score[i]+eng_score[i])/3)


midterm_score = [kor_score, math_score, eng_score]
