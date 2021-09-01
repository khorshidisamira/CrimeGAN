## Evaluation

### Metrics

#### NLL-test loss

It is the average negative log-likelihood of real test data from the generator. It can only be applied to autoregressive generative models like RNNs.

#### BLEU score

BLEU is a widely used metric evaluating the word similarity between two sentences or documents.

Please refer to [BLEU: a method for automatic evaluation of machine translation](https://dl.acm.org/citation.cfm?id=1073135)

Also refer to its python [nltk implementation with smooth function](http://www.nltk.org/_modules/nltk/translate/bleu_score.html). 
We use smooth function _method1_.

#### EmbSim

Inspired by BLEU, a new metric named EmbSim evaluating the similarity between two documents. Instead of comparing sentences words by words, we compare the word embedding.

First, word embedding is evaluated on real data using a skip-gram model.

### Experiment

* epoch 1-80: pretrain process

* epoch 81-181: adversarial training process