from __future__ import annotations


from typing import List, Dict, Any, Optional

from rich.console import Console
class Application:
    
    
    
    def __init__(self) -> None:
        # init the rich console
        self.console = Console()    
        

    def starting(self, console: Console) -> None:
        
        console.print("Starting Breachr")
        
        
        
        console.print("Loading configuration")
        console.print("Loading plugins")
        console.print("Loading data")
        console.print("Starting plugins")
        console.print("Starting data")
        console.print("Breachr started")

