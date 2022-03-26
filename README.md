# BruteZ

This project is designed to send a brute force range of number combinations of length N as keyboard input.


## Setup

Essentially we just need to set up virtualenv and PIP dependencies and run `main.py`

Virtual Environment setup:
[Windows Guide](https://www.educative.io/edpresso/how-to-activate-virtualenv-windows)
```bash
# Install
pip install virtualenv
cd project_path
# Activate
virtualenv env
./venv/scripts/activate # Unix only. Windows path is different.
```

## Running

Once the script is executed, it will enter an infinite wait as it watches for control hotkeys to be pressed. 

| Hotkey  | Effect                                          |
|---------|-------------------------------------------------|
| `home`  | Initiates typing of many numbers.               |
| `pause` | Hold for a couple seconds to terminate program. |

The `WAIT_TIME_SECONDS` variable controls the time between combo outputs. A value of `0` will type out continuously without pausing.  

Ensure that your cursor is in the correct window when starting this script, otherwise you may get strange behavior out of applications getting too much input.  