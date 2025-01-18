# SAE 3.02 SAE_PONEY

## Informations du groupe
- Vergerolle Lenny 23 (chef de projet)
- Hun Valentin 23
- Akhtar Naima 21

## Commandes pratiquesw
Une fois connecté à mysql : 
- supprimer la base de données : `source delPon.sql;`
- créer la base de données : `source creaPon.sql;`
- ajouter les insertions : `source insPon.sql;`
  
## Organisation 1ère Partie

|  date  | Lenny (chef de projet)        |  Valentin           | Naima             |
|--------|-------------------------------|---------------------|-------------------|
| 16/09  | diagramme de CU               |  MCD                | MCD               |
| 23/09  |finalisation diagramme du CU et du MCD (pour tout le monde)              |       
| 30/09  | implémentation trigger/check  | création maquettes  | implémentation BD |
| 07/10  | travail sur la SAE dev eff + qualité dev (pour tout le monde)           |
| 14/10  | travail sur la SAE crypto     |SAE crypto           | SAE crypto        |
| 21/10  | SAE FI                        |                     |                   |
| 04/11  | SAE FI                        |                     |                   |
| 12/11  | maquette                      | maquette            | insertions BD     |
| 18/11  | maquettes + triggers          | maquettes           | rapport           |
| 21/11  | triggers                      |                     | triggers          |


## Commandes à réaliser pour lancer l'application

- Pour installer les prérequis : `./init.sh`
- Pour lancer : `./start.sh`

## Pour tester la BD
- Pour lancer les tests : `python -m unittest src/models/tests/tests_BD.py`

## Fonctionnalités implémentées


### Pour un visiteur :
- Consulter les informations du club sur la page d’accueil.
- S’inscrire en tant qu’adhérent.
- Se connecter, si la personne a déjà un compte.

### Pour un administrateur :
- Se connecter/se déconnecter.
- Modifier son profil : la photo de profil, le nom, le prénom, etc.

## Après la soutenance :

- Gérer les poneys : consulter la liste des poneys et ajouter/supprimer/modifier un poney.
- Gérer les moniteurs : consulter la liste des moniteurs et ajouter/supprimer/modifier un moniteur.
- Gérer les adhérents : consulter la liste des adhérents et ajouter/supprimer un adhérent.
- Historique : garder en mémoire toutes les réservations même si elles sont supprimées.
- Modifier le mot de passe des autres


### Pour un moniteur :
- Se connecter/se déconnecter.
- Consulter son planning : supprimer une réservation présente dans le planning.
- Modifier son profil : la photo de profil, le nom, le prénom
## Après la soutenance :

- Créer un cours privé pour un adhérent.
- Gérer ses réservations (depuis la navbar et depuis le planning) : consulter la liste des réservations et ajouter/supprimer une réservation.
- Modifier son mot de passe
### Pour un adhérent :
- Se connecter/se déconnecter.
- Consulter son planning.
- Réserver un cours.
- Modifier son profil : la photo de profil, le nom, le prénom, etc.


## Après la soutenance :

- Gérer ses réservations (depuis la navbar et depuis le planning) : consulter la liste des réservations et ajouter/supprimer une réservation.
- Modifier son mot de passe

