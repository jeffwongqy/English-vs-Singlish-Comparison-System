import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

st.title("🗣️ English vs Singlish Comparison")
st.write("A platform to compare its Standard English and Singlish characteristics.")

st.info("NOTE: Please enter a sentence written in Singlish.")
user_input = st.text_area("Enter a sentence:", placeholder = "Example: This chicken rice is damn shiok!")

llm = ChatOllama(model = "llama3.2", temperature = 0, num_ctx = 1024)

english_prompt = ChatPromptTemplate.from_template(
    
    """
    You are an English linguistics analyzer.
    
    Analyze the following sentence from the perspective of Standard English. 
    
    Sentence: 
    {sentence}
    
    Provide a concise analysis covering:
    
    1. Grammar Structure
    2. Vocabulary
    3. Sentence meaning 
    4. Whether the sentence is grammatically acceptable
    5. A Standard English version if necessary
    
    Do not discuss Singlish. 
    """
)

singlish_prompt = ChatPromptTemplate.from_template(
    
    """
    You are a Singapore English (Singlish) linguistics analyzer. 
    
    Analyze the following sentence from the perspective of Singlish. 
    
    Sentence:
    {sentence}
    
    Provide a concise analysis covering:
    
    1. Singlish grammatical features
    2. Vocabulary or discourse particles
    3. Sentence Meaning
    4. Possible Singaporean cultural or conversational context
    5. A natural Singlish interpretation or version 
    
    Do not assume every Singaporean uses Singlish.
    Do not stereotype Singaporeans. 
    """ 
)

english_chain = english_prompt | llm | StrOutputParser()
singlish_chain = singlish_prompt | llm | StrOutputParser()

parallel_chain = RunnableParallel(standard_english = english_chain, 
                                  singlish = singlish_chain)


if st.button("Analyze Sentence"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Analyzing..."):
            result = parallel_chain.invoke({"sentence": user_input})
            
            st.subheader("Standard English Analysis")
            st.write(result["standard_english"])
            
            st.subheader("Singlish")
            st.write(result["singlish"])