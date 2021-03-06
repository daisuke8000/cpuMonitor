# CPU Monitor
Monitor CPU resources

* CPU Performance
* Memory Volume

## application image

![cpumonitor-images](https://user-images.githubusercontent.com/55035595/150790159-34fbfbbe-d233-4cdd-9f6b-28209534ef38.png)

## how to use

1. create environment
```bash
python -m venv .venv
```

2. activate environment
```bash
source .venv/bin/activate
```

3. library managements
```bash
pip install -r requirements.txt
```

4. start monitor
```bash
python main.py
```

## application packaging

* pip install [pyinstaller](https://github.com/pyinstaller/pyinstaller/blob/fcff15e6e7ab6fad135c584c2b6cc5e0f7809319/doc/index.rst)
```bash
pip install pyinstaller
```
* in dist main.pkg
```bash
pyinstaller main.py --onefile
```
