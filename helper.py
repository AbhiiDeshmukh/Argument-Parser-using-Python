import argparse

def get_args():

    parser = argparse.ArgumentParser("Flags supported by the program are: ")

    n_desc = "Your name please"
    pn_desc = "Name of program"
    arg1_desc = "Loc of demo files to be given to script"
    arg2_desc = "Selection parameters: Async('A') or Sync('S')"

    parser.add_argument("-n",help=n_desc)
    parser.add_argument("-pn",help=pn_desc)
    parser.add_argument("-arg1",help=arg1_desc)
    parser.add_argument("-arg2",help=arg2_desc)

    args = parser.parse_args()

    return args

def main():
    args = get_args()
    
    print("Name: ",args.n)
    print("Program: ",args.pn)
    print("Loc of file: ",args.arg1)
    print("Selected parameter: ",args.arg2)


if __name__ == "__main__":
    main()
