import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ["OPENAI"])

# Define the function to interact with the OpenAI API
def chat(system, user_assistant, top_prob=0.9):
    # Create system and user messages
    system_msg = [{"role": "system", "content": system}]
    user_assistant_msgs = [
        {"role": "assistant", "content": user_assistant[i]} if i % 2 else {"role": "user", "content": user_assistant[i]}
        for i in range(len(user_assistant))
    ]

    # Combine messages for OpenAI API input
    msgs = system_msg + user_assistant_msgs
    try:
        # Interact with the GPT model
        response = client.chat.completions.create(model="gpt-4", messages=msgs, top_p=top_prob)
        # Return the content of the response
        return response.choices[0].message.content
    except Exception as e:
        print("An exception occurred when communicating with ChatGPT:", e)
        return None

# Agent setup
system_agent1 = "You are Agent 1, an assistant specialized in logical reasoning and answering concisely."
system_agent2 = "You are Agent 2, an assistant specialized in creative problem-solving and detailed explanations."

# Initial messages
message_agent1 = "Hello Agent 2, could you explain a unique approach to solving optimization problems?"
message_agent2 = ""  # Agent 2 will respond to Agent 1

# Simulate conversation
conversation = []
turns = 5  # Set number of turns

for i in range(turns):
    # Agent 1 sends a message to Agent 2
    response_agent2 = chat(system_agent2, [message_agent1], top_prob=0.9)
    if response_agent2:
        conversation.append(("Agent 1", message_agent1))
        conversation.append(("Agent 2", response_agent2))
    else:
        print("Error in generating Agent 2's response.")
        break

    # Agent 2's response becomes Agent 1's next message
    message_agent2 = response_agent2

    # Agent 2 sends a message to Agent 1
    response_agent1 = chat(system_agent1, [message_agent2], top_prob=0.9)
    if response_agent1:
        conversation.append(("Agent 2", message_agent2))
        conversation.append(("Agent 1", response_agent1))
    else:
        print("Error in generating Agent 1's response.")
        break

    # Agent 1's response becomes Agent 2's next message
    message_agent1 = response_agent1

# Output the conversation
for turn, (agent, message) in enumerate(conversation):
    print(f"{agent} (Turn {turn + 1}): {message}")
