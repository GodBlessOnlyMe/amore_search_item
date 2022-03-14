import argparse

from src.service.container import Container


def main(args_dict):
    container_type = args_dict.get('type')
    if container_type == 'all':
        Container.run_all()
    else:
        is_running = Container.run(container_type)
        print(f'Container for {container_type} is running: {is_running}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type',
                        type=str,
                        required=True,
                        choices=['mysql', 'elasticsearch', 'kibana', 'all'])
    args = parser.parse_args()
    args = vars(args)

    main(args)
