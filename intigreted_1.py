name = input('what yo name cuh ')

top = '_' * 30
wallBlank = '|' + ' ' * 28+ '|'
wallName = '|' + ' ' * int((28 - len(name)/2))+ name + '|'
bot = '-' * 30

print(top)
print(wallBlank)
print(wallName)
print(wallBlank)
print(bot)