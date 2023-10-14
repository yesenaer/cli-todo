![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# cli-todo

CLI tool to track to-do lists and items.

## setup
- clone the repo
- (suggested) create a virtual environment
- install the dependencies using `pip install .`
    - or include optional dependencies `pip install .[test]` 

## test
- run `pytest .` from root of repo

## build
- run `pip install -e .` to make the cli tool available in your venv
- run `pip install --upgrade build` and `py build` to create a distribution

## run 
with the cli tool available in venv
- `todo` for the todo cli app
- `cli-example` for the example app build with calmcode.io (includes db submodule)
- `cli-db` for the db app

### example
```
> todo add cheese
> todo show
todo:
x | snacks
  | bread
  | cheese
```

## links
[calmcode.io](https://calmcode.io/typer/introduction.html) -> shout out to calmcode.io for introducing me to typer. <br>
[typer website](https://typer.tiangolo.com/) for official docs on the typer framework.
