DATA_FOLDER_PATH=/home/chli/Dataset/NeRF/3vjia_test

mkdir $DATA_FOLDER_PATH/sparse

./build/install/bin/colmap mapper \
	--database_path $DATA_FOLDER_PATH/1.db \
	--image_path $DATA_FOLDER_PATH/input + \
	--output_path $DATA_FOLDER_PATH/sparse + \
	--Mapper.ba_global_function_tolerance=0.000001
