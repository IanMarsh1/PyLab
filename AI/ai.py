from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch
import warnings

#! https://huggingface.co/openai-community/gpt2

warnings.filterwarnings("ignore")

# Load a pre-trained tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Set the padToken to be the same as eosToken
tokenizer.pad_token = tokenizer.eos_token

# User input
userInput = "Hello, how are you?"

# Tokenize the input
tokens = tokenizer.tokenize(userInput)
cleanTokens = [token.lstrip('Ġ') for token in tokens]

print("Tokens:", cleanTokens)

# Convert tokens to inputIds with padding and attentionMask
inputs = tokenizer(userInput, return_tensors="pt", padding=True, truncation=True, max_length=1024)
inputIds = inputs['input_ids']
attentionMask = inputs['attention_mask']

print("Input IDs:", inputIds)
print("Attention Mask:", attentionMask)

# Load a pre-trained language model
model = AutoModelForCausalLM.from_pretrained("gpt2")
model = model.to(torch.device("cpu"))

# Generate a response with temperature and topP to avoid repetition
output = model.generate(inputIds,
                        attention_mask=attentionMask,
                        max_length=50,
                        num_return_sequences=1,
                        temperature=0.7,  # Adjust for randomness
                        top_k=50,         # Top-k sampling to limit choices
                        top_p=0.95,       # Nucleus sampling
                        repetition_penalty=2.0,  # Penalize repetition
                        do_sample=True,   # Enable sampling-based generation
                        pad_token_id=model.config.eos_token_id)  # Explicitly set padTokenId


# Decode the output IDs to text
response = tokenizer.decode(output[0], skip_special_tokens=True)
print("Chatbot Response:", response)

# Example of maintaining context with adjusted generation parameters
conversationHistory = "User: Hello, how are you?\nBot: I'm doing well, thank you! How can I assist you today?\nUser: Tell me about AI?"

# Tokenize and encode the conversation history with padding and attentionMask
inputs = tokenizer(conversationHistory, return_tensors="pt", padding=True, truncation=True, max_length=1024)
inputIds = inputs['input_ids']
attentionMask = inputs['attention_mask']

# Generate a response based on the conversation history with adjusted parameters
output = model.generate(inputIds,
                        attention_mask=attentionMask,
                        max_length=50,
                        num_return_sequences=1,
                        temperature=0.7,  # Adjust for randomness
                        top_k=50,         # Top-k sampling to limit choices
                        top_p=0.95,       # Nucleus sampling
                        repetition_penalty=2.0,  # Penalize repetition
                        do_sample=True,   # Enable sampling-based generation
                        pad_token_id=model.config.eos_token_id)  # Explicitly set padTokenId


# Decode the output IDs to text
response = tokenizer.decode(output[0], skip_special_tokens=True)
print("Chatbot Response with Context:", response)
