# Discord Webhook Discovery

## Project Description

Le but du projet est de créer un script python en utilisant discord.py afin de transformer un fichier CSV contenant des informations sur la raspberry pi 4 en list de lists,<br>
permettant par la suite de créer un webhook discord afin de connaitre la disponibilité du produit, son prix, sa photo ainsi qu’un lien nous redirigeant vers le site afin de pouvoir l’acheter dans le cas ou le produit est disponible à la vente.<br>
Le webhook apparaitra en rouge en cas de rupture de stock, et en vers dans le cas contraire.

### Example
<img src="img/image.png" width="350" title="hover text">

## Installation
- **MacOS**
```bash
brew install python
```
- **Linux**
```bash
sudo dnf install python3.11
```

### GitHub repository
- using **SSH**
```bash
git clone git@github.com:morganwolff/Discord-webhook-discovery.git
```
- using **HTTPS**
```bash
git clone https://github.com/morganwolff/Discord-webhook-discovery.git
```

## Usage
```
./webhook.py
```