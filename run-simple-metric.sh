#!/usr/bin/env bash

# set this path to the directory where the data files lie 
# the data can be downloaded from google see README
DATA_PATH=../amr_nli/data_all_amr_nli_final/ 

for dat in sick.test sick.dev multinli_1.0_dev_mismatched multinli_1.0_dev_matched snli_1.0_dev snli_1.0_test 
do
    python simple_metric.py $DATA_PATH/$dat.txt.amrhypothesis $DATA_PATH/$dat.txt.amrpremise > sim-predictions/$dat-simpleMetricP.txt 
done

