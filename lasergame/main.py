from lasergame.procedures.gameloop import gameloop

def main():
    gameloop()


# This is needed, or else calling `python -m <name>` will mean that main() is called twice.
if __name__ == "__main__":
    main()
