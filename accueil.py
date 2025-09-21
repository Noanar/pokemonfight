from jeu_pokemon import Jeu, liste_1, liste_2

if __name__ == "__main__":
    print("=== Bienvenue dans le jeu Pokémon ===")
    print("Deux joueurs vont composer leurs équipes et s'affronter !\n")

    # Création et lancement du jeu
    jeu = Jeu(liste_1, liste_2)
    jeu.jouer()
