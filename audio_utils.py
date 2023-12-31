from pytube import YouTube

from os import path
from pydub import AudioSegment
import os
from pathlib import Path

# files                                                                         
src = "transcript.mp3"
dst = "test.wav"

def convert_mp3_to_wav(src, dst):

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")




def Download(link, video_save_directory, only_audio=False):
    youtubeObject = YouTube(link)

    if only_audio:
        video_stream = youtubeObject.streams.filter(only_audio = only_audio).first()
    else:

        video_stream = youtubeObject.streams.get_highest_resolution()
    try:
        video_stream.download(video_save_directory)
    except:
        print("Failed to Download Video")

    print("Download is completed successfully")

    return video_stream



if __name__ == "__main__":

    # src_path = '../audio_data/Famous_Figures/Test/Donald Trump/Eleven Labs/'

    src_path = os.path.dirname(os.getcwd()) +  '/audio_data/Famous_Figures/Test/'

    speaker_name = 'Elon_Musk'
    DF_type = 'ElevenLabs'

    mp3_fpaths = list(Path(src_path, speaker_name, DF_type).glob("**/*.mp3"))

    print(mp3_fpaths)

    # all_files = os.listdir(src_path)

    # print(all_files)

    # mp3_files = []

    for file in mp3_fpaths:
        
        # if file.endswith('.mp3'):
            # mp3_files.append(file)

        filename = file.as_posix().split('.')[0]

        print(filename)

        # in_file = src_path + file
        # out_file = Path(src_path, speaker_name, DF_type) + filename + '.wav'
        convert_mp3_to_wav(file.as_posix(), filename + '.wav')