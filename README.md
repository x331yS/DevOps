# github-actions

### 1. Si vous n’en possédez pas déjà un, créez vous un compte Github et lié votre compte via clé SSH à votre ordinateur.
![img.png](img.png)

### 2. Tester un premier workflow Github avec l’exemple suivant : https://docs.github.com/fr/actions/quickstart
![image](https://user-images.githubusercontent.com/71019269/211592002-ac5b2721-cc50-4edd-b089-cd2419bc5fcf.png)

### 3. Créer deux classes python, une classe SimpleMath contenant une fonction statique “addition” prenant deux arguments. Et une classe TestSimpleMath qui hérite de unittest.TestCase et contient une fonction de test unitaire
![image](https://user-images.githubusercontent.com/71019269/211594975-db81527d-85c8-480f-b550-c3863e9ab56a.png)

### 4. Pousser votre code sur un nouveau repository Github et avec Github Actions créer un workflow permettant de lancer les tests unitaires de votre application.
![image](https://user-images.githubusercontent.com/71019269/211598723-11b16d26-a781-4203-996b-a6d5ac8be11e.png)   ![image](https://user-images.githubusercontent.com/71019269/211598820-b7526719-fa9b-45c2-958e-c5596d8e84a4.png)
### 5. Créer la fonction soustraction et le test associé. Puis, pousser votre commit. Les tests sont effectués automatiquement via la pipeline.

![image](https://user-images.githubusercontent.com/71019269/211598899-3868246e-46c4-4058-845e-f5211c3cbff9.png)

### 6. Ajouter une étape de lint (validation statique et syntaxique de votre code source) dans votre workflow. Utiliser pylint.
![image](https://user-images.githubusercontent.com/71019269/211603286-64493a4d-1280-49c0-a3e4-14d87a74c092.png)


### 7. Ajouter une étape qui build un conteneur Docker embarquant votre application. La directive CMD de votre Dockerfile doit exécuter les tests unitaires dès le run d’un nouveau conteneur à partir de cette image.
![image](https://user-images.githubusercontent.com/71019269/211604687-868e9a8a-6ab4-4112-b8a6-6e39c249a854.png)
