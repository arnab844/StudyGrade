import pandas as pd
import matplotlib.pyplot as plt
import csv
student_data_file = "E:\\student.csv"
choice = input("Enter 1 to log in or 2 to sign up: ")
if choice == '2':
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    student_name = input("Enter Your Name: ")
    math_grade = input("Enter Math Grade: ")
    science_grade = input("Enter Science Grade: ")
    english_grade = input("Enter English Grade: ")
    with open(student_data_file, 'a', newline='') as student_data:
        writer = csv.writer(student_data)
        writer.writerow([new_username, new_password, student_name, math_grade, science_grade, english_grade])
    print("Sign up successful! Please log in with your new credentials.")
else:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open(student_data_file, 'r') as student_data:
        reader = csv.reader(student_data)
        header = next(reader)  # Skip header row
        user_data = None
        for row in reader:
            if row[0] == username and row[1] == password:
                user_data = row[2:]
                break    
    if user_data is not None:
        columns = ['student_name', 'math_grade', 'science_grade', 'english_grade']
        df = pd.DataFrame([user_data], columns=columns)
        df[['math_grade', 'science_grade', 'english_grade']] = df[['math_grade', 'science_grade', 'english_grade']].apply(pd.to_numeric)
        df['average_grade'] = df[['math_grade', 'english_grade', 'science_grade']].mean(axis=1)
        df.plot(kind='bar', x='student_name', y='average_grade', title='Average Grades by Student')
        goal = float(input("What grade do you want to achieve? "))
        plt.axhline(y=goal, color='r', linestyle='--', label='Goal')
        plt.legend()
        plt.show()
        student_data = pd.read_csv(student_data_file)
        student_data['average_grade'] = student_data[['math_grade', 'english_grade', 'science_grade']].mean(axis=1)
        class_average = student_data['average_grade'].mean()
        
        print(f"Class average is: {class_average}.")
        if class_average >= goal:
            print(f"Congratulations, you achieved your goal of getting a {goal} average grade!")
        else:
            print(f"Sorry, you did not achieve your goal of getting a {goal} average grade. Keep working hard!")
    else:
     print("Invalid username or password. Please try again.")