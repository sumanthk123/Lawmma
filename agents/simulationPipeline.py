import subprocess
from rag import load_model, load_data, inference
from IPython.display import Markdown, display

import os
from pypdf import PdfReader

harvey, harvey_embed = load_model()
litt, litt_embed = load_model()
judge, judge_embed = load_model()

harvey_engine = load_data(harvey, harvey_embed, 'prosecutor')
litt_engine = load_data(litt, litt_embed, 'defense')
judge_engine = load_data(judge, judge_embed, 'judge')



def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        text += page.extract_text()
    return text

upload_dir = '/Users/main/Desktop/Lawma/Lawmma/uploads'
for filename in os.listdir(upload_dir):
    if filename.endswith('.pdf'):
        file_path = os.path.join(upload_dir, filename)
        initial_case = extract_text_from_pdf(file_path)
        # print(f"Text from {filename}:\n{initial_text}\n")

print("initial case finished compiling")

epochs = 5
num_conversations = 5
print("starting conversation")
for conversation in range(num_conversations):
    with open(f"/Users/main/Desktop/Lawma/Lawmma/agents/case1/conversation_{conversation+1}.txt", "w") as pdf:
        for epoch in range(epochs):
            prosecutor_prompt = f"Use your knowledge of the given documents and Illinois State Law to create the best rebuttal claim to the case argument. Your response should only be about one part of the case argument and should not contain any reasoning, only your claim with a brief citation and explanation. Any claim should be restricted to the law of the state of Illinois: {initial_case}"
            prosecutor_response = inference(litt_engine, prosecutor_prompt)
            pdf.write("Litt's Claim: " + '\n')
            pdf.write(str(prosecutor_response))
            pdf.write("\n\n")
            print('prosecutor response finished')
            display(Markdown(str(prosecutor_response)))

            judge_prompt = f"Look through the argument and using prior knowledge, determine if the argument is valid or invalid, and make sure this reasoning is not in your response. If it is invalid, respond with only the word 'invalid'. If it is valid, respond with only the word 'valid': {prosecutor_response}"
            judge_response = inference(judge_engine, judge_prompt)
            display(Markdown(str(judge_response)))
            print('judge response finished')
            if (str(judge_response) == "invalid"):
                break

            harvey_prompt = f"Use your knowledge of the given documents and Illinois State Law to create a strong counterclaim that directly addresses the argument and your response should only be the counterclaim with a brief citation and explanation. Any argument should be restricted to the law of the state of Illinois: {prosecutor_response}"
            harvey_response = inference(harvey_engine, harvey_prompt)
            pdf.write("Harvey's Counterclaim: " + '\n')
            pdf.write(str(harvey_response))
            pdf.write("\n\n")
            print('harvey response finished')
            display(Markdown(str(harvey_response)))
            initial_case = harvey_response
            print('epoch finished', epoch)
print("conversation finished")


