from dataclasses import dataclass
from typing import List, Dict, Optional

from jinja2 import Environment, FileSystemLoader


@dataclass
class Dataset:
    name: str
    example: Dict
    path: Optional[str] = None


@dataclass
class Task:
    name: str
    datasets: List[Dataset]


TASKS = [
    Task(name='multidocNFQA', datasets=[
        Dataset(name='step_answer', example={}),
        Dataset(name='passage_answeer',
                example={
                    'wikihow_article_id': 56853,
                    'question': 'How To Develop Good Study Habits for College',
                    'target_manual_summary': "To develop good study habits for college, find a quiet, dedicated space and create a consistent study schedule for yourself. Make sure you have everything you need to study at your space and eliminate all distractions, like your smartphone, while you're reviewing your materials. Figure out what topics are most pressing before each study session and try to tackle the hardest stuff first to make the most efficient use of your time. For tips on forming an effective study group with your classmates, read on!",
                    'external_urls': {
                        'http://web.archive.org/web/20211127094354/https://psychcentral.com/lib/top-10-most-effective-study-habits': '10 Highly Effective Study Habits',
                        'http://web.archive.org/web/20210413140406/https://www.ecpi.edu/blog/top-10-effective-study-habits-college-students': 'Top 10 Effective Study Habits for College Students | ECPI University',
                        'http://web.archive.org/web/20201027212737/https://psychcentral.com/lib/top-10-most-effective-study-habits/2/': '10 Highly Effective Study Habits - Part 2',
                        'http://web.archive.org/web/20210306051740/http://centuracollege.edu/blog/10-effective-study-habits-for-college-students/': '10 Effective Study Habits for College Students Centura College Blog',
                        'http://web.archive.org/web/20211201175907/https://www.educationcorner.com/habits-of-successful-students.html': 'Study Habits of Highly Effective Students'}
                }),
    ])
]

HTML_TEMPLATES = ['dataset', 'explore', 'download']


def generate():
    # Render html file
    env = Environment(loader=FileSystemLoader('templates'))

    for i, task in enumerate(TASKS):
        htmls = []
        for j, dataset in enumerate(task.datasets):
            for html_file in HTML_TEMPLATES:
                if i == 0 and j == 0 and html_file == 'dataset':
                    html_file = 'index.html'
                else:
                    html_file = f'{html_file}_task{i + 1}_dataset{j + 1}.html'

                template = env.get_template(html_file)
                active_task_html = {
                    f'active_task{k + 1}': "active" if k == i else "" for k in range(len(TASKS))}

                active_dataset_html = {
                    f'active_task_dataset{k + 1}': "active" if k == j else "" for k in range(len(task.datasets))}

                output_from_parsed_template = template.render(
                    **{**{'html_file': html_file}, **active_task_html, **active_dataset_html, **dataset.example})

                with open(html_file, "w") as f:
                    f.write(output_from_parsed_template)

                htmls.append(html_file)

        if htmls:
            print(f"Generated {','.join(htmls)} for {task.name}")


if __name__ == '__main__':
    generate()
