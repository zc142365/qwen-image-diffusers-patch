# import diffusers
# import os
# print(os.path.join(diffusers.__file__[:-11], 'pipelines', 'pipeline_loading_utils.py'))

from diffusers import DiffusionPipeline
from diffusers import BitsAndBytesConfig as DiffusersBitsAndBytesConfig
from diffusers.quantizers import PipelineQuantizationConfig
from transformers import BitsAndBytesConfig as TransformersBitsAndBytesConfig

import torch, gc

# 양자화 설정 구성
quantization_config = PipelineQuantizationConfig(
    quant_mapping={
        "text_encoder": TransformersBitsAndBytesConfig(
            load_in_4bit=True, 
            load_in_8bit=False,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            llm_int8_enable_fp32_cpu_offload=False
        ),
        "transformer": DiffusersBitsAndBytesConfig(
            load_in_4bit=False,
            load_in_8bit=True,
            # load_in_4bit=True,
            # bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            llm_int8_enable_fp32_cpu_offload=False
        )
    }
)

pipe = DiffusionPipeline.from_pretrained(

"Qwen/Qwen-Image",

torch_dtype=torch.bfloat16,

device_map="balanced",
quantization_config=quantization_config,
gpu_only=True,

)

pipe.enable_attention_slicing()

pipe.enable_vae_tiling()

prompt = (

"Ultra HD, 4K, cinematic composition, 超清，4K，电影级构图, human, one people, person"

)

negative_prompt = (

""

)

img = pipe(

prompt=prompt,

negative_prompt=negative_prompt,

width=1472, height=832,

num_inference_steps=32,

true_cfg_scale=3.0,

generator=torch.Generator("cuda").manual_seed(8899)

).images[0]

img.save("qwen_cyberpunk_market.png")

del pipe; gc.collect(); torch.cuda.empty_cache()