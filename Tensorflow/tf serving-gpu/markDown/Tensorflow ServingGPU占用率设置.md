tensorflow serving服务：

GPU指定占用率：

sudo docker run --runtime=nvidia -p 8501:8501 --mount type=bind,source=/home/tf-serving/model/yolo,target=/models/yolo -e MODEL_NAME=yolo -t tensorflow/serving:latest-gpu --per_process_gpu_memory_fraction=0.1 &

