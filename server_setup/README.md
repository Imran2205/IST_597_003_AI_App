# Lab Server
- Server domain: `i4-cs-gpu01.ist.psu.edu`
- CPU: Intel® Xeon® Processor E5 Family
- RAM: 64 GB memory
- Storage: 9 TB disk space total
- GPU: 2xNVIDIA GeForce GTX 1080 Ti (11GB each)

## Important Commands
- [Make ssh command easier](./ssh_config.md)
- [Anaconda Installation and Environment Creation](./anaconda_setup.md)
- [Access Jupyter Notebook from local computer](./jupyter_server.md)
- [Secure Copy](./scp_commands.md)
- [Screen Commands](./screen_commands.md)

[//]: # (- [Configuring RSA for password less authentication]&#40;important_commands/rsa_setup.md&#41;)


[//]: # (## Available Datasets and Models)

[//]: # (- [Datasets]&#40;datasets_and_models/datasets.md&#41;)

[//]: # (- [Models]&#40;datasets_and_models/models.md&#41;)

[//]: # (- [Setting up Llama models]&#40;datasets_and_models/setting_up_llama.md&#41;)

## Productivity commands
- Quick login: `ssh -J your_jump_server_username@ssh.ist.psu.edu your_server_username@i4-cs-gpu01.ist.psu.edu`

[//]: # (- If shortcuts are set up: `ssh a11y_server`)
- For human-readable output of `ls` command, add `-h` (e.g., `ls -l -h`)

## Using VS Code locally
- In VS Code, install `Remote Development` extension. A new icon will appear on the left sidebar named `Remote Explorer`. 
- Click on `Remote Explorer` and provide the log-in credential in the address bar to see the remote files/folders 

