from requests import Session
import argparse

def cli_args():
    desc = 'use --slow or --quick to modify response type. use --url to modify default URL'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--slow', action='store_true')
    parser.add_argument('--quick', action='store_true')
    parser.add_argument('--url')

    return parser.parse_args()

def slow(url_base):
    s = Session()
    s.get(f"{url_base}/")
    resp = s.get(f"{url_base}/slow_response")

    print(resp.text[:500])

def quick(url_base):
    s = Session()
    s.get(url_base)
    resp = s.get(f"{url_base}/quick_response")

    print(resp.text[:500])

if __name__ == '__main__':

    url_base = 'https://lab.je-clark.com'

    a = cli_args()

    print(a)

    if a.url:
        url_base = a.url

    print(url_base)

    if a.slow:
        slow(url_base)
    if a.quick:
        quick(url_base)
