marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))

total_percentage = (100) * (marks1 + marks2 + marks3) / 300

if marks1 >= 33 and marks2 >= 33 and marks3 >= 33:

    if total_percentage >= 40:
        print(f"you passed the exam with percentage : {total_percentage:.2f}")

    else:
        print(
            f"You failed the exam beacuse of total percentage is less than 40% with percentage: {total_percentage:.2f}"
        )

else:
    print(
        f"You failed the exam beacuse you are not able to get 33 marks in one of the three subjects,with percentage: {total_percentage:.2f}"
    )
