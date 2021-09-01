import getopt
import sys

from colorama import Fore
from models.mle.Mle import Mle
from models.leakgan.Leakgan import Leakgan
from models.maligan_basic.Maligan import Maligan
from models.rankgan.Rankgan import Rankgan
from models.seqgan.Seqgan import Seqgan

#import nltk
#nltk.download('punkt')

def set_gan(gan_name):
    gans = dict()
    gans['seqgan'] = Seqgan
    gans['leakgan'] = Leakgan
    gans['rankgan'] = Rankgan
    gans['maligan'] = Maligan
    gans['mle'] = Mle
    try:
        Gan = gans[gan_name.lower()]
        gan = Gan()
        gan.vocab_size = 5000
        gan.generate_num = 10000
        return gan
    except KeyError:
        print(Fore.RED + 'Unsupported GAN type: ' + gan_name + Fore.RESET)
        sys.exit(-2)



def set_training(gan, training_method):
    gan_func = gan.train_real
    return gan_func


def parse_cmd(argv):
    opts, args = getopt.getopt(argv, "hg:t:d:")
    opt_arg = dict(opts)
    gan = set_gan(opt_arg['-g'])# set_gan('seqgan')
    print("*********************************")
    print(opt_arg['-g'])
    print("*********************************")
    gan_func = set_training(gan, 'real')
    #gan_func('data/naratives.txt')
    gan_func('data/naratives_rwords.txt')

if __name__ == '__main__':
    gan = None
    parse_cmd(sys.argv[1:])
