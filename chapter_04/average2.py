import random
kor_score = [0,0,0,0,0]
math_score = [0,0,0,0,0]
eng_score = [0,0,0,0,0]

for i in range(5):
    kor_score[i] = random.randint(20,100)
    math_score[i] = random.randint(20,100)
    eng_score[i] = random.randint(20,100)

midterm_score = [kor_score, math_score, eng_score]

student_score = [0,0,0,0,0]
i=0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

a,b,c,d,e=student_score
student_average = [a/3,b/3,c/3,d/3,e/3]
print(student_average)
