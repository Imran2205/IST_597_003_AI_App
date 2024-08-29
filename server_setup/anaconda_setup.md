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