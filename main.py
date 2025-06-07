import sys

def run_cli():
    import cli
    cli.run()

def run_api():
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        run_cli()
    else:
        run_api()
