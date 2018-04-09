import json
import sys, getopt


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'name_script.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   json_data=open(inputfile).read()
   data=json.loads(json_data)

   name, sep, tail = inputfile.partition('.')
   for x in data:
      x['account_name'] = 'narendramodi'
   with open(outputfile, 'w') as f:
      f.write(json.dumps(data))


if __name__ == "__main__":
   main(sys.argv[1:])
