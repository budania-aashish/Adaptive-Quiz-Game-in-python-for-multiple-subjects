def add_question(filename):
    question = raw_input('Type your question\n')
    write_to_file(question,filename)

def add_answer(filename):
    answer = raw_input('Type your answer\n')
    write_to_file(answer,filename)

def write_to_file(input,filename):
    with open(filename, 'a') as f:
        f.write('\n'+input)
        print("Wrote in ",filename)
check = True 

while check == True:
    subjectname=raw_input("Enter your choice of subject, maths as M, GK as G and C as C\n")
    if subjectname=="M":
        dir="mathsquestionset/"
        level=raw_input("Enter level, Easy - 1, Medium - 2 , High - 3")
    elif subjectname=="G":
        dir="gkquestionset/"
        level=raw_input("Enter level, Easy - 1, Medium - 2 , High - 3")
    elif subjectname=="C":
        dir="cquestionset/"
        level=raw_input("Enter level, Easy - 1, Medium - 2 , High - 3")
    else :
        print("Invalid selection")

    add_question(dir+"quiz"+level+".txt")
    add_answer(dir+"quiz"+level+".txt")

    if  raw_input('Do you want to add another question?') == 'yes':
        check = True
    else:
        check = False

#end of file 
