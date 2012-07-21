# coding=utf-8
import argparse
from drawing import drawing

parser = argparse.ArgumentParser(description=u"Aplica efeito de desenho a lápis em foto.")
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("foto", type=str, help=u"Nome da foto que será transformada. Ex.: foto.jpg")
parser.add_argument("desenho", type=str, help=u"Nome da foto depois de transformada. Ex.: desenho.jpg")
parser.add_argument("--blur", type=int, default=25, dest="blur", help=u"Configura o valor da desfocagem. Ex.: 25")
parser.add_argument("--alpha", type=float, default=1.0, dest="alpha", help=u"Configura o valor da transparencia. Ex.: 0.5 para 50% de transparencia")

args = parser.parse_args()

drawing(args.foto, args.desenho, blur=args.blur, alpha=args.alpha)

if args.quiet:
    pass

elif args.verbose:
    print "A imagem {0} foi convertida para {1}".format(args.foto, args.desenho)
    print "Com blur: {0} e alpha: {1}".format(args.blur, args.alpha)

else:
    print "{0} -> {1}".format(args.foto, args.desenho)
