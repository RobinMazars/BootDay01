class Evaluator(object):
    """docstring for Evaluator."""

    def __init__(self, arg):
        self.arg = arg

    def zip_evaluate(coef, word):
        if (isinstance(coef, list) and isinstance(word, list)
           and len(coef) == len(word)):
            z = zip(word, coef)
            f = []
            for x in z:
                if isinstance(x[0], str) and isinstance(x[1], float):
                    f.append(len(x[0])*x[1])
                else:
                    return -1
            return sum(f)
        else:
            return -1

    def enumerate_evaluate(coef, word):
        if (isinstance(coef, list) and isinstance(word, list)
           and len(coef) == len(word)):
            f = []
            for c, value in enumerate(word):
                for c2, value2 in enumerate(coef):
                    if (isinstance(value, str)
                       and isinstance(value2, float)):
                        if c == c2:
                            f.append(len(value) * value2)
                    else:
                        return -1
            return sum(f)
        else:
            return -1


# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# print(Evaluator.zip_evaluate(coefs, words))
# print(Evaluator.enumerate_evaluate(coefs, words))
