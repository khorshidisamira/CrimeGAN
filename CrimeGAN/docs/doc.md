### How to run?

```bash 
#usage:
python main.py -g <GAN type> 
  -g <GAN type>  
    specify the GAN type in the experiment
    <GAN type> = seqgan | maligan | rankgan | leakgan 
dataset used in this code is crime narratives named naratives_rwords.txt under data directory
```

#### Where to find the experiment results.

The results will be saved as `experiment-XXgan.csv`, a comma-separated values file, with first column be the training epoch,
 the others be the scores of metrics at each epoch.
 
The log will also be printed on the console. 
