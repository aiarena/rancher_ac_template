import subprocess
import os
import re


def run():
    subprocess.check_call("kubectl kustomize ./deployment > bulk.yaml", shell=True)
    subprocess.check_call("kubesplit -i bulk.yaml -o ./outputyaml", shell=True)
    print("Done")


if __name__ == '__main__':
    run()