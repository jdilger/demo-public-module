# src/my_module/core.py
class Processor:
    def __init__(self, name: str):
        self.name = name
    
    def process(self, data: str) -> str:
        return f"Processed {data} for {self.name}"

    def get_status(self) -> str:
        return f"Ready for {self.name}"
    
def print_aok():
    print("AOK")
