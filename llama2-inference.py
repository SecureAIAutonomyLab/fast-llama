from vllm import LLM, SamplingParams
from time import perf_counter
from dotenv import load_dotenv
import os

# Load environment variables
# load_dotenv()
# huggingface_token = os.environ.get('HUGGINGFACE_TOKEN')

# Define sampling parameters
sampling_params = SamplingParams(
    temperature=0.6, 
    top_p=0.9, 
    max_tokens=4096,
    use_beam_search=False,
    n=1,
)

# Initialize the model
llm = LLM(
    model='../Llama-2-13b-chat-hf',
    tokenizer='../Llama-2-13b-chat-hf',
    dtype='auto',
    tensor_parallel_size=8,
)

print("Chat with Llama2. Type 'exit' to end the session.")
while True:
    # Get input from user
    user_input = input("You: ")
    
    # Exit the loop if user types 'exit'
    if user_input.lower() == 'exit':
        break
    
    # Record start time
    start = perf_counter()
    
    # Generate response
    outputs = llm.generate([user_input], sampling_params)
    
    # Calculate inference time
    time = perf_counter() - start
    
    # Retrieve the generated text
    generated_text = outputs[0].outputs[0].text

    # Print inference time and response
    print(f"Inference time: {time:.3f} seconds")
    print(f"Llama2: {generated_text}")

