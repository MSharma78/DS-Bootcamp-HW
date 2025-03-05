# Question 1 
n_terms = 10
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b

# Question 2 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Numbers at odd indices:")
for i in range(1, len(numbers), 2):  
    print(numbers[i], end=" ")

# Question 3
import string

text = """I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!"""

text = text.translate(str.maketrans("", "", string.punctuation)).lower()

words = text.split()

unique_words = set(words)

print("Number of different words:", len(unique_words))

# Question 4
def count_vowels(word):
    vowels = "aeiouAEIOU" 
    count = sum(1 for char in word if char in vowels) 
    return count

word = "Hello"
print("Number of vowels in", word, ":", count_vowels(word))

# Question 5
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

# Question 6
for num in range(1, 21):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Question 7
def sum_of_integers(a, b):
    return a + b


num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

print("Sum:", sum_of_integers(num1, num2))
