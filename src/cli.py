import argparse

def setup_parser():
    parser = argparse.ArgumentParser(
            prog="wiki-fetch",
            description="Wiki-fetch is a wikipedia search engine that fetches article titles from wikipedia",
            epilog="Thank you for supporting this project")

    parser.add_argument("topic", action="store")
        
    return parser

def parse(parser):
    args = parser.parse_args()

    return args 
        

