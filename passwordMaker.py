import random
words = input("Enter 5 random words separated by spaces: ").split()
while True:
    selected_words = random.sample(words, 3)
    num_pair = random.sample(range(10), 2)
    special_char = random.choice(['!', '@', '#', '$', '%', '&'])
    combined = random.sample(selected_words + [str(num_pair[0]) + special_char + str(num_pair[1])], 4)
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''.join([c.upper() if c.lower() in vowels else c for c in ''.join(combined)])
    print(result)
    again = input("Would you like to generate a new random set? (y/n) ")
    if again.lower() != 'y':
        break
