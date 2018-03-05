def main():
    import requests

    url = 'http://facebook.com'

    r = requests.get(url, auth('stallmanor', 'eltenior'))

    print(r.status_code

    )

if __name__ == '__main__':
    main()
