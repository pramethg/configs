import os
import argparse

def argparser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--file", type = str)
  parser.add_argument("--dir", action = 'store_true')
  parser.add_argument("--ext", type = str, default = 'py')
  return parser.parse_args()

def convert(fpath):
  with open(f"./{fpath}", 'r') as file:
    content = file.read()
  modified = content.replace('    ', '  ')
  with open(f"./{fpath}", 'w') as file:
    file.write(modified)

if __name__ == "__main__":
  args = argparser()
  if args.dir:
    if args.file[-1] == '/':
      args.file = args.file[:-1]
    fdir = [file for file in os.listdir(f'./{args.file}') if file.endswith(args.ext)]
    for fpath in fdir:
      convert(f'./{args.file}/{fpath}')
  else:
    convert(f'./{args.file}')
