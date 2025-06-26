import typer

from template_project_name.utils.helper import get_version_from_installed

app = typer.Typer()


@app.command()
def version():
    print(f"v{get_version_from_installed('template_project_name')}")
