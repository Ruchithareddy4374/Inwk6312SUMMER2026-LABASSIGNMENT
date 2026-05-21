from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task6.j2")

with open("data-task7.yml") as f:
    interfaces = yaml.safe_load(f)
    print(template.render(interface_list=interfaces))
