import random
# x = random.random()*100
# x = random.uniform(5,10)
# x= random.randint(4,10)

# x = ['gaya','samini','rosi','bikki']
# # win = random.choice(x)
# win = random.choices(x,k=2)
# print(win)

numbers = list(range(1,10))
random.shuffle(numbers)
print(numbers)