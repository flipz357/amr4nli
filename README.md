# AMR4NLI

## Data

All AMR NLI data, (including more than 1,500,000 parses) can be downloaded [here](https://drive.google.com/file/d/1VDptvvA0qbbsfAXk3-I3Ej9LjfaqY7I9/view?usp=sharing).

Note that in the paper we only use dev and test sets, however, graphs of the NLI training data are included too.

## Evaluation script and metrics

### AMR Metrics

- [SmatchP](https://github.com/flipz357/smatchpp): use smatch precision to check whether H is entailed by P
- [WWLKP (Wasserstein AMR)](https://github.com/flipz357/weisfeiler-leman-amr-metrics): run with `-k 1` and `-prs p` 
- Node Mover: use Wasserstein AMR with `-k 0`.

### Eval instruction:

1. use a metric to generate a file where each line contains a score, and the line aligns with the AMR parse files. Name the file: `<data>-<metricName`.txt, e.g., `snli_1.0_dev-smatchP.txt`. 
2. run evaluation script: coming.

### Full evaluation example:

coming
