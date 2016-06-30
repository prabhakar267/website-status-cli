import time
import requests
import click

DEFAULT_HEADERS = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36"

"""
Function to check website status and return response according to code

:params:
    url     string
    code    boolean     if set to True, send status_code, else True/False
:return:
    status          string      if code is set False
    status_code     integer     if code is set True
    None                        if URL is not of proper format
"""
def __check_website(url, code):
    try:
        response = requests.get(url, headers={'user_agent': DEFAULT_HEADERS}, timeout=15)
        website_status_code = response.status_code
        if code:
            return website_status_code
        else:
            if website_status_code == 200:
                return True
            else:
                return False
    except requests.exceptions.Timeout, requests.exceptions.ConnectionError:
        if code:
            return -1
        else:
            return False
    except requests.exceptions.MissingSchema, message:
        print message
        return

"""
Function to check if the URL is present in the parameter or not
"""
def validate_url(ctx, param, value):
    if not value:
        raise click.BadParameter('You need to enter URL\ne.g. --url=http://www.prabhakargupta.com')
    else:
        return value

"""
Main Function to print response

:params:
    url     string      required-field
    code    boolean     
    f       integer     
"""
@click.command()
@click.option('--url', callback=validate_url, help="URL whose status is to be checked")
@click.option('--code', is_flag=True, help="If set, then returns status code of the URL passed")
@click.option('--f', default=0, help="Number of seconds after which the check is to be repeated")
def website_code(url, code, f):
    if f is not 0:
        while True:
            response = __check_website(url, code)

            if response is None:
                exit()

            print response
            time.sleep(f)
    else:
        print __check_website(url, code)

