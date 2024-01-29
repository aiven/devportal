# 🔒 Former Aiven Documentation

> [!IMPORTANT]  
> This repository used to be the main documentation of Aiven.
>
> The content has been migrated to https://github.com/aiven/aiven-docs.

## Building the docs

1. We recommend using a [virtual environment](https://docs.python.org/3/library/venv.html):

   ```bash
   python3 -m venv venv
   ```

1. Activate your virtual environment:

   ```bash
   source venv/bin/activate
   ```

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Build a local preview:

   ```bash
   make livehtml
   ```

See the output on [http://localhost:8000](http://localhost:8000).
