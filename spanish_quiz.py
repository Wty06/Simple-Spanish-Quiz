print("Welcome to my Spanish quiz!")

playing = input("Would you like to play Tyler's Spanish Quiz? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Get Started!")
score = 0

# Question 1
answer = input("Translate the word 'Casa' to its English counterpart: ")
if answer.lower() == "house":
    print("Correcto!")
    score += 1
else:
    print("Incorrecto")

# Question 2
answer = input("How do you say 'Door' in Spanish? ")
if answer.lower() == "puerta":
    print("Correcto!")
    score += 1
else:
    print("Incorrecto")

# Question 3
answer = input("What is a natural way to say 'how are you' in Spanish? hint there is more than one answer: ")
if answer.lower() in ['que tal', 'cómo estás', 'cómo está usted']:
    print("Correcto!")
    score += 1
else:
    print("Incorrecto")

# Question 4
answer = input("Conjugate the verb 'ser' in the present tense (write all forms separated by commas): ")
if answer.lower() == "soy, eres, es, somos, sois, son":
    print("Correcto!")
    score += 5
else:
    print("Incorrecto")

# Question 5
answer = input("What does the Spanish verb 'ir' translate to in English? ")
if answer.lower() == "to go":
    print("Correcto!")
    score += 1
else:
    print("Incorrecto")

# Question 6
answer = input('How do you say "I go" in Spanish? ')
if answer.lower() == "yo voy":
    print("Correcto!")
    score += 1
else:
    print("Incorrecto")

# Question 7
print('Way to go!')
print('You are almost done')
print('There is only one question left!')
print('This one is for all the marbles!')

answer = input("How do you say 'I go home' in Spanish? ")
if answer.lower() == "yo voy a la casa":
    print("¡Wondísimo!")
    score += 10
else:
    print("Incorrecto!")

# Calculate the percentage score
total_possible_points = 5 + 5 + 10  # Total possible points from all questions
percentage = (score / total_possible_points) * 100

# Display the score
print(f"Your score is: {percentage:.2f}%")
