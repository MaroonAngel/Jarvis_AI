import speech_recognition as sr
import configparser
import re


def hot_word_detection(lang='en'):
    """
    Hot word (wake word / background listen) detection
    :param lang: str
        default 'en'
    :return: Bool, str
        status, command
    """
    config = configparser.ConfigParser()
    config.read('configs/config.ini')
    bot_name = config['default']['bot_name']    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("booting...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            print("listening...")
            audio = r.listen(source)
            print("processing...")
            command = r.recognize_google(audio, language=lang).lower()
            print("  Input: " + str(command))
            if re.search(bot_name, command):
                return True, command
            else:
                return False, None
    except Exception as e:
        # print("- Couldn't parse audio as speech. - " + str(e))
        return False, None


if __name__ == '__main__':
    hot_word_detection()
