import argparse

from src.service.container import Container


def main(args_dict):
    container_type = args_dict.get('type')
    is_running = Container.run(container_type)
    print(f'Container for {container_type} is running: {is_running}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type',
                        type=str,
                        required=True,
                        choices=['mysql', 'elasticsearch', 'kibana'])
    args = parser.parse_args()
    args = vars(args)

    main(args)
