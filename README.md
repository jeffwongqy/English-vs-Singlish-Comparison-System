# English vs Singlish Comparison System

<img width="1000" height="500" alt="images" src="https://github.com/user-attachments/assets/1e3dad5a-104d-4dec-b751-8cab77172726" />


## 1. Introduction
Singapore is a multilingual society where English is widely used alongside languages such as Mandarin, Malay, Tamil, and various Chinese dialects. Within this environment, Singapore English (Singlish) has developed distinctive vocabulary, grammatical patterns, discourse particles, and sentence structures. Examples include expressions such as “Can lah,” “You eat already or not?” and “Why you never tell me?”

This project develops an LLM-based English vs Singlish Comparison System using **LangChain - RunnableParallel** and **Ollama**. The system accepts a Singlish sentence as input and processes it through two independent linguistic analysis branches. One branch analyzes the sentence from a Standard English perspective, while the other analyzes its Singlish characteristics.

The use of **RunnableParallel** allows both analysis chains to process the same input independently. This demonstrates how LangChain can be applied to linguistic analysis by separating different analytical perspectives into parallel processing pipelines.

## 2. Aim 
The aim of this project is to develop an LLM-based linguistic comparison system that analyzes Singlish sentences from both Standard English and Singlish perspectives using LangChain RunnableParallel and Ollama.

## 3. Objectives
The objectives of this project are to:

1. Develop a Singlish input interface that allows users to enter Singapore English sentences.
2. Analyze Singlish sentences from a Standard English perspective, including grammatical structure, vocabulary, sentence meaning, and possible Standard English equivalents.
3. Analyze Singlish linguistic features, including grammar, vocabulary, discourse particles, sentence-final expressions, and conversational usage.
4. Implement LangChain RunnableParallel to process Standard English and Singlish analyses simultaneously.
5. Use Ollama as the local Large Language Model (LLM) to perform the linguistic analyses without relying on a cloud-based LLM API.
6. Compare the two linguistic analyses to highlight differences between Standard English and Singlish.
7. Develop a simple Streamlit interface that presents the analysis results in a clear and user-friendly format.
8. Demonstrate the application of LLMs to computational linguistics, particularly in the analysis of grammatical and pragmatic differences between English varieties.

## 4. Langchain Runnables Parallel

```python
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
```

### 4.1 User Input
Allows users to enter a Singlish sentence for analysis.

```python
st.info("NOTE: Please enter a sentence written in Singlish.")
user_input = st.text_area("Enter a sentence:", placeholder = "Example: This chicken rice is damn shiok!")
```

### 4.2 Ollama LLM
Configures the local llama3.2 model to perform the linguistic analysis and correction tasks.

```python
llm = ChatOllama(model = "llama3.2", temperature = 0, num_ctx = 1024)
```

### 4.3 English Prompt
Defines instructions for analyzing the input from a Standard English perspective.

```python
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
```

### 4.4. Singlish Prompt
Defines instructions for analyzing grammatical, lexical, and conversational features from a Singlish perspective.

```python
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

```

### 4.5 Langchain Chains
Connects each prompt to the LLM and StrOutputParser to convert the model response into readable text.

```python
english_chain = english_prompt | llm | StrOutputParser()
singlish_chain = singlish_prompt | llm | StrOutputParser()
```

### 4.6 RunnableParallel
Combines both analysis pipelines so the same sentence is processed by both perspectives.

```python
parallel_chain = RunnableParallel(standard_english = english_chain, 
                                  singlish = singlish_chain)
```

### 4.7 Validation 
Checks whether the user has entered a sentence before executing the pipeline.

### 4.8 Pipeline Execution 
Invokes the complete RunnableSequence and processes the submitted sentence through all three stages.

### 4.9 Output Display
Presents the standard English analysis and Singlish analysis in the Streamlit interface.

```python
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
```

## 5. Testing for Common Singlish 
1. "Don't worry, relax lah." — Don't worry, stay calm.
2. "Eh, I chope this table already hor!" — Hey, I have already reserved this table with a tissue packet!
3. "You makan already or not?" — Have you eaten your meal yet?
4. "Aiyoh, why you so blur like sotong one?" — Oh no, why are you so confused and clueless?
5. "This chicken rice is damn shiok!" — This chicken rice is extremely delicious!
6. "So sian, nothing to do at home today." — I feel so bored and fed up because there is nothing to do today.
7. "Don't chiong so fast, take it easy." — Do not rush so fast.

## 6. Demo Working Implementation

