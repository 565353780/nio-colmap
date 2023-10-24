cd ../niocm
git reset --hard

cd ../nio-colmap
python replace.py

cd ../niocm/build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=86 -DCMAKE_INSTALL_PREFIX=./install -G Ninja
ninja
ninja install
