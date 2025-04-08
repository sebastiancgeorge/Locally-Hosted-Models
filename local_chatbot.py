from llama_cpp import Llama

llm = Llama(model_path="model.gguf", n_ctx=512)

print("Local AI Chatbot (TinyLLaMA)")
print("Type 'exit' to quit.\n")

chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history.append({"role": "user", "content": user_input})

    prompt = "### Conversation:\n"
    for turn in chat_history:
        role = "User" if turn["role"] == "user" else "AI"
        prompt += f"{role}: {turn['content']}\n"
    prompt += "AI:"

    response = llm(prompt, max_tokens=200, stop=["User:", "AI:"])
    message = response["choices"][0]["text"].strip()
    print("AI:", message)

    chat_history.append({"role": "ai", "content": message})
