
# README

## Description

Ce programme est conçu pour cloner un site web en utilisant une combinaison de Puppeteer et HTTrack. Il visite chaque lien du site à l'aide de Puppeteer, puis utilise HTTrack pour copier le site localement, en s'assurant que tous les liens pertinents sont inclus.

## Prérequis

- **Node.js**: Assurez-vous que Node.js est installé sur votre machine, car Puppeteer nécessite Node.js pour fonctionner.
- **HTTrack**: Cet outil est utilisé pour cloner le site web. Vous devez l'avoir installé sur votre machine.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez Puppeteer en utilisant npm :

   ```bash
   npm install puppeteer
   ```

3. Assurez-vous que HTTrack est installé. Vous pouvez l'installer via votre gestionnaire de paquets préféré :

   - Sous Ubuntu/Debian :
     ```bash
     sudo apt-get install httrack
     ```

   - Sous macOS (via Homebrew) :
     ```bash
     brew install httrack
     ```

## Utilisation

1. Modifiez le fichier Python pour spécifier l'URL du site que vous souhaitez cloner et le répertoire de sortie souhaité :

   ```python
   site_url = "https://www.andapirate.com"  # Remplacez par l'URL de votre choix
   output_directory = "Clone_Panda"  # Remplacez par le répertoire de sortie souhaité
   ```

2. Exécutez le script Python :

   ```bash
   python script.py
   ```

3. Après l'exécution du script, le site sera cloné dans le répertoire spécifié. **Note importante :** Certains fichiers HTML peuvent ne pas avoir d'extension. Vous devez ajouter l'extension `.html` manuellement à ces fichiers pour qu'ils soient correctement reconnus comme des fichiers HTML.

## Fonctionnement

1. **Étape 1 :** Le script écrit un script Puppeteer temporaire en JavaScript qui ouvre la page d'accueil du site et collecte tous les liens sur cette page.
2. **Étape 2 :** Puppeteer visite chaque lien collecté, enregistre les liens et les transmet au script Python.
3. **Étape 3 :** HTTrack est utilisé pour cloner le site en fonction des liens visités par Puppeteer. HTTrack télécharge toutes les pages, images et autres ressources liées.
4. **Étape 4 :** Les fichiers clonés sont stockés dans le répertoire de sortie.

## Problèmes courants

- **Erreur de Puppeteer** : Si Puppeteer rencontre des erreurs lors de la visite des liens, vérifiez que l'URL du site est correcte et accessible.
- **Fichiers sans extension** : Après le clonage, certains fichiers peuvent ne pas avoir d'extension. Ajoutez `.html` manuellement pour que ces fichiers soient reconnus comme des fichiers HTML.
