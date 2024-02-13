# sem_score_benchmarking

Benchmark for Sem Score that capable of RAG with Eli5 dataset.

## What is Sem Score?

Here is the paper [link](https://arxiv.org/pdf/2401.17072.pdf).

The concept of SemScore is quite simple.
It measures semantic similarity between ground truth and model’s generation using an embedding model.
Really straightforward, right?

## Benchmarking

I used Eli5 dataset for benchmarking at [here](https://huggingface.co/datasets/MarkrAI/eli5_sample_autorag).
I use four models (text-davinci-002, text-babbage-001, gpt-3.5-turbo-0125, mistral-7B) for benchmarking.
And three metrics (BLEU, ROUGE, METEOR) plus sem score.
And I evaluated all models results manually like the paper did.

You can see the config YAML file at [config.yaml](config.yaml).

## Result

|     Model     |  BLEU  | ROUGE  | METEOR | Sem Score |
|:-------------:|:------:|:------:|:------:|:---------:|
| gpt-3.5-turbo | 1.399  | 0.137  | 0.125  |  0.5237   |
|  Mistral-7B   | 1.3980 | 0.1879 | 0.1195 |  0.5096   |
