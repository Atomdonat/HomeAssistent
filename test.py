import webbrowser as web

text = "suche nachrichten auf google"


if all(i in text for i in("suche", "google")):
    suche = text.replace("suche ","").replace(" auf google","")
    web.open_new_tab("https://www.google.com/search?q=" + suche)