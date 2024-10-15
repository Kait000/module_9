class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг итерации не может быть равным нулю')
        self.start = self.pointer = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (((self.pointer <= self.stop) and (self.step > 0)) or
                ((self.pointer >= self.stop) and (self.step < 0))):
            res = self.pointer
            self.pointer += self.step
        else:
            raise StopIteration()
        return res


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(exc)
print()

iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()

iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()

iter5 = Iterator(10, 1)
for i in iter5:
    print(i, end=' ')
print()
