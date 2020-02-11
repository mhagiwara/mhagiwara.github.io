import codecs
import glob

from jinja2 import Environment, FileSystemLoader
import markdown2
import simplejson as json


CONTENTS_DIR = 'content'


def get_content_files():
    for filename in glob.glob('%s/*.md' % CONTENTS_DIR):
        yield filename


def read_content_file(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        page = json.loads(next(f))
        page['body'] = f.read()

    return page


def main():
    env = Environment(loader=FileSystemLoader('templates'))

    for filename in get_content_files():
        page = read_content_file(filename)

        body = markdown2.markdown(page['body'])
        template = env.get_template(page['template'])

        with codecs.open(page['url'], mode='w', encoding='utf-8') as outfile:
            outfile.write(template.render(
                body=body,
                title=page['title'],
                url=page['url'],
                description=page.get('description'),
                image=page.get('image')))


if __name__ == '__main__':
    main()
