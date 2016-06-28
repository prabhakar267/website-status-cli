import requests
import click

DEFAULT_HEADERS = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36"

@click.command()
@click.option('--url', help="URL whose status is to be checked")
@click.option('--code', is_flag=True, help="If set, then returns status code of the URL passed")
def website_code(url, code):
    try:
        response = requests.get(url, headers={'user_agent': DEFAULT_HEADERS}, timeout=15)
        website_status_code = response.status_code
        if code:
            print website_status_code
        else:
            if website_status_code == 200:
                print True
            else:
                print False
    except requests.exceptions.Timeout, requests.exceptions.ConnectionError:
        if code:
            print -1
        else:
            print False

