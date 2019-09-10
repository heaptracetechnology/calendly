# _Calendly_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
[![Build Status](https://travis-ci.com/omg-services/calendly.svg?branch=master)](https://travis-ci.com/omg-services/freshdesk)
[![codecov](https://codecov.io/gh/omg-services/calendly/branch/master/graph/badge.svg)](https://codecov.io/gh/omg-services/freshdesk)

An OMG service for calendly.

## Direct usage in [Storyscript](https://storyscript.io/):

##### Create webhook subscription 
```coffee
calendly create  events=<HOOKs_ID> url=<URL> 
{ "id": 497954 }
```
##### Get webhook subscription 
```coffee
calendly subscribe hooksId=<HOOKS_ID>
{"attributes": {"created_at": "2019-09-10T06:51:55Z","events": ["invitee.created"],"state": "active","url": "https://blah.foo/bar"},"id": 497836,"type": "hooks"}
```
##### Get list of webhook subscription
```coffee
calendly subscribeList
 {"attributes": {"created_at": "2019-09-10T06:51:55Z","events": ["invitee.created"],"state": "active",  "url": "https://blah.foo/bar" },"id": 497836,"type": "hooks" }
```
##### Delete webhook subscription
```coffee
calendly delete hooksId=<HOOKS_ID>
{"success": true }
```
##### User event type 
```coffee
calendly eventType
{"attributes": {"active": true,"color": "#dfc12d","created_at": "2019-09-06T14:11:34Z","description": null,"duration": 15,"location":null,"name": "15 Minute Meeting","slug": "15min","updated_at": "2019-09-06T14:11:34Z","url": "https://calendly.com/demot636/15min"},"id": "HFBKCTZQZLEX6CW3","type": "event_types"}
```
##### About me
```coffee
calendly about
"attributes": {"avatar": {"url": null}, "created_at": "2019-09-06T14:10:06Z","email": "demot636@gmail.com","slug": "demot636","timezone": "Asia/Kolkata","updated_at": "2019-09-09T06:36:36Z","url": "https://calendly.com/demot636"},"id": "BAGAC7NEYKNJOTOJ","type": "users"}
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Create webhook subscription
```shell
$ omg run create -a events=<Events> -a url=<URL>  -e API_KEY=<API_KEY> 
```
##### Get webhook subscription
```shell
$ omg run subscribe -a hooksId=<HOOKS_ID> -e API_KEY=<API_KEY> 
```
##### Get list of webhook subscription
```shell
$ omg run subscribeList -e API_KEY=<API_KEY> 
```
##### Delete webhook subscription
```shell
$ omg run delete -a hooksId=<HOOKS_ID> -e API_KEY=<API_KEY> 
```
##### User event type
```shell
$ omg run eventType -e API_KEY=<API_KEY> 
```
##### About me
```shell
$ omg run about -e API_KEY=<API_KEY> 
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/calendly/blob/master/LICENSE).
