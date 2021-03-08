# function I want to run when I execute module3.py

def local_run():
    print("I am running a local function when I execute it")


def import_run(a, b):
    print("I import this function from other modules")
    return a + b



if __name__ == "__main__":
    print("Execute the script")
    local_run()