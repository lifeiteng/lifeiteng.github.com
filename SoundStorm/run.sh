
# ln -s ~/Geek/OpenSource/speech/lifeiteng.github.com/valle/audios

python -c"
import sys

with open(sys.argv[1]) as f:
  for line in f:
    fields = line.strip().split('\t')
    output_file = fields[-1].replace('libritts.wav', 'MLS_Epoch1_soundstorm.wav')
    print(f'python ./bin/client.py --audio-prompt {fields[1]} --text \"{fields[2]}\" --output-dir {output_file}')
" ../valle/libritts.txt



python -c"
import sys
import librosa
import soundfile

with open(sys.argv[1]) as f:
  for line in f:
    fields = line.strip().split('\t')
    prompt_file = fields[1].replace('.wav', '_16K.wav')
    data, sr = librosa.load(fields[1], sr=16000)
    soundfile.write(prompt_file, data, 16000)
    output_file = fields[-1].replace('libritts.wav', 'MLS_Epoch1_soundstorm.wav')
    print(f'python ./bin/client.py --audio-prompt {prompt_file} --text \"{fields[2]}\" --output-dir {output_file}')
" ../valle/libritts.txt


