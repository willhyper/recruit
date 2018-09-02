import recruit
from test.task_fib import fib

c = recruit.Contractor(fib)

r = c.send(25)
print(r)


r = c.send(30)
print(r)