from optparse import OptionParser
from dirFind import *
if __name__ == '__main__':
    banner = """
     _ _     _____              
  __| (_)_ _|_   _| __ ___  ___ 
 / _` | | '__|| || '__/ _ \/ _ \\
| (_| | | |   | || | |  __/  __/
 \__,_|_|_|   |_||_|  \___|\___|
                                

    """
    print(banner)
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="base_path",
                          help="dir path", metavar="dir path")
    (options, args) = parser.parse_args()
    if options.base_path is None:
            # 打印提示信息
        parser.print_help()
    else:
        dirFind.dirFind(options.base_path)


