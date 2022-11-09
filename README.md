# GUI based Deep Learning Platform for Compute Vision 

A gui based low code deep learning platform for compute vision, which is implemented by [paddlepaddle](https://github.com/PaddlePaddle/Paddle) and [flask](https://flask.palletsprojects.com/).

Paddlepaddle is a popular open-sourced deep learning framework which has similar encoding style like pytorch. Based on paddlepaddle, many great algorithm suites have been developed, such as [paddleclas](https://github.com/PaddlePaddle/PaddleClas) for image classification, [paddleseg](https://github.com/PaddlePaddle/PaddleSeg) for image segmentation, [paddledetection](https://github.com/PaddlePaddle/PaddleDetection) for object detection, etc. In order to facilitate developing compute vision products for non-specialists, this project will build a pure gui deep learning platform of compute vision. Users can use this platform to complete usual deep learning steps even whthout any professional knowledge, such as data annotation, training, validation and deployment.

Considering that all suite algorithms of paddlepaddle are implemented by python, we will adopt falsk, which is a purely efficient python web framework, as the backend for restful-api development. 


## 1. [Prepare Environment](./doc/PrepareEnvironment.md)

## 2. [Build Framework](./doc/2.md)

## 3. [Develop Classification Module](./doc/3.md)

## 4. [Develop Segmentation Module](./doc/4.md)

## 5. [Develop Object Detection Module](./doc/5.md)

## 6. [Develop Lable Module](./doc/6.md)

## 7. [Develop Product Module](./doc/7.md)