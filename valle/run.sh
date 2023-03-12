
# find audios | grep ours | while read line;do
# 	renamed=`echo $line | sed 's/ours/official/g'`
# 	cp $line $renamed
# done

# find audios | grep ours | while read line;do
# 	rm $line
# done

pip install -U openai-whisper
