import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for up to 20 seconds...")
    
    # Set timeout and phrase_time_limit for longer recordings
    recorded_audio = recognizer.listen(source, timeout=None, phrase_time_limit=20)  # Listen for up to 20 seconds
    print("Done recording.")

# Ask the user for the language code
language_code = input("Enter the language code (e.g., 'en-US' for English, 'hi-IN' for Hindi, 'te-IN' for Telugu): ")

try:
    print("Recognizing the text...")
    text = recognizer.recognize_google(recorded_audio, language=language_code)
    print("Decoded Text: {}".format(text))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as ex:
    print(f"An error occurred: {ex}")
