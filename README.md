# Flask

**Flask** is a Python [micro framework](https://flask.palletsprojects.com/en/3.0.x/) for building web applications.

## Local Development

### Requirements

 * `terminal`
 * `git`
 * `python3`

### How get this running

* Clone this repository
* Change directory
* Create new [`virtualenv`](https://virtualenv.pypa.io/en/latest/)
* [Activate](https://pip.pypa.io/en/stable/cli/pip_install/#options) `virtualenv`
* [Install](https://pip.pypa.io/en/stable/cli/pip_install/#options) required Python packages (into the `virtualenv`)
* Run `Flask` application
* Access service via `HTTP`
* Fun&Freizeit

## Examples

### Windows

```shell
git clone https://github.com/cbwham/training-flask.git
cd training-flask
python -m venv .venv
.venv\Scripts\activate.bat
pip install -U -r requirements.txt
flask run
```

### Linux, MacOS

Just the activation of the virutalenv is different:

```shell
. .venv/bin/activate # https://linuxize.com/post/
```

