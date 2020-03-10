# latest_release
An attempt to get the latest release version of any repo.

## prerequisites
Ensure that you have python>=3.6.9.<br/>
Clone this repo and run `pip install -r requirements.txt` from the repo root, provided that pip is from python>=3.6.9 :)

## usage
```
python3 get_latest_release.py --repo=<repo_name>
```
### example
```
python3 get_latest_release.py --repo=kubernetes/minikube
```
displayed
```
v1.8.1
```
at the time this was written.
