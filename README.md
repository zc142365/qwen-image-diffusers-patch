# qwen-image-diffusers-patch

## En

By using diffusers_search.py, you can locate the current path of the diffusers package in your Python environment.

Then, overwrite pipeline_loading_utils.py and pipeline_utils.py in that location.

After that, you can run example.py to execute the Qwen-Image model with quantized options using two GPUs.

## Ko

현재 python 환경에 있는 diffusers의 경로를
diffusers_search.py로 찾고

pipeline_loading_utils.py와 pipeline_utils.py로 덮어 씌우고

example.py 사용하면 GPU 2개에서 양자화된 옵션으로 qwen-image 실행 가능함
