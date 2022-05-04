
# Machine Learning AMR Reley Differential Curve

Implementing Deep Neural Network Binary Classification Algorithm for AMR Reley Differential Curve.

A novel approach to the implementation differential protection scheme by using a <b>Deep Neural Network</b> Dataset has been obtained from Differential Characteristic plane in the <b><a href="https://vebko.org/en/" target="_blank">Vebko</a> AMPro</b> software.

## Features
  - Using <b>Python Tensorflow</b> to build a Deep Neural Network model
  - Converting the <b>Tensorflow</b> model to tflite for running on Embedded Board ARM Architecture
  - Using <b>Golang</b> TFLite to be able to easily run tflite model
  - Running on <a href="https://www.xilinx.com/products/silicon-devices/soc/zynq-7000.html" target="_blank"><b>Xilinx Zynq-7020</b></a> Embedded Board
  - Usable via <b>Docker</b> file
  
## Installation


#### First you need install TensorFlow for C

1) Install bazel
```bash
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install bazel
sudo apt install openjdk-11-jdk
```

2) Build tensorflowlite c lib from source
```bash
cd ~/workspace
git clone https://github.com/tensorflow/tensorflow.git && cd tensorflow
./configure
bazel build --config opt --config monolithic --define tflite_with_xnnpack=false //tensorflow/lite:libtensorflowlite.so
bazel build --config opt --config monolithic --define tflite_with_xnnpack=false //tensorflow/lite/c:libtensorflowlite_c.so

# Check status
file bazel-bin/tensorflow/lite/c/libtensorflowlite_c.so
# ELF 64-bit LSB shared object, x86-64
```

3) Build go-tflite
```bash
export CGO_LDFLAGS=-L$HOME/workspace/tensorflow/bazel-bin/tensorflow/lite/c
export CGO_CFLAGS=-I$HOME/workspace/tensorflow/
```

## Build

For Linux/MacOs amd64:

```bash
  export CGO_LDFLAGS=-L$HOME/workspace/tensorflow/bazel-bin/tensorflow/lite/c

  go build main.go
```

For xilinx Zynq-7020 (ARM-based computers):

```bash
  sudo apt-get install gcc-arm-linux-gnueabihf
  
  export CGO_LDFLAGS=-L$HOME/workspace/tensorflow/bazel-bin/tensorflow/lite/c
  
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

## Note:
 If you had issue and got `standard_init_linux.go:211: exec user process caused "exec format error` error, try [this solution](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/).

## Collaborators

- [Nima Akbarzade](https://www.github.com/iw4p) - Dr.Mohammad Parpaei - [Dr.Mohammad Haji Seyed Javadi](https://www.github.com/EHUser) - Sajad Ansari 


## License

[MIT](https://choosealicense.com/licenses/mit/)

