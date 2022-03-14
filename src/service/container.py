import os

import docker

from util.config import get_config

DOCKER_CLIENT = docker.DockerClient(base_url='unix://var/run/docker.sock')
RUNNING = 'running'


class Container(object):
    """
    docker container 관리
    """

    @staticmethod
    def run(container_type):
        """
        Run container
        Available container types : mysql, elasticsearch, kibana
        :param container_type: the container type to run
        :type container_type: str
        :returns: whether the container is running
        :rtype: bool
        """

        # Read config yaml
        config = get_config(container_type)
        container_name = config.get("container_name")

        # Run the container
        docker_run_command = {
            "mysql":
                f'''
                docker run \
                --detach \
                --env MYSQL_ROOT_PASSWORD="{config.get("root_password")}" \
                --env MYSQL_USER="{config.get("user")}"  \
                --env MYSQL_PASSWORD="{config.get("password")}" \
                --env MYSQL_DATABASE="{config.get("database")}" \
                --name "{config.get("container_name")}" \
                --publish {config.get("port")}:3306 \
                {config.get("image_version")}
                ''',
            "elasticsearch":
                f'''
                docker run \
                --detach \
                --publish 9200:9200 \
                --env discovery.type=single-node \
                --name {config.get("container_name")} \
                {config.get("image_version")}
                ''',
            "logstash": "",
            "kibana": f'''
                docker run \
                --detach \
                --publish 5601:5601 \
                --link elasticsearch:elasticsearch \
                --name {config.get("container_name")} \
                {config.get("image_version")}
                ''',
            "flask": ""
        }
        print(docker_run_command.get(container_type))
        os.system(docker_run_command.get(container_type))

        # post-processes
        post_processes = {
            "elasticsearch": f'''
            docker exec --detach {config.get("container_name")} elasticsearch-plugin install analysis-nori; \
            docker restart {config.get("container_name")}
            '''
        }
        post_process = post_processes.get(container_type)
        if callable(post_process):
            post_process()
        elif isinstance(post_process, str):
            os.system(post_process)

        # Check the container status
        is_running = Container.is_running(container_name)
        return is_running

    @staticmethod
    def is_running(container_name):
        """Check the container status by container name
        :param container_name: the container name to be checked
        :type container_type: str
        :returns: whether the container is running
        :rtype: bool
        """
        container = DOCKER_CLIENT.containers.get(container_name)
        container_state = container.attrs['State']
        container_is_running = container_state['Status'] == RUNNING
        return container_is_running


if __name__ == '__main__':
    Container.run('mysql')
