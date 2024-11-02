import nest_asyncio
from dotenv import load_dotenv
from IPython.display import Markdown, display

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core import PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader

nest_asyncio.apply()

input_dir_path = './documents'


# setup llm & embedding model
def load_model():
    llm=Ollama(model="hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:latest", request_timeout=120.0)
    # embed_model = HuggingFaceEmbedding( model_name="Snowflake/snowflake-arctic-embed-m", trust_remote_code=True)
    embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)
    return llm, embed_model

# load data
def load_data(llm, embed_model):
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
    qa_prompt_tmpl_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
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
    return Markdown(str(response))
