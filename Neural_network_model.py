class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = "Layer"

    def __call__(self, obj):
        self.next_layer = obj
        return obj


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = "Input"


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = "Dense"


class NetworkIterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        self.current_obj = self.obj
        return self

    def __next__(self):
        if self.current_obj is None:
            raise StopIteration
        res = self.current_obj
        self.current_obj = res.next_layer
        return res


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    print(x.name)
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"