from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch
import warnings

warnings.filterwarnings("ignore")

# Load a pre-trained tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Set the padToken to be the same as eosToken
tokenizer.pad_token = tokenizer.eos_token

# User input
userInput = "Do you like planes?" # Once upon a time,

# 1. Tokenization: Tokenize the input
tokens = tokenizer.tokenize(userInput)

# Remove the 'Ġ' prefix from tokens (this marks the space in the tokenization)
cleanTokens = [token.lstrip('Ġ') for token in tokens]

print("\n------------------------------------------------")
print("Tokenization: The text is split into tokens (without special chars):\n", cleanTokens)

# 2. Token IDs: Convert tokens to token IDs
inputIds = tokenizer.convert_tokens_to_ids(tokens)
print("\n------------------------------------------------")
print("Token IDs: These tokens are mapped to token IDs:\n", inputIds)

# Convert the tokens to input IDs with padding and attention mask
inputs = tokenizer(userInput, return_tensors="pt", padding=True, truncation=True, max_length=1024)
inputIdsTensor = inputs['input_ids']
attentionMask = inputs['attention_mask']  # Ensure the attention mask is passed

print("\n------------------------------------------------")
print("Attention Mask: The attention mask that tells the model which tokens are padding:\n", attentionMask)

# 3. Embeddings: Pass token IDs through the embedding layer
model = AutoModelForCausalLM.from_pretrained("gpt2")
model = model.to(torch.device("cpu"))

# Access the embedding layer
embeddings = model.transformer.wte(inputIdsTensor)
print("\n------------------------------------------------")
print("Embeddings: The model converts the token IDs into embeddings (vector representations):")
print(embeddings)

# 4. Transformer Layers: Passing embeddings through transformer layers (self-attention, etc.)
# Get the hidden states from the transformer
outputs = model.transformer(inputIdsTensor, attention_mask=attentionMask)
lastHiddenStates = outputs.last_hidden_state
print("\n------------------------------------------------")
print("Transformer Layers: The embeddings go through several layers of self-attention and feed-forward networks:")
print(lastHiddenStates)

# 5. Prediction: The model generates the next token ID with custom parameters
output = model.generate(inputIdsTensor,
                        attention_mask=attentionMask,
                        max_length=50,
                        num_return_sequences=1,
                        temperature=0.7,  # Adjust for randomness
                        top_k=50,         # Top-k sampling to limit choices
                        top_p=0.95,       # Nucleus sampling
                        repetition_penalty=0.1,  # Penalize repetition
                        do_sample=True,   # Enable sampling-based generation
                        pad_token_id=model.config.eos_token_id)  # Explicitly set padTokenId

# Print the generated token IDs
predictedTokenIds = output[0][len(inputIdsTensor[0]):]  # Slice the predicted tokens after the input
print("\n------------------------------------------------")
print("Prediction: The model generates the next token ID:\n", predictedTokenIds)

# 6. Decoding: Decode the generated token IDs back to text
generatedText = tokenizer.decode(output[0], skip_special_tokens=True)
print("\n------------------------------------------------\n")
print("Decoding: The generated token ID is decoded back to text, resulting in:\n", generatedText)
print("\n------------------------------------------------\n")
