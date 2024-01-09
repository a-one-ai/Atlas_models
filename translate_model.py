from deep_translator import GoogleTranslator
import re

def word_tokenization(text):
    words = re.findall(r'\b\w+\b', text)
    return words

def translate(input, script_lang):
    max_chunk_length = 500  # The maximum allowed query length
    words = word_tokenization(input)
    
    translated_chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) <= max_chunk_length:
            current_chunk += word + " "
        else:
            translated_chunk = GoogleTranslator(source='auto', target=script_lang).translate(current_chunk.strip())
            translated_chunks.append(translated_chunk)
            current_chunk = word + " "

    # Translate the last chunk
    if current_chunk:
        translated_chunk = GoogleTranslator(source='auto', target=script_lang).translate(current_chunk.strip())
        translated_chunks.append(translated_chunk)

    translated_text = " ".join(translated_chunks)
    return translated_text
