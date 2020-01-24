from random import shuffle

def student_names(request):
    students = ["Alex", "Roma",'Ira','Bohdan','Serhiy', "Andrii"]
    shuffle(students)
    return{"students": students}