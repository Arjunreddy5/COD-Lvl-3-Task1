import pyttsx3
from gtts import gTTS
import os
import argparse

# Function to list available languages in gTTS
def list_gtts_languages():
    from gtts.lang import tts_langs
    languages = tts_langs()
    for lang in languages:
        print(f"{lang}: {languages[lang]}")

# Function to list available voices in pyttsx3
def list_pyttsx3_voices(engine):
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"ID: {voice.id}\nName: {voice.name}\nLanguages: {voice.languages}\nGender: {voice.gender}\nAge: {voice.age}\n")

# Function to synthesize speech using pyttsx3
def synthesize_pyttsx3(text, voice_id=None, rate=150, volume=1.0):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()

# Function to synthesize speech using gTTS
def synthesize_gtts(text, language='en', slow=False, filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(filename)
    os.system(f"start {filename}" if os.name == "nt" else f"xdg-open {filename}")

# Main function to handle user input and synthesis
def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech Conversion Application")
    parser.add_argument('text', type=str, help="Text to convert to speech")
    parser.add_argument('--engine', type=str, choices=['pyttsx3', 'gtts'], default='pyttsx3', help="TTS engine to use")
    parser.add_argument('--language', type=str, default='en', help="Language for TTS (gTTS only)")
    parser.add_argument('--slow', action='store_true', help="Slow speech (gTTS only)")
    parser.add_argument('--voice_id', type=str, help="Voice ID for pyttsx3")
    parser.add_argument('--rate', type=int, default=150, help="Speech rate for pyttsx3")
    parser.add_argument('--volume', type=float, default=1.0, help="Volume for pyttsx3")
    parser.add_argument('--list_voices', action='store_true', help="List available voices (pyttsx3)")
    parser.add_argument('--list_languages', action='store_true', help="List available languages (gTTS)")

    args = parser.parse_args()

    if args.list_voices:
        engine = pyttsx3.init()
        list_pyttsx3_voices(engine)
        return

    if args.list_languages:
        list_gtts_languages()
        return

    if args.engine == 'pyttsx3':
        synthesize_pyttsx3(args.text, voice_id=args.voice_id, rate=args.rate, volume=args.volume)
    elif args.engine == 'gtts':
        synthesize_gtts(args.text, language=args.language, slow=args.slow)

if __name__ == "__main__":
    main()
    """
      !! Write the path of this file in CMD, after that use below commands
               # Synthesizing Text to Speech using pyttsx3:
               - python ttscapp.py "Hello there! How are you?" --engine pyttsx3 --rate 150 --volume 9.0


             # Synthesizing Text to Speech using gTTS: 
            - python ttscapp.py "Hello, this is a test." --engine gtts --language en --slow
  """
