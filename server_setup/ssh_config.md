## Default ssh command
```shell
ssh -J your_jump_server_username@ssh.ist.psu.edu your_server_username@i4-cs-gpu01.ist.psu.edu
```

[//]: # (## Create ssh config file)

[//]: # ()
[//]: # (```shell)

[//]: # (# Create a config file in the .ssh directory of the local machine )

[//]: # (# &#40;which should be in your home directory&#41; )

[//]: # (# create a config file in the .ssh directory)

[//]: # (nano .ssh/config)

[//]: # (```)

[//]: # ()
[//]: # (#### Put the following code snippet in that file)

[//]: # ()
[//]: # (```shell)

[//]: # (Host ssh_ist)

[//]: # (   Hostname ssh.ist.psu.edu)

[//]: # (   Port 22)

[//]: # (   User your_jump_server_username)

[//]: # ()
[//]: # (Host a11y_server)

[//]: # (   Hostname i4-l-skb5969-1.ist.psu.edu)

[//]: # (   User your_server_username)

[//]: # (   ProxyJump ssh_ist)

[//]: # (```)

[//]: # ()
[//]: # (#### save the file. now you should be able to ssh to the server using)

[//]: # ()
[//]: # (```shell)

[//]: # (ssh a11y_server)

[//]: # (# or)

[//]: # (ssh your_server_username@a11y_server)

[//]: # (```)