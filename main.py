import sqlite3
from pathlib import Path
from requetes import print_aeroport, print_num_vol_ville_depart_ville_arrivee, print_passager_num_vol, print_passager_vol, print_passagers, print_vols, vol_passager, get_id_vol
from connexion import ouvrir_connexion
from affichage import afficher_resultat


try:    
    conn = ouvrir_connexion("gestion_aeroports.db")

    while True :

        print("\n======== MENU GESTION AEROPORTS ========\n")
        print("1. Afficher le nom et la ville de tous les aéroports ")
        print("2. Afficher le numéro, la date et le statut des vols dont le statut vaut Programme")
        print("3. Afficher le nom et le prénom des passagers du vol CM101")
        print("4. Afficher le nom et le prénom de chaque passager avec le numéro de son vol")
        print("5. Afficher chaque numéro de vol avec sa ville de départ et sa ville d’arrivée")
        print("6. Afficher les passagers du vol CM101")
        print("7. Afficher tous les vols avec le nom et le prénom de leurs passagers, y compris les vols sans inscription")
        print("8. Quitter")
        choice = int(input("\n Faites un choix : "))

    

        if choice == 1:
    
            rows = print_aeroport(conn)
            afficher_resultat("AEROPORTS ET LEURS VILLES", rows)
        
        elif choice == 2:
        
            rows = print_vols(conn, "Programme")
            afficher_resultat("VOLS PROGRAMMES", rows)
        
        elif choice == 3:
            row = get_id_vol(conn, "CM101")
            if isinstance(row, str):
                print(row)  # Affiche le message d'erreur si le vol est introuvable
            else:
                rows = print_passagers(conn, row[0])  # Utilise l'ID du vol pour récupérer les passagers
                afficher_resultat(f"PASSAGERS DU VOL CM101", rows)
                         
        elif choice == 4:
            rows = print_passager_num_vol(conn)
            afficher_resultat("PASSAGERS ET LEURS VOLS", rows)
        
        elif choice == 5:
        
            rows = print_num_vol_ville_depart_ville_arrivee(conn)
            afficher_resultat("VOLS AVEC VILLE DE DEPART ET VILLE D'ARRIVEE", rows)
            
        elif choice == 6:

            rows = print_passager_vol(conn)
            afficher_resultat("PASSAGERS DU VOL CM101", rows)
                    
        elif choice == 7:
            print("\n++++ TOUS LES VOLS ET LEURS PASSAGERS ++++\n")
            vol_passager(conn)
            
        elif choice == 8:
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")
            
finally:
    conn.close()