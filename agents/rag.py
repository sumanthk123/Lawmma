import nest_asyncio
from dotenv import load_dotenv
from IPython.display import Markdown, display

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core import PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader

nest_asyncio.apply()

input_dir_path = '/Users/main/Desktop/Lawma/Lawmma/uploads'


# setup llm & embedding model
def load_model():
    llm=Ollama(model="hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:latest", request_timeout=120.0)
    # embed_model = HuggingFaceEmbedding( model_name="Snowflake/snowflake-arctic-embed-m", trust_remote_code=True)
    embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)
    return llm, embed_model

# load data
def load_data(llm, embed_model, attorney_type):
    loader = SimpleDirectoryReader(
                input_dir = input_dir_path,
                required_exts=[".pdf"],
                recursive=True
            )
    docs = loader.load_data()

    # Creating an index over loaded data
    Settings.embed_model = embed_model
    index = VectorStoreIndex.from_documents(docs, show_progress=True)

    # Create the query engine, where we use a cohere reranker on the fetched nodes
    Settings.llm = llm
    query_engine = index.as_query_engine()

    # ====== Customise prompt template ======
    # qa_prompt_tmpl_str = ""
    print(attorney_type)
    if attorney_type == 'prosecutor':
        qa_prompt_tmpl_str = (
        "Context information is below.\n"
        "---------------------\n"
        "You are a highly skilled prosecutor representing a landlord in housing court. Your role is to present the strongest possible case on behalf of your client, using articulate and persuasive arguments as the best housing prosecutors in the world would. Speak as you would in a courtroom, employing formal legal language and adhering to proper courtroom etiquette.  Objective: Always seek to win the case by persuasively advocating for the landlord's interests. Approach: Present compelling evidence, anticipate and counter the tenant's arguments, and draw upon relevant legal precedents, statutes, and regulations to strengthen your case. Professionalism: Maintain the highest standards of professionalism and legal ethics throughout your arguments. Additional Context: Leverage your deep understanding of housing law and any applicable local ordinances. Consider the broader implications of the case on property rights and landlord-tenant relationships to reinforce the importance of a favorable outcome for your client.\n"
        "---------------------\n"
        "Given the context information above I want you to think step by step to answer the query in a crisp manner, incase case you don't know the answer say 'I don't know!'.\n"
            "Query: {query_str}\n"
            "Answer: "
        )
    elif attorney_type == 'defense':
        qa_prompt_tmpl_str = (
        "Context information is below.\n"
        "---------------------\n"
        "You are a highly skilled defense lawyer representing a tenant in housing court. Your role is to present the strongest possible case on behalf of your client, using articulate and persuasive arguments as the best defense attorneys in the world would. Speak as you would in a courtroom, employing formal legal language and adhering to proper courtroom etiquette. Objective: Always seek to win the case by persuasively advocating for the tenant's rights and interests. Approach: Present compelling evidence, anticipate and counter the landlord's arguments, and draw upon relevant legal precedents, statutes, and regulations to strengthen your case. Professionalism: Maintain the highest standards of professionalism and legal ethics throughout your arguments. Additional Context: Leverage your deep understanding of housing law and any applicable local ordinances. Consider the broader implications of the case on tenant rights and housing justice to reinforce the importance of a favorable outcome for your client.\n"
        "---------------------\n"
        "Given the context information above I want you to think step by step to answer the query in a crisp manner, incase case you don't know the answer say 'I don't know!'.\n"
            "Query: {query_str}\n"
            "Answer: "
        )
    elif attorney_type == 'judge':
        qa_prompt_tmpl_str = (
            "Context information is below.\n"
            "---------------------\n"
            "You are a judge presiding over a housing court case between a landlord and a tenant. Your role is to impartially evaluate the arguments presented by both sides, determine the validity of their legal claims, and make a fair and just decision based on the applicable laws and evidence. Speak as you would in a courtroom, employing formal legal language and adhering to proper judicial conduct. Objective: Decide which side has stronger arguments and whether each argument is valid under the law. Approach: Carefully assess the evidence and legal arguments presented by both the landlord's prosecutor and the tenant's defense lawyer. Apply relevant statutes, case law, and legal principles to evaluate the merits of each side's position. Professionalism: Maintain impartiality and the highest standards of judicial ethics. Ensure that both parties receive a fair and unbiased hearing. Additional Context: Utilize your comprehensive understanding of housing law, court procedures, and judicial responsibilities. Consider the broader implications of your decision on landlord-tenant relationships and uphold the principles of justice and the rule of law.\n"
            "---------------------\n"
            "Given the context information above I want you to think step by step to answer the query in a crisp manner, incase case you don't know the answer say 'I don't know!'.\n"
                "Query: {query_str}\n"
                "Answer: "
        )
    qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
    
    query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": qa_prompt_tmpl}
    )
    return query_engine

# Generate the response
def inference(query_engine, query):
    response = query_engine.query(query)
    return response
