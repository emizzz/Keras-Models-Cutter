# Keras-Models-Cutter
A simple function that allows to cut model's layers (es. in Keras pretrained models)

Sometimes we need to cut models from a specific layer to another, or merge models together, or this kind of stuff.

## how to use it

```python

#import the needed modules
from keras.applications.mobilenet import MobileNet
from keras import Model

# import a model (in my case, MobileNet)
mobilenet = MobileNet(input_shape=(128, 128, 3), alpha=1.0, include_top=False, weights='imagenet')

# call the function with the desired layers (in my case I want to cut from layer 'conv1_pad' to layer 'conv_pw_4_relu'
output = get_model_layers(mobilenet, _from='conv1', _from_input=mobilenet.input, _to='conv_pw_4_relu')   

# create a new model with the desired layers
cutted_mobilenet = Model(inputs=mobilenet.input, outputs=output)

cutted_mobilenet.summary()


_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_5 (InputLayer)         (None, 128, 128, 3)       0         
_________________________________________________________________
conv1 (Conv2D)               multiple                  864       
_________________________________________________________________
conv1_bn (BatchNormalization multiple                  128       
_________________________________________________________________
conv1_relu (ReLU)            multiple                  0         
_________________________________________________________________
conv_dw_1 (DepthwiseConv2D)  multiple                  288       
_________________________________________________________________
conv_dw_1_bn (BatchNormaliza multiple                  128       
_________________________________________________________________
conv_dw_1_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_pw_1 (Conv2D)           multiple                  2048      
_________________________________________________________________
conv_pw_1_bn (BatchNormaliza multiple                  256       
_________________________________________________________________
conv_pw_1_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_pad_2 (ZeroPadding2D)   multiple                  0         
_________________________________________________________________
conv_dw_2 (DepthwiseConv2D)  multiple                  576       
_________________________________________________________________
conv_dw_2_bn (BatchNormaliza multiple                  256       
_________________________________________________________________
conv_dw_2_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_pw_2 (Conv2D)           multiple                  8192      
_________________________________________________________________
conv_pw_2_bn (BatchNormaliza multiple                  512       
_________________________________________________________________
conv_pw_2_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_dw_3 (DepthwiseConv2D)  multiple                  1152      
_________________________________________________________________
conv_dw_3_bn (BatchNormaliza multiple                  512       
_________________________________________________________________
conv_dw_3_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_pw_3 (Conv2D)           multiple                  16384     
_________________________________________________________________
conv_pw_3_bn (BatchNormaliza multiple                  512       
_________________________________________________________________
conv_pw_3_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_pad_4 (ZeroPadding2D)   multiple                  0         
_________________________________________________________________
conv_dw_4 (DepthwiseConv2D)  multiple                  1152      
_________________________________________________________________
conv_dw_4_bn (BatchNormaliza multiple                  512       
_________________________________________________________________
conv_dw_4_relu (ReLU)        multiple                  0         
_________________________________________________________________
conv_pw_4 (Conv2D)           multiple                  32768     
_________________________________________________________________
conv_pw_4_bn (BatchNormaliza multiple                  1024      
_________________________________________________________________
conv_pw_4_relu (ReLU)        multiple                  0         
=================================================================
Total params: 67,264
Trainable params: 65,344
Non-trainable params: 1,920
_________________________________________________________________


```
