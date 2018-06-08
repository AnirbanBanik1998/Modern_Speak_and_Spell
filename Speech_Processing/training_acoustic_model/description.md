# Training Acoustic Model

This is particularly important due to the presence of different accents of different people. We can increase the accuracy by considering their own accents by adapting from the existing en-us **Hidden Markov Model**.

Make sure you have Sphixtrain installed in your machine.

## To run the entire training script...type:
```
$./run.sh
```

## Steps

* You have to speak out the letters or words provided each time clearly. This creates the audio files required to make the adapted model.
 
* Now the model will be generated automatically. For decoding with the new updated model...just add an extra argument -hmm en-us-adapt while using any pocketsphinx command.

