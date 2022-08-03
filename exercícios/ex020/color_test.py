
# teste de comentários
# teste de comentários
# teste de comentários


[]
{}
()

dc = {'file': 'docx',
      'extension': '.txt'}

a = ["Dauro", "Carol", "Isabel"]
b = ['44', '40', '3']
c = ['amendoa', 'pretos', 'castanhos']

for x, y, z in zip(a, b, c):
    print(f" Nome: {x}\n Idade: {y}\n Olhos: {z}\n")


def main(n):

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            print(f'The number is {i}.')


main(50)

def fibonacci(stop):
    a = 0
    b = 1
    while b < stop:
        print(b, end=' ')
        a, b = b, a + b

n = int(input('Which number do you want the sequence to stop on? '))
fibonacci(n)


class Foo:

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

False, None True as and async assert await break class continue def del elif else
except finally for from global if import in is lambda nonlocal not or pass raise
return try while with yield
