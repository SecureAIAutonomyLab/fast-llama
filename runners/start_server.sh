#!/bin/bash


python -m vllm.entrypoints.openai.api_server \
    --model ../../Llama-2-13b-chat-hf \
    --host 127.0.0.1 \
    --port 8080