print("Choices of the subjects are :\n")
choice=raw_input("Enter 1 for quiz or 2 to add questions")
if choice=='1':
	print("1. Maths 2. G K  3.C Programming")
	response= raw_input("Enter a choice for the selection of the subject ")
	if response=='1':
		import mathsquiz
	elif response=='2':
		import gkquiz
	elif response=='3':
		import cquiz 
	else :
		print("You have selected a wrong choice\nPlease try again :)\n")
else :
	import add_questions 
  