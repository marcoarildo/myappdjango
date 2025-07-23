#myappdjango

https://marcoapps.pythonanywhere.com

token
b832f13c98df88390b792daaf1491194254bbef2

import requests
username = 'marcoapps'
token = 'b832f13c98df88390b792daaf1491194254bbef2'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        


## deploy para pythonanywhere
```
$ pip install --user pythonanywhere
$ pa_autoconfigure_django.py https://github.com/marcoarildo/myappdjango.git --python=3.13
```

## atualizar projeto rodando
```
$ pa_autoconfigure_django.py https://github.com/marcoarildo/myappdjango.git --python=3.13 --nuke
```
