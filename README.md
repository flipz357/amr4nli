# AMR4NLI

## Data

All AMR NLI data, (including more than 1,500,000 parses) can be downloaded [here](https://drive.google.com/file/d/1VDptvvA0qbbsfAXk3-I3Ej9LjfaqY7I9/view?usp=sharing).

Note that in [our paper](https://arxiv.org/abs/2306.00936) we only use dev and test sets, however, graphs of the NLI training data are included too.

## Evaluation script and metrics

### AMR Metrics

- [SmatchP](https://github.com/flipz357/smatchpp): use smatch precision to check whether H is entailed by P
- [WWLKP (Wasserstein AMR)](https://github.com/flipz357/weisfeiler-leman-amr-metrics): run with `-k 1` and `-prs p` 
- Node Mover: use Wasserstein AMR with `-k 0`.
- Graph token precision: see toy example below.

### Eval instruction:

1. use a metric to generate a file where each line contains a score, and the line aligns with the AMR parse files. Name the file: `<data>-<metricName`.txt, e.g., `snli_1.0_dev-smatchP.txt`. 
2. run evaluation script.

See the simple example that comes below.

### Full evaluation example:

1. run a metric on all data: `./run-simple-metric.sh` 

2. Evaluate AUC for entailment: `./eval.sh simpleMetricP`

Explanation: in the first step we execute a (toy) graph metric over all the data, for measuring graph overlap precision. It generates predictions in `sim-predictions/`. In the second step we evaluate the predictions against human gold ratings via AUC.

Running your metric: it should be quite simple, you just need to execute it in the same way as shown in `./run-simple-metric.sh`. If your metric provides one score per graph pair on each single line, you're good to go.

### Additional notes:

#### Computing other metrics

- Evaluation of different thresholds: please set evaluate function in the main method of script `evaluatetasks.py` to `acc_of_ones_thres`. You can just uncomment the part
- Evaluation on hard testing instances, please look into `evaluatetasks.py`. Relatively at the bottom there are some lines that you can uncomment to overwrite the snli data with the hard snli data.


