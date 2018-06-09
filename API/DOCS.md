# A generalized recorder and decoder script

This script can be used and the functions can be imported and used in almost any game and game_launcher so that if anything has to changed in this script...no change has to be done in the game code.

This is under construction...will be updated as the main decoder script soon.

## Documentation

* `recorder`: Class which contains the inner functions of the recorder script.
* `start()`: Main function which starts the entire process.
* `record(stopped, q)`: Function which records when volume of a chunk is greater than a particular threshold value.
* `listen(stopped, q)`: Function which listens to the audio stream and puts the chunks in a queue to be operated later on.
* `decoder(record, chunk)`: Function to decode using the pocketsphinx batch command.
 
