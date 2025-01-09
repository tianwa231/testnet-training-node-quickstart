qwen_template = {
    "system_format": "<|im_start|>system\n{content}<|im_end|>\n",
    "user_format": "<|im_start|>user\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "assistant_format": "{content}<|im_end|>\n",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "<|im_start|>tool\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "system": "You are a helpful assistant.",
}

gemma_template = {
    "system_format": "<bos>",
    "user_format": "<start_of_turn>user\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "assistant_format": "{content}<eos>\n",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "<start_of_turn>tool\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "system": None,
}
phi3_template = {
    "system_format": "<bos>",
    "user_format": "<start_of_turn>user\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "assistant_format": "{content}<eos>\n",
    "system": "",
    "tool_format": "<tool>{content}</tool>",  # 添加这行
    "function_format": "<function>{content}</function>",  # 添加这行
    "observation_format": "<observation>{content}</observation>"  # 添加这行
}


    
model2template = {
    "microsoft/Phi-3-mini-4k-instruct":phi3_template,
    "Qwen/Qwen2.5-3B-Instruct":qwen_template,
    "google/gemma-2-9b-it": gemma_template,
    "google/gemma-7b-it": gemma_template,
    "Qwen/Qwen1.5-0.5B": qwen_template,
    "Qwen/Qwen1.5-1.8B": qwen_template,
    "Qwen/Qwen1.5-7B": qwen_template,
    "google/gemma-2b": gemma_template,
    "google/gemma-7b": gemma_template,
}

model2size = {
    "microsoft/Phi-3-mini-4k-instruct":3_800_000_000,
    "Qwen/Qwen2.5-3B-Instruct":3_000_000_000,
    "google/gemma-2-9b-it":9_000_000_000,
    "google/gemma-7b-it":7_000_000_000,
    "Qwen/Qwen1.5-0.5B": 620_000_000,
    "Qwen/Qwen1.5-1.8B": 1_840_000_000,
    "Qwen/Qwen1.5-7B": 7_720_000_000,
    "google/gemma-2b": 2_510_000_000,
    "google/gemma-7b": 8_540_000_000,
}

model2base_model = {
    "microsoft/Phi-3-mini-4k-instruct":"phi3",
    "Qwen/Qwen2.5-3B-Instruct":"qwen",
    "google/gemma-2-9b-it":"gemma",
    "google/gemma-7b-it": "gemma",
    "Qwen/Qwen1.5-0.5B": "qwen1.5",
    "Qwen/Qwen1.5-1.8B": "qwen1.5",
    "Qwen/Qwen1.5-7B": "qwen1.5",
    "google/gemma-2b": "gemma",
    "google/gemma-7b": "gemma",
}
