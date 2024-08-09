import os


def response(user_query):

    # Load environment and get your openAI api key
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)


    template = """You are a helpful assistant.

    {context}

    Question: {question}

    Helpful Answer:"""

    # Add the context to your user query
    custom_rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        custom_rag_prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain.invoke(user_query) 

