import llama_cpp
import llama_cpp.llama_tokenizer

llama = llama_cpp.Llama.from_pretrained(
    repo_id="Qwen/Qwen1.5-0.5B-Chat-GGUF",
    filename="*q8_0.gguf",
    tokenizer=llama_cpp.llama_tokenizer.LlamaHFTokenizer.from_pretrained(
        "Qwen/Qwen1.5-0.5B"
    ),
    verbose=False,
)

# llm = Llama(
#     model_path="./models/7B/llama-model.gguf",
#     # n_gpu_layers=-1, # Uncomment to use GPU acceleration
#     # seed=1337, # Uncomment to set a specific seed
#     # n_ctx=2048, # Uncomment to increase the context window
# )
# output = llm(
#     "Q: Name the planets in the solar system? A: ",  # Prompt
#     max_tokens=32,  # Generate up to 32 tokens, set to None to generate up to the end of the context window
#     # Stop generating just before the model would generate a new question
#     stop=["Q:", "\n"],
#     echo=True  # Echo the prompt back in the output
# )  # Generate a completion, can also call create_completion
# print(output)
