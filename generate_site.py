from jinja2 import Environment, FileSystemLoader

TASK_HTMLS = {
    'task1': ['index.html', 'exploretask1.html']
}

def generate():
    # Render html file
    env = Environment(loader=FileSystemLoader('templates'))

    for task, filenames in TASK_HTMLS.items():
        for filename in filenames:
            template = env.get_template(filename)
            output_from_parsed_template = template.render()

            with open(filename, "w") as f:
                f.write(output_from_parsed_template)

        print(f"Generated {','.join(filenames)} for {task}")


if __name__ == '__main__':
    generate()
