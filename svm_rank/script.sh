#!/bin/bash
# ./script model_name c_value data_dir
echo "SVM-Rank Model Training and Classifing"
mkdir Results/$1
./svm_rank_learn -c $2 -e 0.001 -l 1 $3/train.txt Results/$1/model
./svm_rank_classify $3/vali.txt Results/$1/model Results/$1/pred_valid
perl Eval-Score.pl $3/vali.txt Results/$1/pred_valid Results/$1/eval_valid 0
./svm_rank_classify $3/test.txt Results/$1/model Results/$1/pred_test
perl Eval-Score.pl $3/test.txt Results/$1/pred_test Results/$1/eval_test 0

