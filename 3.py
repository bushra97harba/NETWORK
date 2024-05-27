import json
questions = { }
scores = 0
number=1
f = open("questions.txt",'r')
questions = json.load(f)
f.close()
print("python quiz programm")
print("Enter t for True or f for False")
name = input("Enter your full name: ")
for ques in questions.keys():
    print("Question",number,": ", ques)
    ans = input("The answer is ")
    if ans.upper() == questions[ques].upper():
        scores = scores + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1
result={name:scores}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()
