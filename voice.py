import openai
import pyttsx3
import speech_recognition as sr

# Clé d'API
openai.api_key = "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"


# Initialiser le recognizer
r = sr.Recognizer()

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

while True:
    # Ecouter pour la commande vocale
    with sr.Microphone() as source:
        print("Ecoute...")
        audio = r.listen(source)

    # Transcrire la commande vocale
    try:
        prompt = r.recognize_google(audio, language="fr-FR")
        print("Tu as dit: " + prompt)
        if prompt == "exit":
            break
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
        continue
    except sr.RequestError as e:
        print("Erreur de service; {0}".format(e))
        continue

    # Envoyer une requête à l'API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Afficher la réponse
    print(response["choices"][0]["text"])
    engine.say(response["choices"][0]["text"])
    engine.runAndWait()
