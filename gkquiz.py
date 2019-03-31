import sys
import difflib
import numpy as np

rankMiddle, rankLow, rankHigh=0,0,0
total=[]
score=[]
prev='1'
print("Welcom to the GK quiz! ")
uname=raw_input("Please enter your name ")
globalCount=int(raw_input("Enter the number of questions you want to take quiz for ? "))
dir="gkquestionset"
#loop over all the number of questions 
for x in xrange(1,globalCount+1):    
    
    #medium level question 
    val=0
    if (prev=='1' and globalCount<10):
                #print("\nmid choice")
                with open(dir+"/quiz2.txt") as fileOne:
                    for i, line in enumerate(fileOne):
                        if(i>=rankMiddle and rankMiddle%2==0):
                            question=line
                            rankMiddle=rankMiddle+1
                            break
                print("Question No "+str(x) + " - > " + question)
                ans=raw_input("Answer -> ")
                #print("your entered answer is ",ans)

                with open(dir+"/quiz2.txt") as fileOne:
                    for i, line in enumerate(fileOne):
                        if(i>=rankMiddle and rankMiddle%2==1):
                            Answer=line
                            rankMiddle=rankMiddle+1
                            break
                #print("Right Answer is ", Answer)

                q = difflib.SequenceMatcher(None, ans, Answer)
                if round(q.ratio(), 1) >= 0.70:
                    val=40
                    prev='2'
                    #print("Toward high level")
                else :
                    prev='0' 
                    val=-7
                    #print("Toward low level")
                total.append(40)
                score.append(val)
                #print("Now score is ",score)

    #easy level question 
    elif (prev=='0' and globalCount<10):
                #print("\nlow choice")
                with open(dir+"/quiz1.txt") as fileOne:
                    for j, line in enumerate(fileOne):
                        if(j>=rankLow and rankLow%2==0):
                            question=line
                            rankLow=rankLow+1
                            break
                print("Question No "+str(x) + " - > " + question)
                ans=raw_input("Answer -> ")
                #print("your entered answer is ",ans)

                with open(dir+"/quiz1.txt") as fileOne:
                    for j, line in enumerate(fileOne):
                        if(j>=rankLow and rankLow%2==1):
                            Answer=line
                            rankLow=rankLow+1
                            break

                #print("Right Answer is ", Answer)

                q = difflib.SequenceMatcher(None, ans, Answer)
                if round(q.ratio(), 1) >= 0.70:
                    val =30
                    prev='1'
                    #print("Toward mid level")

                else :
                    prev='0' 
                    val=-5
                    #print("Toward low level")
                total.append(30)
                score.append(val)
                #print("Now score is ",score)


    #high level question 
    elif (prev=='2' and globalCount<10):
                #print("\nhigh choice")
                with open(dir+"/quiz3.txt") as fileOne:
                    for k, line in enumerate(fileOne):
                        if(k>=rankHigh and rankHigh%2==0):
                            question=line
                            rankHigh=rankHigh+1
                            break
                print("Question No "+str(x) + " - > " + question)
                ans=raw_input("Answer -> ")
                #print("your entered answer is ",ans)

                with open(dir+"/quiz3.txt") as fileOne:
                    for k, line in enumerate(fileOne):
                        if(k>=rankHigh and rankHigh%2==1):
                            Answer=line
                            rankHigh=rankHigh+1
                            break
                #print("Right Answer is ", Answer)

                q = difflib.SequenceMatcher(None, ans, Answer)
                if round(q.ratio(), 1) >= 0.70:
                    val=50
                    prev='2'
                    #print("Toward high level")

                else :
                    prev='1'
                    val=-10
                    #print("Toward mid level")
                total.append(50)
                score.append(val)
                #print("Now score is ",score)

print("")
print("")
print("")
obtainedMarks=np.sum(score)
totalMarks=np.sum(total)

f = open("results.txt", "w")
f.write("Name of the user "+uname +"\n\n"+
        "Score stats "+str(score)+"\nTotal marks stats "+str(total)+"\n\n"+
        "Your obtained marks are "+str(np.sum(score)) +"\n"+
        "Total marks are "+str(np.sum(total)) + "\n\n"+
        "Coongrats! You have achieved "+ str((obtainedMarks*100)/totalMarks) +"% marks"
    )
f.close()
print("")
if(obtainedMarks<totalMarks):
    print("Hey! Do you know you could have scored "+str(40+(globalCount-1)*50)+" marks in this exam")
else :
    print("Badhai ho! You scored the maximum marks possible")
print("")

print("Your results are saved in results.txt file\n")
print("")
print("Have a look at your stats\n")
f = open("results.txt", "r")
print(f.read())
f.close()

