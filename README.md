# TP2
## 2. Compléter le Dockerfile afin de builder correctement l’application contenu dans src/
![image](https://user-images.githubusercontent.com/71019269/210178398-ed6e2433-52fe-49aa-95ea-40711257d763.png)
![image](https://user-images.githubusercontent.com/71019269/210178410-5d247bb9-1d2f-42ab-a1ae-8dd960cff160.png)




## a. Une option de npm vous permet de n’installer que ce qui est nécessaire.
## Quelle est cette option ?
L'option est ```--production``` elle permet d'installer que les dépendances nécessaire à la production de l'application


## Quelle bonne pratique Docker permet t-elle de respecter ?
Cette bonne pratique permet d'alléger l'image et de la rendre plus maintenable et plus facile à déployer

## A l’aide de la commande docker build, créer l’image ma_super_app
```docker build -t ma_super_app .```

![image](https://user-images.githubusercontent.com/71019269/210178498-cbe081ab-450e-4cbc-84c7-1a667a0bd907.png)

```docker compose up```

![img.png](img.png)
![image](https://user-images.githubusercontent.com/71019269/210367635-5ab00d12-50a7-47c9-952d-e6f348ec2984.png)

