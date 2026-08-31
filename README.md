# English vs Singlish Comparison System

<img width="1000" height="500" alt="images" src="https://github.com/user-attachments/assets/1e3dad5a-104d-4dec-b751-8cab77172726" />


## 1. Introduction
Singapore is a multilingual society where English is widely used alongside languages such as Mandarin, Malay, Tamil, and various Chinese dialects. Within this environment, Singapore English (Singlish) has developed distinctive vocabulary, grammatical patterns, discourse particles, and sentence structures. Examples include expressions such as “Can lah,” “You eat already or not?” and “Why you never tell me?”

This project develops an LLM-based English vs Singlish Comparison System using **LangChain - RunnableParallel** and **Ollama**. The system accepts a Singlish sentence as input and processes it through two independent linguistic analysis branches. One branch analyzes the sentence from a Standard English perspective, while the other analyzes its Singlish characteristics.

The use of **RunnableParallel** allows both analysis chains to process the same input independently. This demonstrates how LangChain can be applied to linguistic analysis by separating different analytical perspectives into parallel processing pipelines.
