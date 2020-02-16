mkdir Results
mkdir Results/MQ2008
for fold in 1 2 3
do
	mkdir Results/MQ2008/Fold$fold
	mkdir Results/MQ2008/Fold$fold/Noisy_Data
	for noise in 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
	do
		mkdir Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise
		for round in 1 2 3 4 5 6 7 8 9 10
		do
			mkdir Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round
			python3 noisy_data.py ../Datasets/MQ2008/Fold$fold/train.txt $noise Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/train Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/labels
			python3 graphical_model.py Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/train Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/correc_prob
			python3 evaluate.py Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/correc_prob Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/labels Results/MQ2008/Fold$fold/Noisy_Data/Noise_$noise/Round_$round/result
		done
	done
done
