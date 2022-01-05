# How to Install Mediapipe in Jetson Nano 2GB, 4GB, Jetson Xavier NX


Here, I Will show how to install MediaPipe in jetson nano and run an example program to make sure that it is working
The normal way to install mediapipe in Linux is not working 
So I have found a way to install mediapipe from source code, This way of installing is a little bit hard but it works very well in the jetsons.

So let us start this Tutorial 


In this tutorial, I am using a newly flashed JetPack OS on my jetson nano 

Step 1 - First setup the jetson nano then update it using - sudo apt update

Now the system is updated and ready to install mediapipe

Step 2 -  Prerequisites and Dependencies - https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html#prereqs

Now we need to install the Prerequisites and Dependencies for mediapipe and Tensorflow

1. Install system packages required by TensorFlow: - 

   sudo apt-get update

   sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran

2. Install and upgrade pip3:

   sudo apt-get install python3-pip

   sudo pip3 install -U pip testresources setuptools==49.6.0

3.Install the Python package dependencies:

   sudo pip3 install -U --no-deps numpy==1.19.4 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig

   sudo env H5PY_SETUP_REQUIRES=0 pip3 install -U h5py==3.1.0

Step 3 - Now we need to install opencv-python :

   sudo apt-get install python3-opencv 

Now all the Prerequisites and Dependencies are installed 

Now let’s get the mediapipe source code - 

   cd

   git clone https://github.com/google/mediapipe.git

   cd mediapipe


sudo apt-get install -y \
    libopencv-core-dev \
    libopencv-highgui-dev \
    libopencv-calib3d-dev \
    libopencv-features2d-dev \
    libopencv-imgproc-dev \
    libopencv-video-dev

For OpenCV 4 you need to modify opencv_linux.BUILD taking into account current architecture
Go to this page - https://google.github.io/mediapipe/getting_started/install.html#installing-on-debian-and-ubuntu

