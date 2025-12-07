import paramiko
import platform
import subprocess
from paramiko.ssh_exception import (
    NoValidConnectionsError,
    AuthenticationException,
    SSHException,
    BadHostKeyException
)
class Executor:

    OS_NAME = platform.system()
    """
    This module determines whether the code is running on a Kali Linux host. 
    If it is, commands are executed locally. If not, the module establishes an SSH connection to a Kali machine 
    and runs the commands remotely.
    """
    @staticmethod
    def is_kali():
        if Executor.OS_NAME!="Linux":
            return False
        try:
            with open("/etc/os-release") as f:
                return "kali" in f.read().lower()
            
        except:
            return False

    def __init__(self, host, user, key_path):
        self.host = host
        self.user = user
        self.key_path = key_path

    def run(self, command):
        if KaliCommandExecutor.is_kali():
            # Run command lcoally on kali
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout, result.stderr
        
        else:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                ssh.connect(self.host, username=self.user,key_filename=self.key_path, timeout=5,banner_timeout=5,auth_timeout=5)
                print("[+]SSH Connection to Kali VM is Successfull.")
            
            except(NoValidConnectionsError, SSHException, AuthenticationException,
                    BadHostKeyException, TimeoutError) as e:
                print(f"[!]SSH Connection to remote host failed:{e}")
                return None,None
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            ssh.close()
            return output, error