import pickle


class Mutltiply(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        return number * self.multiplier


muliply = Mutltiply(5)
print(muliply.multiply(10))

f = open("multiply_object.pickle", "wb")
pickle.dump(muliply, f)
f.close()


f = open("multiply_object.pickle", "rb")
multiply_pickle = pickle.load(f)
print(multiply_pickle.multiply(5))
