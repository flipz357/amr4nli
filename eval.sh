#!/usr/bin/env bash

# set this path to the directory where the data files lie 
# the data can be downloaded from google see README
DATA_PATH=../amr_nli/data_all_amr_nli_final/

metric=$1

python evaluatetasks.py -path_sickdev_prediction_file sim-predictions/sick.dev-$metric.txt \
       			 -path_sicktest_prediction_file sim-predictions/sick.test-$metric.txt \
			 -path_snlidev_prediction_file sim-predictions/snli_1.0_dev-$metric.txt \
			 -path_snlitest_prediction_file sim-predictions/snli_1.0_test-$metric.txt \
			 -path_multinlimatch_prediction_file sim-predictions/multinli_1.0_dev_matched-$metric.txt \
			 -path_multinlimismatch_prediction_file sim-predictions/multinli_1.0_dev_mismatched-$metric.txt \
			 -path_sickdev_original_file $DATA_PATH/sick.dev.txt \
       			 -path_sicktest_original_file $DATA_PATH/sick.test.txt \
			 -path_snlidev_original_file $DATA_PATH/snli_1.0_dev.txt \
			 -path_snlitest_original_file $DATA_PATH/snli_1.0_test.txt \
			 -path_multinlimatch_original_file $DATA_PATH/multinli_1.0_dev_matched.txt \
			 -path_multinlimismatch_original_file $DATA_PATH/multinli_1.0_dev_mismatched.txt
