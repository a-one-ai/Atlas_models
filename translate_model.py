from deep_translator import GoogleTranslator
from langdetect import detect



def translate(input,script_lang):
    max_chunk_length = 500  # The maximum allowed query length
    text_chunks = [
        input[i : i + max_chunk_length] for i in range(0, len(input), max_chunk_length)
        ]
    translated_chunks = [GoogleTranslator(source='auto', target=script_lang).translate(chunk) for chunk in text_chunks]
    translated_text = " ".join(translated_chunks)
    return translated_text


