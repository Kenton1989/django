import importlib
import sys
import pkgutil
import traceback


def _main():
    if len(sys.argv) <= 1:
        scan_package('django.dispatch')
    else:
        scan_package(sys.argv[1])

    modules = [(k, v) for k, v in sys.modules.items() if k.startswith('django')]
    modules.sort()
    for name, path in modules:
        print(name, sep='\t')


def scan_package(name: str):
    print('scanning:', name)
    module = importlib.import_module(name)
    try:
        children = [name for _, name, _ in pkgutil.walk_packages(module.__path__)]
    except AttributeError:
        return
    for ch_name in children:
        try:
            importlib.import_module(f'{name}.{ch_name}')
        except Exception as e:
            print(e)
            # traceback.print_exc()


if __name__ == '__main__':
    _main()
