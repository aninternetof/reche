from bs4 import BeautifulSoup
import click
import requests
import urllib.request
import subprocess
from PIL import Image


def get_first_image(url, img_dst):
    tree = BeautifulSoup(requests.get(url).text, 'html.parser')
    img_url = tree.find_all('img')[0].attrs['src'].replace('500.jpg', '1280.jpg')
    urllib.request.urlretrieve(img_url, img_dst)
    return img_url


def overlay(foreground_loc, background_url, dest):
    BACKGROUND_LOC = '/tmp/background.jpg'
    fore = Image.open(foreground_loc, 'r')
    fore_w, fore_h = fore.size
    urllib.request.urlretrieve(background_url, BACKGROUND_LOC)
    back = Image.open(BACKGROUND_LOC, 'r')
    back_w, back_h = back.size
    offset = (int((back_w - fore_w) / 2), int((back_h - fore_h) / 2))
    back.paste(fore, offset)
    back.save(dest)


def set_background(img_loc):
    script="""sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '%s'" && killall Dock"""""
    subprocess.Popen(script % img_loc, shell=True)


@click.command()
@click.option('--url', default='http://a-la-recherche.tumblr.com/',
              help='The url of the Tumblr feed to follow')
@click.option('--back_url', default='http://i.imgur.com/AoInTCS.jpg',
              help='The url of the background image')
def cli(url, back_url):
    TUMBLR_IMG_DST = '/tmp/tumblr_img.jpg'
    FINAL_IMG_DST = '/tmp/final_img.jpg'

    if not url:
        click.echo('Please provide a Tumblr feed url with the --url option')
    img_url = get_first_image(url, TUMBLR_IMG_DST)
    overlay(TUMBLR_IMG_DST, back_url, FINAL_IMG_DST)
    set_background(FINAL_IMG_DST)
    click.echo('Desktop set to {}'.format(img_url))

