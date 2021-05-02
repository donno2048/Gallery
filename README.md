# Gallery

A simple gallery for android

## Install requirements (run)

```sh
sudo apt update
sudo apt install -y python3-pip
pip3 install kivy
```

## Run

```sh
python3 main.py
```

## Install requirements (build)

```sh
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential libstdc++6 aidl
pip3 install --user --upgrade Cython==0.29.19 virtualenv buildozer setuptools
```

## Build apk

```sh
buildozer android release
```
