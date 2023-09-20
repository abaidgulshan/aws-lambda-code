import urllib3


def lambda_handler(event, context):
    # Make the HTTPS request
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://www.google.com')

    #response.data
    print('Response content:', response.data)
    print('Response status code:', response.status)