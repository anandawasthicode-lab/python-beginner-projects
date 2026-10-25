students={"Aman":[85,90,78],"Riya":[92,88,95],"Zoya":[70,65,80]}
avgmarks={}
while True:
    print("\n===== Student Marks Manager =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Show Topper")
    print("4. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        name=input("Enter student name:")
        if name in students:
            print("Student already exists!")
        else:
            marks=[]
            for i in range(1,4):
                mark=int(input(f"Enter marks for subject {i}:"))
                if 0<=mark<=100:
                    marks.append(mark)
                else:
                    print("Invalid marks! Enter marks between 0 and 100.")
                    break
            if len(marks)==3:
                students[name]=marks
                print("Student added successfully!")
    elif ch==2:
        print("\nName        Average    Grade")
        for name in students:
            avg=sum(students[name])/len(students[name])
            if avg>=85:
                grade="A"
            elif avg>=70:
                grade="B"
            elif avg>=50:
                grade="C"
            else:
                grade="F"
            print(f"{name}        {avg:.2f}      {grade}")
    elif ch==3:
        for name in students:
            avgmarks[name]=sum(students[name])/len(students[name])
        topper=max(avgmarks,key=avgmarks.get)
        print("Topper:",topper)
        print("Average Marks:",f"{avgmarks[topper]:.2f}")
    elif ch==4:
        print("GOOD BYE!")
        break
    else:
        print("Invalid choice! Please select 1 to 4.")
