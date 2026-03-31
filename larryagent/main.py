import typer
from larryagent.commands.init import init as init_command
from larryagent.commands.run import run as run_command

app = typer.Typer(help="LarryAgent CLI")

@app.callback()
def main():
    """LarryAgent CLI"""
    pass

@app.command("init")
def init():
    """Scaffold aidelivery and Copilot-friendly files into the current project."""
    init_command()

@app.command("run")
def run(requirement_file: str = "requirement.md"):
    """Run the demo delivery flow for a requirement file."""
    run_command(requirement_file)

if __name__ == "__main__":
    app()
