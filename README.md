<p align="center">
  <img src="examples/logo.png" width="200" height="200" alt="Siberia" />
</p>

# Volk
Python WSGI server

- `HTTP/1.0` *Ongoing work...*
- `HTTP/1.1` *TODO*
- Run from CLI *TODO*
- Workers *TODO*
- Threads *TODO*


### Install
```bash
pip install volk 
```

### Setup

```python
from flask import Flask  # Or any other WSGI application framework
from volk import Volk

flask_app = Flask(__name__)

if __name__ == "__main__":
    volk = Volk(wsgi_application=flask_app)
    volk.serve() 
```