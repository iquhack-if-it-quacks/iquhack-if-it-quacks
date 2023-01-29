from sklearn.base import ClassifierMixin


class Wrapper(ClassifierMixin):
    def __init__(self, pipe0, pipe1):
        self.pipe0 = pipe0
        self.pipe1 = pipe1

    def predict(self, X):
        Y0 = self.pipe0.predict(X)
        Y1 = self.pipe1.predict(X)
        res = []
        for y0, y1 in zip(Y0, Y1):
            if y0 and y1:
                res.append(0)  # error
            elif y0:
                res.append(0)
            elif y1:
                res.append(1)
            else:
                res.append(-1)
        return res
