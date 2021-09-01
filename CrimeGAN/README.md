## Requirement
We suggest you run the platform under Python 3.6+ with following libs:
* **TensorFlow >= 1.5.0**
* Numpy 1.12.1
* Scipy 0.19.0
* NLTK 3.2.3
* CUDA 7.5+ (Suggested for GPU speed up, not compulsory)    

Or just type `pip install -r requirements.txt` in your terminal.

## Implemented Models and Original Papers

* **SeqGAN** -  [SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient](https://arxiv.org/abs/1609.05473)

* **MaliGAN** - [Maximum-Likelihood Augmented Discrete Generative Adversarial Networks](https://arxiv.org/abs/1702.07983)

* **RankGAN** - [Adversarial ranking for language generation](http://papers.nips.cc/paper/6908-adversarial-ranking-for-language-generation)

* **LeakGAN** - [Long Text Generation via Adversarial Training with Leaked Information](https://arxiv.org/abs/1709.08624)

## Running instruction
```
# run with SeqGAN 
python3 main.py  -g seqgan 
# run with MaliGAN 
python3 main.py  -g maligan 
#Run with RankGAN
python3 main.py  -g rankgan 
#Run with LeakGAN
python3 main.py  -g leakgan 
```
