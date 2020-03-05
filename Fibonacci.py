class Fibonacci:
    @staticmethod
    def of(n):
        a, b = 0, 1
        for i in range(n + 1):
            a, b = b, a + b
        print(a)


if __name__ == '__main__':
    for i in range(200):
        Fibonacci.of(i)
