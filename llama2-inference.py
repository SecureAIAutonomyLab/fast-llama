from vllm import LLM, SamplingParams
from time import perf_counter
from dotenv import load_dotenv
import os

load_dotenv()
huggingface_token = os.environ.get('HUGGINGFACE_TOKEN')

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
    "What are you capable of?",
    "Can you write an essay on WW2 for me?",
    "Can you solve this equation with steps:\n"
    "10x^2 - 5x = 10",
]

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=256)

llm = LLM(model="../Llama-2-13b-chat-hf", token=huggingface_token)

start = perf_counter()

outputs = llm.generate(prompts, sampling_params)

time = perf_counter() - start

print(f'Inference time: {time:.3f}')

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


