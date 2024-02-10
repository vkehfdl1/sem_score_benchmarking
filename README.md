# sem_score_benchmarking
Benchmark for Sem Score that capable of RAG with Eli5 dataset.

## What is Sem Score?

Here is the paper [link](https://arxiv.org/pdf/2401.17072.pdf).

The concept of SemScore is quite simple. 
It measures semantic similarity between ground truth and model’s generation using an embedding model. 
Really straightforward, right?

## Benchmarking

I used Eli5 dataset for benchmarking at [here](https://huggingface.co/datasets/MarkrAI/eli5_sample_autorag).
I use 4 models (gpt-4-turbo, gpt-3.5-turbo, davincii-002, mistral-7B) for benchmarking.
And 3 metrics (BLEU, ROUGE, METEOR) plus sem score.
And I evaluated all models results manually like the paper did.

You can see the config YAML file at [config.yaml](config.yaml).

## Result
Working on it...
