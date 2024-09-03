### Secure Copy
```shell
scp -o ProxyJump=your_jump_server_username@ssh.ist.psu.edu:22  -r /local_abs_path_to_files/* your_server_username@i4-cs-gpu01.ist.psu.edu:/abs_path_to_dest_folder/
```