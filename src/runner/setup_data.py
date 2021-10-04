from ..common.data import downloader
from .. import constant


def main():
    downloader.download_cifar_10(constant.PATH_TO_DATA_RAW)


if __name__ == '__main__':
    main()
