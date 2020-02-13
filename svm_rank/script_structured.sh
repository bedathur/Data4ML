# mkdir Results/MQ2008_StructuredNoise
# for fold in 1 2 3
# do
# 	mkdir Results/MQ2008_StructuredNoise/Fold$fold
# 	for noise in 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
# 	do
# 		mkdir Results/MQ2008_StructuredNoise/Fold$fold/Noise_$noise
# 		./svm_rank_learn -c 10 -e 0.001 -l 1 ../Datasets/MQ2008/Fold$fold/Structured_Noise/train_$noise Results/MQ2008_StructuredNoise/Fold$fold/Noise_$noise/model
# 		./svm_rank_classify ../Datasets/MQ2008/Fold$fold/test.txt Results/MQ2008_StructuredNoise/Fold$fold/Noise_$noise/model Results/MQ2008_StructuredNoise/Fold$fold/Noise_$noise/pred
# 		perl Eval-Score.pl ../Datasets/MQ2008/Fold$fold/test.txt Results/MQ2008_StructuredNoise/Fold$fold/Noise_$noise/pred Results/MQ2008_StructuredNoise/Fold$fold/Noise_$noise/eval 0
# 	done
# done