import string
import random
import os

# making empty global dictionary
paswd_dict = {}


# adding data to our dictionary from our txt file
with open("paswd.txt", "r") as f:
	data = f.read()
	paswd_dict = eval(data)


def keyval(dict_name, target):
	if(target in dict_name.keys()):
		print(f"Your {target}'s paswd is : {dict_name[target]}\n\n\n")
	else:
		print("There is no such paswd for this target.")

def generate_paswd(length, target):

	# getting all types of characters for making paswd more complex
	s1 = string.punctuation
	s2 = string.ascii_uppercase
	s3 = string.ascii_lowercase
	s5 = string.ascii_letters
	s4 = string.digits

	# using extend function to add all the characters in the s list
	s = []
	s.extend(list(s1))
	s.extend(list(s2))
	s.extend(list(s3))
	s.extend(list(s4))
	s.extend(list(s5))

	# shuffling our complete list
	random.shuffle(s)
		
	required_paswd = "".join(random.sample(s, length))

	# adding the values to the global dictionary
	paswd_dict[target] = required_paswd

	print(f"Here is your paswd: {required_paswd}")

	
	with open("paswd.txt", "w") as f:
		f.write(f"{paswd_dict}")


	print("Successfully saved the paswd !")


def get_paswd(target):
	
	if(target in paswd_dict):
		keyval(paswd_dict, target)
	else:
		print("There is no such paswd for this target.")


def main():
	while(1):

		choice = int(input("1. Create paswd\t\t2. Get paswd\n"))

		if(choice==1):
			length = int(input("Enter the paswd length: \n"))

			if(length<8):
				print("Paswd length should be atleast of 8 characters !")

			else:
				target = input("where you are using this paswd? \n")
				generate_paswd(length, target)

		if(choice==2):
			target = input("Enter the target name \n")
			get_paswd(target)

		if(choice==0):
			break

if __name__ == '__main__':
	main()