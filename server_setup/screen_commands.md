### To start a new screen
```shell
screen -S <screen_name>
```
### To see the currently running screens
```shell
screen -ls
```
### To reattach a screen
```shell
screen -r <screen_name>
```
### To terminate a screen session
```shell
screen -XS <session-id> quit
```