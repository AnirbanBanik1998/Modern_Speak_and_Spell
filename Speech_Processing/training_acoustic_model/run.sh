
# Generating acoustic feature files.

sphinx_fe -argfile en-us/feat.params -samprate 16000 -c test.fileids -di . -do . -ei wav -eo mfc -mswav yes

# Copying required programs
 cp -a /usr/local/libexec/sphinxtrain/bw .
 cp -a /usr/local/libexec/sphinxtrain/map_adapt .
 cp -a /usr/local/libexec/sphinxtrain/mk_s2sendump .

# Accumulating observation counts

./bw -hmmdir en-us -moddeffn en-us/mdef.txt -ts2cbfn .ptm. -feat 1s_c_d_dd -svspec 0-12/13-25/26-38 -cmn current -agc none -dictfn cmudict-en-us.dict -ctlfn test.fileids -lsnfn test.transcription -accumdir .

# Updating the acoustic model

./map_adapt -moddeffn en-us/mdef -ts2cbfn .ptm. -meanfn en-us/means -varfn en-us/variances -mixwfn en-us/mixture_weights -tmatfn en-us/transition_matrices -accumdir . -mapmeanfn en-us-adapt/variances -mapmixwfn en-us-adapt/mixture_weights -maptmatfn en-us-adapt/transition_matrices

# Recreating the adapted sendump file

./mk_s2sendump -pocketsphinx yes -moddeffn en-us-adapt/mdef -mixwfn en-us-adapt/mixture_weights -sendumpfn en-us-adapt/sendump

