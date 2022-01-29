from jinja2 import Environment, FileSystemLoader

TASK_HTMLS = {
    'task1': ['index.html', 'exploretask1.html'],
    'task2': ['task2.html'],
    'task3': [],
    'task4': [],
    'task5': [],
}

EXAMPLES = {
    'task2': {'wikihow_article_id': 56853,
              'question': 'How To Develop Good Study Habits for College',
              'target_manual_summary': "To develop good study habits for college, find a quiet, dedicated space and create a consistent study schedule for yourself. Make sure you have everything you need to study at your space and eliminate all distractions, like your smartphone, while you're reviewing your materials. Figure out what topics are most pressing before each study session and try to tackle the hardest stuff first to make the most efficient use of your time. For tips on forming an effective study group with your classmates, read on!",
              'external_urls': {
                  'http://web.archive.org/web/20211127094354/https://psychcentral.com/lib/top-10-most-effective-study-habits': '10 Highly Effective Study Habits',
                  'http://web.archive.org/web/20210413140406/https://www.ecpi.edu/blog/top-10-effective-study-habits-college-students': 'Top 10 Effective Study Habits for College Students | ECPI University',
                  'http://web.archive.org/web/20201027212737/https://psychcentral.com/lib/top-10-most-effective-study-habits/2/': '10 Highly Effective Study Habits - Part 2',
                  'http://web.archive.org/web/20210306051740/http://centuracollege.edu/blog/10-effective-study-habits-for-college-students/': '10 Effective Study Habits for College Students Centura College Blog',
                  'http://web.archive.org/web/20211201175907/https://www.educationcorner.com/habits-of-successful-students.html': 'Study Habits of Highly Effective Students'}
              }
}


def generate():
    # Render html file
    env = Environment(loader=FileSystemLoader('templates'))

    for task, filenames in TASK_HTMLS.items():
        for filename in filenames:
            template = env.get_template(filename)

            active_task_html = {f'active_{task_name}': "active" if task_name == task else ""
                                for task_name in TASK_HTMLS}

            output_from_parsed_template = template.render(**{**active_task_html, **EXAMPLES.get(task, {})})

            with open(filename, "w") as f:
                f.write(output_from_parsed_template)
        if filenames:
            print(f"Generated {','.join(filenames)} for {task}")


if __name__ == '__main__':
    generate()
