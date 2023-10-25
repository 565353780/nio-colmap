mkdir build
cd build

cmake .. \
	-DCMAKE_CUDA_ARCHITECTURES=86 \
	-DCMAKE_INSTALL_PREFIX=./install \
	-G Ninja \
	-DCMAKE_BUILD_TYPE=Debug

ninja
ninja install
