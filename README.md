# Manage linux users with Ansible

## Prerequisites

This set of playbooks and scripts needs you to use the "users" YAML dictionary in the `params.yml` file, which will be used to manage users on one or more linux servers.

Here is a pretty simple example for dictionary fill :

```YAML
users:
- name: foo
  email: foo@foo.bar
  shell: /bin/bash
  state: present
```

## How to use the set

```bash
ansible-playbook global.yml -i inventories/production
```
Or
```bash
ansible-playbook global.yml -i inventories/production -u ssh_username -k -K
 ```
