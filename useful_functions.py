print("useful_functions.py", " __name__ is", __name__)
def get_non_empty_string(prompt):
    while True:
        answer = input(prompt)
        if len(answer) > 0 :
            break
    return answer

def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                break
        except:
            print("Error occured")
    return num

def main():
    print("Hello")
# TEst all functions
if __name__ == "__main__":
    main()