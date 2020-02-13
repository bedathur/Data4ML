for fold in 1 2 3
do
	mkdir MQ2008/Fold$fold/Noisy_Data
	for noise in 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
	do
		mkdir MQ2008/Fold$fold/Noisy_Data/Noise_$noise
		for round in 1 2 3 4 5 6 7 8 9 10
		do
			python3 noisy_data.py MQ2008/Fold$fold/train.txt $noise MQ2008/Fold$fold/Noisy_Data/Noise_$noise/train_$round
		done
	done
done
