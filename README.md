# Keras-Models-Cutter
A simple function that allows to cut model's layers (es. in Keras pretrained models)

Sometimes we need to cut models from a specific layer to another, or merge models together, or this kind of stuff.

## how to use it

```python

# import a model (in my case, MobileNet)
mobileNet = MobileNet(input_shape=(128, 128, 3), alpha=1.0, include_top=False, weights='imagenet')

# call the function with the desired layers (in my case I want to cut from layer 'conv1_pad' to layer 'conv_pw_4_relu'
output = get_model_layers(mobileNet, _from='conv1_pad', _from_input=originalMobileNet.input, _to="conv_pw_4_relu")   

# create a new model with the desired layers
mobileNet = Model(inputs=originalMobileNet.input, outputs=output)

```
