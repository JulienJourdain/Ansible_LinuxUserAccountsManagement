# Manage linux users with Ansible

It has never been easier to deploy local user accounts on linux servers !

## Prerequisites

This set of playbooks and scripts needs you to use the "users" YAML dictionary in the `params.yml` file, which will be used to manage users on one or more linux servers.

Here is a pretty simple example for dictionary fill :

```YAML
users:

- name: foo
  email: foo@foo.bar
  shell: /bin/bash
  state: present

- name: app
  comment: Application user account
  email: bar@foo.bar
  shell: /bin/false
  state: present
```

Users dictionary is based on Ansible's user core module. For my needs, I just included these parameters :

```YAML
- user:
    name: "{{ item.name }}"
    password: "{{ item.encrypted_password|default(omit) }}"
    comment: "{{ item.comment|default(omit) }}"
    uid: "{{ item.uid|default(omit) }}"
    group: "{{ item.group|default(omit) }}"
    groups: "{{ item.groups|default(omit) }}"
    shell: "{{ item.shell|default(omit) }}"
    expires: "{{ epoch_date.stdout|default(omit) }}"
    state: "{{ item.state }}"
```

Feel free to adapt it as you needs ;-)

## How to use the set

```bash
ansible-playbook global.yml -i inventories/production
```
Or
```bash
ansible-playbook global.yml -i inventories/production -u ssh_username -k -K
 ```

NB: For my needs, I had to use expires date but you can delete / ignore it.
