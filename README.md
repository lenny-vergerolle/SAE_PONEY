# SAE 3.02 SAE_PONEY

## Informations du groupe
- Vergerolle Lenny 23 (chef de projet)
- Hun Valentin 23
- Akhtar Naima 21

## Commandes pratiques
Une fois connecté à mysql : 
- supprimer la base de données : `source delPon.sql;`
- créer la base de données : `source creaPon.sql;`
- ajouter les insertions : `source insPon.sql;`
  
## Organisation 

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



pour lancer les tests : `python -m unittest src/models/tests/tests_BD.py`