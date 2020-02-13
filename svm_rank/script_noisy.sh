# mkdir Results
# mkdir Results/MQ2008
# for fold in 1 2 3
# do
# 	mkdir Results/MQ2008/Fold$fold
# 	for noise in 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
# 	do
# 		mkdir Results/MQ2008/Fold$fold/Noise_$noise
# 		for round in 1 2 3 4 5 6 7 8 9 10
# 		do
# 			mkdir Results/MQ2008/Fold$fold/Noise_$noise/train_$round
# 			./svm_rank_learn -c 10 -e 0.001 -l 1 ../Datasets/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/train_$round Results/MQ2008/Fold$fold/Noise_$noise/train_$round/model
# 			./svm_rank_classify ../Datasets/MQ2008/Fold$fold/test.txt Results/MQ2008/Fold$fold/Noise_$noise/train_$round/model Results/MQ2008/Fold$fold/Noise_$noise/train_$round/pred
# 			perl Eval-Score.pl ../Datasets/MQ2008/Fold$fold/test.txt Results/MQ2008/Fold$fold/Noise_$noise/train_$round/pred Results/MQ2008/Fold$fold/Noise_$noise/train_$round/eval 0
# 		done
# 	done
# done