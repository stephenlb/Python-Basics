## Arrays

eat = ["apple","orange","carrot","kiwi","banana","kale",True]
dont_eat = ["cat", "dog", "poptarts", "UPF", "Red40"]
combined = eat + dont_eat
combined.__delitem__(combined.index("Red40"))
print(f"{combined=}")

eat.insert(0, "rice")
print(f"{eat=}")
eat.remove(True)
print(f"{eat=}")

#print(f"{dont_eat=}")
#print(f"{combined=}")


## Array Slices
eat_today = eat[0:2]
eat_tomorrow = eat[2:4]
#kprint(f"{eat_today=}")
#print(f"{eat_tomorrow=}")




## eat the last day
eat_last_day = eat[-2:]
eat_last_day.append(eat[-3])
#print(f"{eat_last_day=}")


## ignore this strangeness, just neat
#animals = [[[dont_eat]*3]*3]
#print(animals)
