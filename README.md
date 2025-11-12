<p align="center">
  <img src="examples/logo.png" width="200" height="200" alt="Siberia" />
</p>

# Volk
Python WSGI server

- `HTTP/1.0` *Ongoing work...*
- `HTTP/1.1` *TODO*



### Install
```bash
pip install volk 
```

### Setup

```python
from volk import Volk

if __name__ == "__main__":
    volk = Volk(wsgi_application=app)
    volk.serve() 
```