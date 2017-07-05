#### Herleitung: SVM Abstand


![](https://latex.codecogs.com/gif.latex?\begin{aligned}&space;H_1:&space;\vec{w}^T\vec{x}&plus;b&space;=&space;1&space;\end{aligned}) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| ![](https://latex.codecogs.com/gif.latex?z_o) einsetzen

![](https://latex.codecogs.com/gif.latex?\begin{aligned}&space;\vec{w}^T\vec{z}_0&plus;b&space;=&space;1&space;\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}&space;\vec{w}^T(\vec{x}_0&plus;\vec{k})&plus;b&space;=&space;1&space;\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}\vec{w}^T(\vec{x}_0&plus;m\frac{\vec{w}}{\|\vec{w}\|})&plus;b=1\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}\vec{w}^T\vec{x}_0&plus;m\frac{\vec{w}\cdot\vec{w}}{\|\vec{w}\|}&plus;b=1\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}\vec{w}^T\vec{x}_0&plus;m\frac{\|\vec{w}\|^2}{\|\vec{w}\|}&plus;b=1\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}\vec{w}^T\vec{x}_0&plus;m\|\vec{w}\|&plus;b=1\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}\vec{w}^T\vec{x}_0&plus;b=1-m\|\vec{w}\|\end{aligned}) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| ![](https://latex.codecogs.com/gif.latex?\vec{w}^T\vec{x}_0&plus;b) entspricht  ![](https://latex.codecogs.com/gif.latex?H_0=-1)

![](https://latex.codecogs.com/gif.latex?\begin{aligned}-1=1-m\|\vec{w}\|\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}m\|\vec{w}\|=2\end{aligned})

![](https://latex.codecogs.com/gif.latex?\begin{aligned}m=\frac{2}{\|\vec{w}\|}\end{aligned})

___
Author: Daniel Beneker
