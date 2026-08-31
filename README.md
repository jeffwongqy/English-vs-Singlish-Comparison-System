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

## 5. Testing for Common Singlish 
1. "Don't worry, relax lah." — Don't worry, stay calm.
2. "Eh, I chope this table already hor!" — Hey, I have already reserved this table with a tissue packet!
3. "You makan already or not?" — Have you eaten your meal yet?
4. "Aiyoh, why you so blur like sotong one?" — Oh no, why are you so confused and clueless?
5. "This chicken rice is damn shiok!" — This chicken rice is extremely delicious!
6. "So sian, nothing to do at home today." — I feel so bored and fed up because there is nothing to do today.
7. "Don't chiong so fast, take it easy." — Do not rush so fast.

## 6. Demo Working Implementation

