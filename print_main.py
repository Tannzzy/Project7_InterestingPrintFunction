alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
output = ''
user_input = list(input("type in anything (no special characters, numbers and must be lowercase): "))

for num in range((len(user_input))):
    if user_input[num] == " ":
        output += " "

    for letter in alphabet:
        print(output + letter)
        if letter == user_input[num]:
            output += letter
            break
