import random
def test(currentyear):
    currentyear=str(currentyear)
    if len(currentyear) > 2:
        currentyear=currentyear[2:4]
        print(currentyear)
test(2019)