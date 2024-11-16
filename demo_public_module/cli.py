from demo_public_module.main import Processor

__version__ = "0.1.0"
__all__ = ["Processor"]

# src/my_module/cli.py
import typer
from typing import Optional
from rich import print

app = typer.Typer()

@app.command()
def process(
    data: str = typer.Argument(..., help="Data to process"),
    name: Optional[str] = typer.Option("default", help="Name for the processor")
) -> None:
    """Process data using the module's core functionality"""
    processor = Processor(name)
    result = processor.process(data)
    print(f"[bold green]{result}[/bold green]")

@app.command()
def status(name: str = typer.Option("default", help="Name to check status for")) -> None:
    """Check processor status"""
    processor = Processor(name)
    status = processor.get_status()
    print(f"[bold blue]{status}[/bold blue]")

if __name__ == "__main__":
    app()