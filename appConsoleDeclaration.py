articles = []

with open("declaration1789.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip().startswith("Art."):
            articles.append(line.strip())

if articles:
    articles_count = len(articles)
    print(f"Il y a {articles_count} articles disponibles dans le fichier.")

    while True:
        article_number = input("Entrez le numéro de l'article que vous souhaitez consulter (ou 'q' pour quitter) : ")

        if article_number.lower() == 'q':
            print("Au revoir !")
            break

        try:
            article_index = int(article_number) - 1
            if 0 <= article_index < len(articles):
                print(articles[article_index])
            else:
                print("L'article demandé n'existe pas.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")
else:
    print("Aucun article trouvé dans le fichier.")
