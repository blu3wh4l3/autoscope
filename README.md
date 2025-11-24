## Install Paramiko
sudo apt install python3-paramiko
## SSH Key Generation
ssh-keygen -t ed25519    # accept defaults
ssh-copy-id username@192.168.1.42   # if ssh-copy-id available
# or manually copy ~/.ssh/id_ed25519.pub into Kali's ~/.ssh/authorized_keys