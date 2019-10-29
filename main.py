import argparse
from modules import annotate, metrics

parser = argparse.ArgumentParser(description="Entity Linker")
parser.add_argument("--mode", choices=["annotate", "metrics"], help="Choose between the operating modes")
parser.add_argument("--csv", type=str, help="Filepath for the CSV to annotate")
parser.add_argument("--url", type=str, help="URL of the linker endpoint")
args = parser.parse_args()


def main(args):
    """Launches the chosen running mode according to the passed parameters

    Arguments:
        args {parsed args} -- The parsed arguments
    """
    if args.mode == "annotate":
        annotate.annotate(args.csv, args.url)
    if args.mode == "metrics":
        metrics.metrics(args.url)


if __name__ == "__main__":
    main(args)
