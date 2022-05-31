# pyjwt-oaep-poc
PoC proving support for OAEP in pyjwt

## Requirements

- pipenv
- chromium (headless)

## Setting up

```shell
pipenv install
```

## Running the PoC

Execute the backend with

```shell
pipenv run backend.py
```

Then login with the client with

```shell
pipenv run client.py
```

When asked, the username is `user` and password is `pass`.

The token is printed on the console. Use <https://jwt.io/> to double check that the algorithm `RSA-OAEP` is correctly being decoded.


## Considerations

- The keycloak is a dedicated instance hosted by <https://www.cloud-iam.com>. Thanks a bunch for the free offering which made this PoC incredibly easy.

- Code is part of an article which I authored about SSO and Flask. You can read it on <https://paragraph.xyz/@digitalmeadow/[python]-sso-using-flask,-requests-oauthlib-and-pyjwt> for further details on implementation.

