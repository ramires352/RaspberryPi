import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hp:m:")
    except getopt.GetoptError:
        print("arguments.py -p <pin> -m <message>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("arguments.py -p <pin> -m <message>")
            sys.exit()
        elif opt == "-p":
            pino = arg
        elif opt == "-m":
            mensagem = arg
    print(pino, mensagem)

if __name__ == "__main__":
    main(sys.argv[1:])