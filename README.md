
# Machine Learning AMR Reley Differential Curve

Implementing AMR Reley Differential Curve with Deep Neural Network.

A novel approach to the implementation differential protection scheme by using a <b>Deep Neural Network</b> Dataset has been obtained from Differential Characteristic plane in the <b><a href="https://vebko.org/en/" target="_blank">Vebko</a> AMPro</b> software.

## Features
  - Using <b>Python Tensorflow</b> to build a Deep Neural Network model
  - Converting the <b>Tensorflow</b> model to tflite for running on Embedded Board ARM Architecture
  - Using <b>Golang</b> TFLite to be able to easily run tflite model
  - Running on <a href="https://www.xilinx.com/products/silicon-devices/soc/zynq-7000.html" target="_blank"><b>Xilinx Zynq-7020</b></a> Embedded Board
  - Usable via <b>docker</b> file
  
## Installation

For Linux/MacOs amd64:

```bash
  go build main.go
```

For xilinx Zynq-7020 (ARM-based computers):

```bash
  sudo apt-get install gcc-arm-linux-gnueabihf
  
  CGO_ENABLED=1 GOOS=linux GOARCH=arm CC=arm-linux-gnueabihf-gcc go build -o main
```

## Running

This running for ubuntu/MacOs amd64:

```bash
  ./main
```

This running for xilinx Zynq-7020 (ARM-based computers):

```bash
  export LD_LIBRARY_PATH=./arm
  
  ./main
```

## Running with Docker

First of all, clone and the repo then run
```bash
  docker build -t dnn .
```

After pulling and building the image, You can get the result like this

```bash
  docker run --rm -t amr ./main
```

Or you can go to the container for running it manually like this

```bash
  docker run -it amr
```

## More Info
#### Differential Characteristic in the AMPro software
![Graph](https://github.com/taherfattahi/dnn-amr-reley-differential-curve/blob/master/images/AMR_Relay_Differential_Curve.png)

#### Graph of the Deep Neural Network
![Graph](https://github.com/taherfattahi/dnn-amr-reley-differential-curve/blob/master/images/graph.png)

#### Model Accuracy Plot
![Graph](https://github.com/taherfattahi/dnn-amr-reley-differential-curve/blob/master/images/model_accuracy_plot.png)

#### Model Loss Plot
![Graph](https://github.com/taherfattahi/dnn-amr-reley-differential-curve/blob/master/images/model_loss_plot.png)

Note: If you had issue and got `standard_init_linux.go:211: exec user process caused "exec format error` error, try [this solution](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/).

## Collaborators

- [Nima Akbarzade](https://www.github.com/iw4p) - Dr.Mohammad Parpaei - Sajad Ansari 


## License

[MIT](https://choosealicense.com/licenses/mit/)

