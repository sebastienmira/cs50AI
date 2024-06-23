# cs50AI

## 1st attempt 
(as in handwriting) I tried:

1 2D convolutional layer with 32 filters

1 max pooling layer with a pool size of 2x2

1 flattening layer

1 dense hidden layer with 128 neurons

1 dropout layer with rate (0.5)

accuracy: 0.05


## 2nd attempt:

Added one extra convolutional - pooling layer.

### accuracy: 0.85

## 3rd attempt:

changed number of filters to 64

takes a bit long

### accuracy:0.97

## 4rd attempt
changed pooling size to 3x3

considerably quicker but worse accuracy

### accuracy 0.93

## 5th attempt 

2 2D convolutional layer with 64 filters

2 max pooling layer with a pool size of 2x2

1 flattening layer

2 dense hidden layer with 64 neurons

1 dropout layer with rate 0.5

takes longer and accuracy is pretty bad

### accuracy: 0.05

## 6th attempt 

Same as 4th attempt with droput of 0.25

### accuracy: 0.96


Changing the dropout certainly changes the accuracy of the model drastically but it can result in overfitting, hence II gave priority to other parameters first to not be fall in this problem. The increase to two layers of convolution and pooling saw an extreme improvement. This was enhanced by increasing the number of filters.

Increasing the number of hidden layers made the situation considerably worse

Model 3 was the best attempt with accuracy (96 pm 1)%