# Julia Misiura
# Student Results System Project

import useful_functions
from useful_functions import get_positive_int


def main():
    load_data()
    name_list, exam1_list, exam2_list = load_data()
    show_menu(name_list, exam1_list, exam2_list)

def load_data():
    english_file = open("English.txt")
    name_list = []
    exam1_list = []
    exam2_list = []
    for line in english_file:
        line = line.rstrip()
        info = line.split(",")
        name_list.append(info[0])
        exam1_list.append(int(info[1]))
        exam2_list.append(int(info[2]))

    english_file.close()
    return name_list, exam1_list, exam2_list

def show_menu(name_list, exam1_list, exam2_list):
    print("MENU: ")
    while True:
        print("1. Show Results of Each Exam\n2. Missing Students\n3. Top Marks\n4. -\n5. -\n6. Exit")
        choice = get_positive_int("Enter choice:")
        print()
        if choice == 1:
            show_results(name_list, exam1_list, exam2_list)
            print()

        elif choice == 2:
            missing_students(name_list, exam1_list, exam2_list)
            print()

        elif choice == 3:
            top_marks(name_list, exam1_list, exam2_list)
            print()

        #elif choice == 4:

        #elif choice == 5:

        elif choice == 6:
            save_data(name_list, exam1_list, exam2_list)
            break

def save_data(name_list, exam1_list, exam2_list):
    english_file = open("English.txt", "w")
    for name, exam1, exam2 in zip(name_list, exam1_list, exam2_list):
        print(f"{name},{exam1},{exam2}", file=english_file)
    english_file.close()

def show_results(name_list, exam1_list, exam2_list):
    print("Exam 1:")
    print("----------------------")
    for name, exam1 in zip(name_list, exam1_list):
        if exam1 > -1:
            print(f"{name:20}{exam1}")
    print()

    print("Exam 2:")
    print("----------------------")
    for name, exam2 in zip(name_list, exam2_list):
        if exam2 > -1:
            print(f"{name:20}{exam2}")
    print()

def missing_students(name_list, exam1_list, exam2_list):
    missing_exam1 = 0
    missing_exam2 = 0
    for name, exam1, exam2 in zip(name_list, exam1_list, exam2_list):
        if exam1 == -1:
            missing_exam1 += 1

        if exam2 == -1:
            missing_exam2 += 1

    print(f"Exam 1: ({missing_exam1} missing)")
    print("-----------------")
    for name, exam1 in zip(name_list, exam1_list):
        if exam1 == -1:
            print(name)
    print()

    print(f"Exam 2: ({missing_exam2} missing)")
    print("-----------------")
    for name, exam2 in zip(name_list, exam2_list):
        if exam2 == -1:
            print(name)

def top_marks(name_list, exam1_list, exam2_list):
    print("Exam 1:")
    top_exam1 = 0
    top_exam1_name = ""
    for name, exam1 in zip(name_list, exam1_list):
        if exam1 > top_exam1:
            top_exam1 = exam1
            top_exam1_name = name

    print(f"Highest mark was {top_exam1}")
    print(top_exam1_name)
    print()

    print("Exam 2:")
    top_exam2 = 0
    top_exam2_name = ""
    for name, exam2 in zip(name_list, exam2_list):
        if exam2 > top_exam2:
            top_exam2 = exam2
            top_exam2_name = name

    print(f"Highest mark was {top_exam2}")
    print(top_exam2_name)
    print()

main()