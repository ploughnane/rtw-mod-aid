import argparse  
parser = argparse.ArgumentParser(description='Command Line to aid modding Rome Total War Remastered')  
parser.add_argument('--list_units', type=str, help='Lists units in Mod')  
args = parser.parse_args()  
print(f'Hello, {args.name}!')     