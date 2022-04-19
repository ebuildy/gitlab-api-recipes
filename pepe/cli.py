from typing import Optional

import typer
import logging

from pepe import __app_name__, __version__

from .commands.projects_gitops import pepe_commands_projects_gitops
from .commands.projects_runners_tags import pepe_commands_projects_runners

app = typer.Typer()

@app.command()
def gitops_projects():
    pepe_commands_projects_gitops()
    
@app.command()
def projects_runners():
    pepe_commands_projects_runners()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

def _log_level_callback(value: str) -> None:
    if value:
        level = {
            "debug" : logging.DEBUG,
            "info" : logging.INFO,
            "warn" : logging.WARN,
            "warning" : logging.WARN,
            "err" : logging.ERROR,
            "error" : logging.ERROR
        }[value]
        
        logging.basicConfig(level=level)

@app.callback()
def main(
    log_level: Optional[str] = typer.Option(
        None,
        "--log",
        "-l",
        help="debug / info / warn / error",
        callback=_log_level_callback
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return