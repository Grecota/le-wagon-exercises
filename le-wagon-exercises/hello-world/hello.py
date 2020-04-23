# pylint: disable=missing-docstring

# Here is what you need to do:
#   1. Write some code below
#   2. Save to disk with Ctrl + S (Windows) or Cmd + S (Mac)
#   3. Run the code

print("Hello World !")

age = 21 #Variable assignment
print (age)

#one year passes
age = (age + 1) #Variable re-assignment
#Shortcut version
age += 1 #Incrementation

print(age)

# ---

first_name = "Grégory"
last_name = "Cohen Tannugi"

#Concatenation
sentence= "Hello, je m'appelle" + first_name + "" + last_name
print(sentence)

#Interpolation
sentence2 = f"Hello, je m'appelle {first name}"
print(sentence2)
