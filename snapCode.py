from lxml import etree
from io import StringIO
import sys


def readFile():
  with open('pom.xml', 'r') as xml_file:
        return(xml_file.read())

def writeFile(updateVersion):
  with open('pom.xml','w') as newFile:
    newFile.write(updateVersion)

def replaceFormat(checkFile):
     print(' Snapshot Found...\n')
     newVersion = checkFile.replace('SNAPSHOT','ci_Team_Foo_Bar-SNAPSHOT')
     writeFile(newVersion)
     print(readFile())
    

def formatValidate():
    xml_to_check = readFile()
    try:
        etree.parse(StringIO(xml_to_check))
        print('\n XML well formed, syntax ok.\n')
        if '1.0-SNAPSHOT' in xml_to_check:
            replaceFormat(xml_to_check)
        else:
            print(" Old Snapshot Version Format Not Found.")

# check for file IO error
    except IOError:
        print('Invalid File')

# check for XML syntax errors
    except etree.XMLSyntaxError as err:
        print('XML Syntax Error, see error_syntax.log')
        with open('error_syntax.log', 'w') as error_log_file:
          error_log_file.write(str(err.error_log))
        quit()

    except:
        print('Unknown error, exiting.')
        quit()


def main():
    formatValidate()

if __name__ == '__main__':
   main()
