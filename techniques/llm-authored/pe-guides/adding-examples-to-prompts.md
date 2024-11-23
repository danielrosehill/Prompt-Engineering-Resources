---
title: "Adding Examples To Prompts"
---

![Written By GPT-4 Turbo](https://img.shields.io/badge/Written%20By-GPT--4%20Turbo-5A5A5A?style=for-the-badge&logo=openai&logoColor=white)

## Introduction

Adding examples to prompts is a technique used in prompt engineering to provide a model with context and guide its response. This technique involves providing a few examples of the desired output before asking the model to generate its own. It's a way of 'priming' the model, giving it a clearer idea of what is expected in its responses.

## History

The technique of adding examples to prompts has been in use since the advent of transformer-based language models like GPT-3. It is based on the principle that these models learn from patterns and can replicate the structure and content of provided examples in their responses.

## Use-Cases

Adding examples to prompts can be useful in a variety of scenarios:

1. **Question-Answering Systems**: By providing examples of questions and their corresponding answers, the model can be guided to generate appropriate responses to new questions.
2. **Data Generation**: If you need the model to generate data in a specific format, providing examples can help ensure the output matches the desired structure.
3. **Translation Tasks**: By providing examples of sentences in one language and their translations in another, the model can be guided to translate new sentences accurately.

## Example

Here's an example of how you might use this technique:

Prompt: 
```
Translate the following English sentences to French:
1. "The cat is black." -> "Le chat est noir."
2. "I love to read books." -> "J'aime lire des livres."
3. "She is a good friend." -> ?
```
In this case, the model is provided with two examples of English sentences and their French translations before being asked to translate a new sentence.

## Advantages

1. **Improved Accuracy**: By providing examples, you can guide the model towards the correct type of response, improving the accuracy of its outputs.
2. **Versatility**: This technique can be used for a wide range of tasks, from translation to data generation and beyond.
3. **Ease of Use**: Adding examples to prompts is a straightforward technique that doesn't require advanced knowledge of AI or machine learning.

## Drawbacks

1. **Dependence on Quality of Examples**: The effectiveness of this technique depends on the quality and relevance of the examples provided. Poor examples can lead to inaccurate outputs.
2. **Increased Prompt Length**: Adding examples increases the length of the prompt, which could be a problem for models with a maximum token limit.

## LLMs

This technique works especially well with large language models like GPT-3 and GPT-J. These models have been trained on diverse datasets and can effectively learn from the examples provided in the prompt to generate accurate responses. However, the effectiveness of this technique can vary depending on the specific task and the quality of the examples provided.