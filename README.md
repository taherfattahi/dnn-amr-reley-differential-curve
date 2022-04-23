
# Machine Learning AMR Reley Differential Curve

Implementing AMR Reley Differential Curve with Deep Neural Network


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)



## Installation

For Linux/MacOs amd64:

```bash
  go build main.go
```

For xilinx Zynq-7020 (ARM-based computers):

```bash
  CGO_ENABLED=1 GOOS=linux GOARCH=arm CC=arm-linux-gnueabihf-gcc go build -o main
```

## Running

This running for ubuntu/MacOs amd64:

```bash
    ./main
```

This running for xilinx Zynq-7020 (ARM-based computers):

```bash
  LD_LIBRARY_PATH=~/arm ./main
```
## Collaborators

- Dr.Mohammad Parpaei - Sajad Ansari - [Nima Akbarzade](https://www.github.com/iw4p) 


## License

[MIT](https://choosealicense.com/licenses/mit/)

