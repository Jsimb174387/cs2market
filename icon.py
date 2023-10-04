# Retrieves Icon's from steam using api key.
# This is done like this: https://api.steampowered.com/<interface>/<method>/v<version>/
from flask import render_template

# GET https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/
# https://api.steampowered.com/ISteamEconomy/GetAssetClassInfo/v1/
# https://api.steampowered.com/ISteamEconomy/GetAssetClassInfo/v1/?key=95872D9716731EE3E51E63A2ADB8D25A


def display(url):
    # urllib.request.urlretrieve(url, f"{name}.png")
    # img = Image.open(f"{name}.png")
    # return serve_pil_image(img)
    return render_template('image.html', image_urls=url)
