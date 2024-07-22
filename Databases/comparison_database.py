import play_audio as play
import secondary_methods as s2t
import text2speech as t2s
import webbrowser as web
import subprocess as sub
import os

def comparison_said_text(text):
    text = text.lower()

##exit
    if any(i in text for i in("exit", "stop", "stopp", "abbruch", "aboard")):
        raise SystemExit

##Youtube.com
    if all(i in text for i in("öffne", "youtube")):
        web.open_new_tab("https://www.youtube.com")
    
 
    elif all(i in text for i in("suche", "youtube")):
        suche = text.replace("suche ","").replace(" auf youtube","")
        web.open_new_tab("https://www.youtube.com/results?search_query=" + suche)

##Google.com
    elif all(i in text for i in("öffne", "google")):
        web.open_new_tab("https://www.google.com")    
    
    elif all(i in text for i in("suche", "google")):
        suche = text.replace("suche ","").replace(" auf google","")
        web.open_new_tab("https://www.google.com/search?q=" + suche)

## Öffne Dateien / Programme
    elif all(i in text for i in("starte", "world of warships")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\WoWs.ahk")

    elif all(i in text for i in("öffne", "reddit")):
        web.open_new_tab("https://www.reddit.com")

    elif all(i in text for i in("starte", "war", "thunder")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\Warthunder.ahk")

    elif all(i in text for i in("öffne", "disney")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\DisneyPlus.ahk")
    
    elif all(i in text for i in("öffne", "netflix")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\\Netflix.ahk")
    
    elif all(i in text for i in("öffne", "prime")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\PrimeVideo.ahk")
    
    elif all(i in text for i in("öffne", "Assassin")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\AC_BlackFlag.ahk")
    
    elif all(i in text for i in("öffne", "Fusion")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\Fusion.ahk")
    
    elif all(i in text for i in("öffne", "gimp")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\Gimp.ahk")
    
    elif all(i in text for i in("öffne", "Krypto")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\Kryptobuch.ahk")
    
    elif all(i in text for i in("öffne", "opera")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\Opera.ahk")
    
    elif all(i in text for i in("starte", "Satis")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\Satisfactory.ahk")
    
    elif all(i in text for i in("öffne", "vivaldi")):
        os.system("F:\Programmieren\python\Sprachassistent\AHK\\vivaldi.ahk") 
    
    # elif all(i in text for i in("öffne", "")):
    #     os.system("F:\Programmieren\python\Sprachassistent\AHK\.ahk")
    
    # elif all(i in text for i in("öffne", "")):
    #     os.system("F:\Programmieren\python\Sprachassistent\AHK\.ahk")
    
    # elif all(i in text for i in("öffne", "")):
    #     os.system("F:\Programmieren\python\Sprachassistent\AHK\.ahk")
    
    # elif all(i in text for i in("öffne", "")):
    #     os.system("F:\Programmieren\python\Sprachassistent\AHK\.ahk")
    
    ##else
    else:
        t2s.output_speak("Zu Ihrem Wunsch konnte ich leider nichts finden")

## Testaufrufe
# testaufruf = "öffne reddit"
# comparison_said_text(testaufruf)
    
    



