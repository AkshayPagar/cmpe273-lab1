import requests


def main():
    r = requests.get('https://webhook.site/0c5e7c09-ee98-4e7d-9e51-653662301d50')
    r1 = requests.get('https://webhook.site/0c5e7c09-ee98-4e7d-9e51-653662301d50')
    r2 = requests.get('https://webhook.site/0c5e7c09-ee98-4e7d-9e51-653662301d50')

    print('Date =', r.headers.get('Date'))
    print('Date =', r1.headers.get('Date'))
    print('Date =', r2.headers.get('Date'))


main()
