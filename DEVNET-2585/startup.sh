#!/bin/bash

#!/usr/bin/env bash

echo
echo ***Stopping All Other Virtual Box Instances***
echo
vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate

echo
echo ***Setting Ansible Environment Variables***
echo

export ANSIBLE_PARAMIKO_LOOK_FOR_KEYS=False
export ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD=True

echo
echo ***SETTING BASH PROMPT***
echo

export PS1='\W$ '

echo
echo ***CREATING VIRTUAL ENVIRONMENT***
echo
virtualenv venv --python=python3

echo
echo ***STARTING VIRTUAL ENVIRONMENT***
echo
source ./venv/bin/activate

echo
echo ***INSTALLING REQUIREMENTS***
echo
pip install -r code/requirements.txt

echo
echo ***STARTING VAGRANT***
echo

vagrant up

echo
echo ***Opening up the Task List***
echo

open tasklist.txt

echo ***THE STARTUP SCRIPT IS COMPLETE.***