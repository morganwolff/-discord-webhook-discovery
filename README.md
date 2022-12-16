# Discord Webhook Discovery

## Project Description

The goal of the project is to create a python script using discord.py to transform a CSV file containing information about the raspberry pi 4 into a list of lists,<br>
subsequently allowing to create a discord webhook in order to know the availability of the product, its price, its photo as well as a link redirecting us to the site in order to be able to buy it in the event that the product is available for sale.<br>
The webhook will appear in red if out of stock, and in verse otherwise.

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