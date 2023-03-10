import logging
import argparse

from example.foo import Foo
from example.celcius import Celsius


# the main function could be called from somewhere else
def main(args):
    logging.info("str param: {}".format(args.str_param))
    logging.info("bool param: {}".format(args.bool_param))
    logging.info("int param: {}".format(args.int_param))
    logging.info("float param: {}".format(args.float_param))
    logging.error("verbose: {}".format(args.verbose))
    logging.warning("this is a warning")

    foo = Foo()
    logging.info(foo.private_variable)

    temp = Celsius(37)
    temp.temperature = -30
    logging.info(temp.to_fahrenheit())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # examples
    parser.add_argument("--str_param", type=str, required=True)
    parser.add_argument("--bool_param", action="store_true", default=False)
    parser.add_argument("--int_param", type=int, default=5)
    parser.add_argument("--float_param", type=float, default=2.5)
    parser.add_argument("--verbose", action="store_true", default=False)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    main(args)
