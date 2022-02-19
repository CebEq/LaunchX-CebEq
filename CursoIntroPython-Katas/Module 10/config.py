def main():
    try:
        configuration = open('config.txt')
    # except OSError as err:
    #     if err.errno == 2:
    #         print("Couldn't find the config.txt file!")
    #     elif err.errno == 13:
    #         print("Found config.txt but couldn't read it")
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!")
        print("Got a problem trying to read the file:", err)
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError as err:
        print("Found config.txt but couldn't read it:", err)
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()