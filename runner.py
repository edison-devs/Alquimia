from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent))

from settings import engine
from commands import commands

def run(command):
    try:
        with engine.connect():
            commands[command]()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        try:
            with engine.connect():
                pass
        except Exception as e:
            print(f"Error de conexión: {e}")
            sys.exit(1)
    elif sys.argv[1] in commands:
        run(sys.argv[1])
    else:
        print("Uso: python main.py <comando>")
        print(f"Comandos disponibles: {', '.join(commands)}")
        sys.exit(1)
