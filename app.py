from bs4 import BeautifulSoup
import click
import requests
import urllib.request
import subprocess

IMG_DST = '/tmp/img.jpg'



def get_first_image(url, img_dst):
    tree = BeautifulSoup(requests.get(url).text, 'html.parser')
    img_url = tree.find_all('img')[2].attrs['src'].replace('500.jpg', '1280.jpg')
    urllib.request.urlretrieve(img_url, img_dst)
    return img_url

def set_background(img_loc):
    script="""sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '%s'" && killall Dock"""""
    subprocess.Popen(script % img_loc, shell=True)

@click.command()
@click.option('--url', default='http://a-la-recherche.tumblr.com/', help='The url of the Tumblr feed to follow')
def cli(url):
    if not url:
        click.echo('Please provide a Tumblr feed url with the --url option')
    img_url = get_first_image(url, IMG_DST)
    set_background(IMG_DST)
    click.echo('Background set to {}'.format(img_url))

