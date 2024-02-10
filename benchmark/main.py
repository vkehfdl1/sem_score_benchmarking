import os

import click
from autorag.evaluator import Evaluator
from autorag import generator_models
from llama_index.llms import Vllm

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(root_path, 'data')


@click.command()
@click.option('--config', type=click.Path(exists=True))
def main(config):
    generator_models['vllm'] = Vllm
    evaluator = Evaluator(qa_data_path=os.path.join(data_path, 'qa_test.parquet'),
                          corpus_data_path=os.path.join(data_path, 'corpus.parquet'))
    evaluator.start_trial(config)


if __name__ == '__main__':
    main()
