class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        try:
            if self.a < 6:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration
        except StopIteration:
            print("Iteration stopped as it reached stop iteration")
            return "Iteration Stopped"


myNum = MyNumbers()
myNumberIterator = iter(myNum)

print(next(myNumberIterator))
print(next(myNumberIterator))
print(next(myNumberIterator))
print(next(myNumberIterator))
print(next(myNumberIterator))
print(next(myNumberIterator))

