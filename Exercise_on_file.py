
def main():
    global first_name, last_name, age
    file = open("data.txt","w")
    first_name = input('enter your first name: ')
    last_name = input('Enter your last name: ')
    age = input('Enter your age here: ')
    file.write(first_name)
    file.write("\t")
    file.write(last_name)
    file.write('\t')
    file.write(age)
    file.close()
  
def read_items():
    file1 = open('data.txt', 'r')
    details = file1.readlines()
    
    count = 0
    # Strips the newline character
    for detail in details:
        count += 1
        print(f"{count} Firstname: {first_name}  Lastname: {last_name}  Age: {age}")
  
  
  
if __name__  == '__main__':
    main()
    read_items()