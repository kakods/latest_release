#!/usr/bin/env python3
import requests,fire

def get_latest_version(repo):
    response = requests.get(f'https://api.github.com/repos/{repo}/releases/latest')
    return response.json()['tag_name']

if __name__=='__main__':
    fire.Fire(get_latest_version)
