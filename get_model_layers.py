'''
params:
model: the original model that you want to cut
_from: the layer's name (from where to start the cut) 
_from_input: the "from layer's" input
_to: the layer's name (from where to finish the cut) 
'''

def get_model_layers(model, _from, _from_input, _to):
    layers = [(i, layer.name, layer) for i, layer in enumerate(model.layers)]
    from_index = [layer[0] for layer in layers if layer[1] == _from][0]
    to_index = [layer[0] for layer in layers if layer[1] == _to][0]

    out = _from_input
    for l in range(from_index, to_index+1):
        out = layers[l][2](out)

    return out
