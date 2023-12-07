
import whisper
from pytube import YouTube
from whisper.utils import format_timestamp
from summa.summarizer import summarize
from deep_translator import GoogleTranslator
from langdetect import detect
import os

model = whisper.load_model("large-v3")

# Configurations
UPLOADS_FOLDER = "./uploads"
if not os.path.exists(UPLOADS_FOLDER): # Create necessary directories
    os.makedirs(UPLOADS_FOLDER)


def download_audio_from_youtube(youtube_url):
    
    # Create a YouTube object
    yt = YouTube(youtube_url)
    # Select the audio stream (you may want to choose the best quality)
    audio_stream = yt.streams.filter(only_audio=True).first()
    # download
    file_name = 'youtube_audio'
    audio_stream.download(output_path= UPLOADS_FOLDER, filename= file_name)
    # return with file path
    return f"./{UPLOADS_FOLDER}/{file_name}"


def Transcribe_whisper(audio_path):

  # Transcribe the audio from the video
  text_time = model.transcribe(audio_path)
  script=text_time['text']
  script_lang=text_time['language']
  return script,script_lang


def translate_en_script(input,script_lang):

  if(script_lang=='en'):
      return input
  else:
    max_chunk_length = 500  # The maximum allowed query length
    text_chunks = [input[i : i + max_chunk_length] for i in range(0, len(input), max_chunk_length)]
    translated_chunks = [GoogleTranslator(source='auto', target='en').translate(chunk) for chunk in text_chunks]
    translated_text = " ".join(translated_chunks)
    return translated_text

def translate_ar_script(input,script_lang):

  if(script_lang=='ar'):
      return input
  else:
    max_chunk_length = 500  # The maximum allowed query length
    text_chunks = [input[i : i + max_chunk_length] for i in range(0, len(input), max_chunk_length)]
    translated_chunks = [GoogleTranslator(source='auto', target='ar').translate(chunk) for chunk in text_chunks]
    translated_text = " ".join(translated_chunks)
    return translated_text


def translate_en(input):

        max_chunk_length = 500  # The maximum allowed query length
        text_chunks = [
          input[i : i + max_chunk_length] for i in range(0, len(input), max_chunk_length)
          ]
        translated_chunks = [GoogleTranslator(source='auto', target='en').translate(chunk) for chunk in text_chunks]
        translated_text = " ".join(translated_chunks)
        return translated_text

def translate_ar(input):

        max_chunk_length = 500  # The maximum allowed query length
        text_chunks = [
          input[i : i + max_chunk_length] for i in range(0, len(input), max_chunk_length)
          ]
        translated_chunks = [GoogleTranslator(source='auto', target='ar').translate(chunk) for chunk in text_chunks]
        translated_text = " ".join(translated_chunks)
        return translated_text

def get_summary(text):
    
    en_summary = summarize(text,ratio=0.2, language="english")
    ar_summary=translate_ar(en_summary)

    return en_summary,ar_summary



### Finial_recall_functions ###

def proccesVideoAudioFile(video_audio_File_Path):

  script,script_lang=Transcribe_whisper(video_audio_File_Path)
  ar_script=translate_ar_script(script,script_lang)
  en_script=translate_en_script(script,script_lang)
  en_summary,ar_summary=get_summary(en_script)

  result={
      "ar_script":ar_script,
      "en_script":en_script,
      "ar_summary":ar_summary,
      "en_summary":en_summary
  }

  return result


def proccesYoutubeLinkVideo(link):

  audio_path=download_audio_from_youtube(link)
  script,script_lang=Transcribe_whisper(audio_path)
  ar_script=translate_ar_script(script,script_lang)
  en_script=translate_en_script(script,script_lang)
  en_summary,ar_summary=get_summary(en_script)

  result={
      "ar_script":ar_script,
      "en_script":en_script,
      "ar_summary":ar_summary,
      "en_summary":en_summary
  }

  return result