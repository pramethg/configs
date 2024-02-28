import os
import argparse

def argparser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--file", type = str)
  parser.add_argument("--dir", action = 'store_true')
  parser.add_argument("--ext", type = str, default = 'py')
  return parser.parse_args()

def convert(fpath):
  with open(fpath, 'r') as file:
    content = file.read()
  modified = content.replace('    ', '  ')
  with open(fpath, 'w') as file:
    file.write(modified)

if __name__ == "__main__":
  args = argparser()
  if args.dir:
    if args.file[-1] == '/':
      args.file = args.file[:-1]
    for dirpath, dirnames, filenames in os.walk(args.file):
      for filename in filenames:
        if filename.endswith(args.ext):
          convert(os.path.join(dirpath, filename))
  else:
    convert(args.file)