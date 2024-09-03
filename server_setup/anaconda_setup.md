## Pre Installed Anaconda
Anaconda is already installed in the server

Add the following code snippet to .bashrc file of your home directory and restart the terminal.
You should be able to use the pre installed anaconda
```shell
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/data/shared/.anaconda/anaconda3/bin/conda' 'shell.bash' 'hoo$
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/data/shared/.anaconda/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/data/shared/.anaconda/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/data/shared/.anaconda/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```
### Pre configured conda environments
```shell
conda activate venv311
```

## Create environment
To create a conda environment with a custom name
```shell
conda create -n <custom_name> -y
```
To create environment with a specific python version
```shell
conda create -n <custom_name> python=<version> -y
```
To activate custom environment
```shell
conda activate <custom_name>
```

[//]: # (## To install custom pip within an environment)

[//]: # (To check available packages in your virtual environment)

[//]: # (```shell)

[//]: # (conda list -n [your_environment])

[//]: # (```)

[//]: # ()
[//]: # (```shell)

[//]: # (conda install -c conda-forge -n [your_env] [your package])

[//]: # (```)
