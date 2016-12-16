sudo apt-get install --no-install-recommends git graphviz python-dev python-flask python-flaskext.wtf python-gevent python-h5py python-numpy python-pil python-pip python-protobuf python-scipy

sudo apt-get install --no-install-recommends build-essential cmake git gfortran libatlas-base-dev libboost-all-dev libgflags-dev libgoogle-glog-dev libhdf5-serial-dev libleveldb-dev liblmdb-dev libopencv-dev libprotobuf-dev libsnappy-dev protobuf-compiler python-all-dev python-dev python-h5py python-matplotlib python-numpy python-opencv python-pil python-pip python-protobuf python-scipy python-skimage python-sklearn

export CAFFE_ROOT=~/digits-multi-detect/caffe
sudo pip install -r $CAFFE_ROOT/python/requirements.txt

cd $CAFFE_ROOT
mkdir build
cd build
cmake ..
make --jobs=4

DIGITS_ROOT=~/digits-multi-detect/digits
sudo pip install -r $DIGITS_ROOT/requirements.txt
sudo pip install -e $DIGITS_ROOT

cd $DIGITS_ROOT
./digits-devserver
