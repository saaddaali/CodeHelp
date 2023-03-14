import openai

# Clé d'API
openai.api_key = "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"


while True:
    # Demander à l'utilisateur de saisir une recherche
    prompt = input("Tape ta question ('exit' pour sortir) : ")
    if prompt == "exit":
        break
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
