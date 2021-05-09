import argparse
import os

# Create the parser
parser = argparse.ArgumentParser(description="Start the Hola Mundo Bot project")

# Create the parser and the arguments
parser.add_argument(
    "--deps", action="store_true", help="Install all dependencies from Pipfile"
)
parser.add_argument(
    "--start", action="store_true", help="Start the bot and run with the token"
)
parser.add_argument(
    "--format", action="store_true", help="Format the file with Black and Flake8"
)
parser.add_argument(
    "--version", action="store_true", help="Show the version from this utilitie"
)

# Parse the args
args = parser.parse_args()

# Validate the args
if args.deps:
    print("Creating a virtual env..")
    os.system("pipenv shell")
    print("Sync all dependencies :)")
    os.system("pipenv sync --dev")
elif args.start:
    print("Running the bot...")
    os.system("python src/main.py")
elif args.format:
    print("Formating the files..")
    os.system("pipenv run format")
    print("Linting the files..")
elif args.version:
    print("1.0 Get start util")
