# Gallery

A simple gallery for android

## Clone the repo

```sh
git clone https://github.com/donno2048/Gallery
cd Gallery
```

## Install requirements (run)

```sh
sudo apt update
sudo apt install -y python3-pip
pip3 install kivy==2.0.0
```

## Run

```sh
python3 main.py
```

## Install requirements (build)

```sh
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential libstdc++6 aidl
pip3 install -r requirements.txt
```

## Build apk

```sh
buildozer android release
```
