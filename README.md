# Flask sample project to ask google Speech to Text

This is sample project to host Flask with swagger and ask Speech to Text using DeepSpeech-Keras

## Thanks

- [Swagger](https://swagger.io/tools/swagger-ui/)
- [Docs](https://python101.readthedocs.io/pl/latest/webflask/)
- [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/quickstart.html#a-minimal-api)
- [Visual Studio Code Tutorial](https://code.visualstudio.com/docs/python/tutorial-flask)
- [DeepSpeech-Keras](https://github.com/rolczynski/Synthetic-Boosted-DeepSpeech/blob/master/README.md)

## Useful commands

### Python

- check Python version

```powershell
python --version
```

- update pip

```powershell
python -m pip install --upgrade pip
```

- instal requirements

```powershell
pip install -r [FILE_NAME]
```

- - examples

```powershell
pip install -r requirements.txt
```

- add virtual enviroment

```powershell
py -m venv env
```

- activate virtual enviroment

```powershell
.\env\Scripts\activate
```

- deactivate virtual enviroment

```powershell
deactivate
```

- check virtual enviroment

```powershell
where python
```

### Visual Studio Code

- Python: Select Interpreter

```code
Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter.
Select virtual environment. `./env/...` or `.\env\...`
```

### Docker

- check the docker version

```powershell
docker -v
```

- show any running containers

```powershell
docker ps
```

- kill docker container

```powershell
docker kill [CONTAINER_ID]
```

- show docker not running containers

```powershell
docker images
```

- clear all local docker stuff

```powershell
docker system prune -a
```

- Build docker images

```powershell
docker build -t [DOCKER_IMAGE_NAME]:[TAG] .
```

- - example

```powershell
docker build -t speechmatics_s2t:latest .
```

- Run docker images

```powershell
docker run -d -p [PORT_ON_HOST]:[PORT_ON_DOCKER_NETWORK] [DOCKER_IMAGE_NAME]:[TAG]
```

- - example

```powershell
docker run -d -p 5000:5000 speechmatics_s2t:latest
```

### Conda enviroments

You can use pip (not prepared yet):

```bash
pip install deepspeech-keras
```

Otherwise clone the code and create a new environment via [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#):

```bash
conda env create -f=environment.yml     # or use: environment-gpu.yml
conda activate SpeechToText_DeepSpeech
```
