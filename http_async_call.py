import requests
import asyncio


def main():
    loop1 = asyncio.get_event_loop()
    request1 = loop1.run_in_executor(None, requests.get, 'https://webhook.site/0c5e7c09-ee98-4e7d-9e51-653662301d50')
    request2 = loop1.run_in_executor(None, requests.get, 'https://webhook.site/0c5e7c09-ee98-4e7d-9e51-653662301d50')
    request3 = loop1.run_in_executor(None, requests.get, 'https://webhook.site/0c5e7c09-ee98-4e7d-9e51-653662301d50')

    response1 = yield from request1
    response2 = yield from request2
    response3 = yield from request3

    print(response1.headers.get('Date'))
    print(response2.headers.get('Date'))
    print(response3.headers.get('Date'))


loop2 = asyncio.get_event_loop()
loop2.run_until_complete(main())
