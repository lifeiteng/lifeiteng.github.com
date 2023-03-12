import whisper

model = whisper.load_model("large-v2")


librispeech = { "61-70970-0024": {"text": "They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission.",
                                 "prompt_text": "",
                                 "prompt_audio": "audios/librispeech/61-70970-0024/prompt.wav",
                                 "libritts_audio": "audios/librispeech/61-70970-0024/libritts.wav"},
                "908-157963-0027": {"text": "They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission.",
                                 "prompt_text": "",
                                 "prompt_audio": "audios/librispeech/908-157963-0027/prompt.wav",
                                 "libritts_audio": "audios/librispeech/908-157963-0027/libritts.wav"},
                "1089-134686-0004": {"text": "They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission.",
                                 "prompt_text": "",
                                 "prompt_audio": "audios/librispeech/1089-134686-0004/prompt.wav",
                                 "libritts_audio": "audios/librispeech/1089-134686-0004/libritts.wav"},
                 "1221-135767-0014": {"text": "They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission.",
                                 "prompt_text": "",
                                 "prompt_audio": "audios/librispeech/1221-135767-0014/prompt.wav",
                                 "libritts_audio": "audios/librispeech/1221-135767-0014/libritts.wav"},              
              }

for key in librispeech:
  result = model.transcribe(librispeech[key]["prompt_text"])
  librispeech[key]["prompt_text"] = result["text"]

with open("to_be_syntheised.txt", "w") as f:
  for key, value in librispeech.items():
    # text-prompts audio-prompts text path
    f.write(f"{value["prompt_text"]}\t{value["prompt_audio"]}\t{value["text"]}\t{value["libritts_audio"]}\n")
