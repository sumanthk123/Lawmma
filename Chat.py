import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ["OPENAI"])

# Define the function to interact with the OpenAI API
def chat(system, user_assistant, topic, top_prob=0.9):
    # Create system and user messages with the topic included
    system_msg = [{"role": "system", "content": f"{system} Topic: {topic}"}]
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
system_judge = "You are the Judge, an expert in legal matters and fair decision-making."
system_landlord = "You are the Landlord, knowledgeable about property management and tenant laws."
system_tenant = "You are the Tenant, well-versed in tenant rights and responsibilities."

# Initial messages
message_judge = "Court is now in session. Landlord, please state your case."
message_landlord = ""  # Landlord will respond to the Judge
message_tenant = ""  # Tenant will respond to the Landlord

# Simulate conversation
conversation = []
turns = 5  # Set number of turns
topic = "tenant eviction"  # Input your specific topic here

for i in range(turns):
    # Judge sends a message to Landlord
    response_landlord = chat(system_landlord, [message_judge], topic, top_prob=0.9)
    if response_landlord:
        conversation.append(("Judge", message_judge))
        conversation.append(("Landlord", response_landlord))
    else:
        print("Error in generating Landlord's response.")
        break

    # Landlord's response becomes Tenant's next message
    message_landlord = response_landlord

    # Landlord sends a message to Tenant
    response_tenant = chat(system_tenant, [message_landlord], topic, top_prob=0.9)
    if response_tenant:
        conversation.append(("Landlord", message_landlord))
        conversation.append(("Tenant", response_tenant))
    else:
        print("Error in generating Tenant's response.")
        break

    # Tenant's response becomes Judge's next message
    message_tenant = response_tenant

    # Tenant sends a message to Judge
    response_judge = chat(system_judge, [message_tenant], topic, top_prob=0.9)
    if response_judge:
        conversation.append(("Tenant", message_tenant))
        conversation.append(("Judge", response_judge))
    else:
        print("Error in generating Judge's response.")
        break

    # Judge's response becomes Landlord's next message
    message_judge = response_judge

# Output the conversation
for turn, (agent, message) in enumerate(conversation):
    print(f"{agent} (Turn {turn + 1}): {message}")
