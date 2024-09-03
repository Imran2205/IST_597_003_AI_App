### Forward jupyter server to localhost of local machine

- Log in to the remote **GPU server** as follows: `ssh -J your_jump_server_username@ssh.ist.psu.edu your_server_username@i4-cs-gpu01.ist.psu.edu`
- Check all virtual environments: `conda info --envs`. In case you need to create a new environment use: `conda create -n new_envn` 
- Select your virtual environment (e.g., chatllma) : `conda activate venv311`
- Next, run the notebook on the remote **GPU server** as follows: `jupyter notebook --no-browser --port=8080`

[//]: # (- Next, create tunnel on your **local machine** as follows: `ssh -L 8080:localhost:8080 a11y_server`)
- Next, create tunnel on your **local machine** as follows: `ssh -L port:localhost:port -J ******@ssh.ist.psu.edu ******@i4-cs-gpu01.ist.psu.edu`
- Finally, on your **local machine**, open the browser and go to: `http://localhost:8080/`
- To deactivate your session, press `Crtl+C`, then then type `exit` twice


