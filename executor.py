import paramiko

class KaliCommandExecutor:
    def __init__(self, host, user, key_path):
        self.host = host
        self.user = user
        self.key_path = key_path
    
    def run(self, cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, username=self.user,key_filename=self.key_path)

        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()
        return output, error