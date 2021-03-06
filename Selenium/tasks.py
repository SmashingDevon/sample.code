import os
import sys

from datetime import datetime
from invoke import task


## KEWL STUFF
def color(code):
    '''A simple ANSI color wrapper factory'''
    return lambda t: '\033[{0}{1}\033[0;m'.format(code, t)


green = color('1;32m')
red = color('1;31m')
blue = color('1;30m')
cyan = color('1;36m')
purple = color('1;35m')
white = color('1;39m')


def header(text):
    '''Display an header'''
    print(' '.join((blue('>>'), cyan(text))))
    sys.stdout.flush()


def info(text, *args, **kwargs):
    '''Display informations'''
    text = text.format(*args, **kwargs)
    print(' '.join((purple('>>>'), text)))
    sys.stdout.flush()


def success(text):
    '''Display a success message'''
    print(' '.join((green('>>'), white(text))))
    sys.stdout.flush()


def error(text):
    '''Display an error message'''
    print(red('✘ {0}'.format(text)))
    sys.stdout.flush()


def exit(text=None, code=-1):
    if text:
        error(text)
    sys.exit(-1)


def build_args(*args):
    return ' '.join(a for a in args if a)
## KEWL STUFF

## STATIC DATA
CLEAN_PATTERNS = [
#    '**/*.pyc',
    '__pycache__',
    '**/__pycache__',
    '**/**/__pycache__',
#    'build',
#    'dist',
#    'cover',
#    'docs/_build',
#    '.tox',
#    'reports',
    '*.egg-info',
    '.benchmarks',
    '.cache',
    '.pytest_cache',
]

MS_PRJ_SKEL_DIRS = [
    'service',
    'data',
#    'api/dat',
#    'api/svc',
#    'api/mod',
#    'static',
#    'templates',
#    'cli',
#    'bi',
#    'mi',
]

MS_PRJ_SKEL_FILES = [
    'service/__init__.py',
    'data/__init__.py',
]

ROOT = os.path.dirname(__file__)
SERVICE = os.path.dirname(__file__) + '/' + MS_PRJ_SKEL_DIRS[0] + '/'
MODEL = os.path.dirname(__file__) + '/' + MS_PRJ_SKEL_DIRS[1] + '/'

DOCKER_IMAGE_LABEL_NEO4J = 'neo4j-localhost'
DOCKER_IMAGE_LABEL_COUCHBASE = 'couchbase-localhost'

## STATIC DATA

@task
def init(ctx):
    '''Initialize Project'''
    header(init.__doc__)
    with ctx.cd(ROOT):
        for pattern in MS_PRJ_SKEL_DIRS:
           info('Creating {0}', pattern)
           try:
              ctx.run('mkdir {0}'.format(pattern))
           except Exception:
              print ("Error creating dir {0}".format(pattern))
        for pattern in MS_PRJ_SKEL_FILES:
           info('Creating {0}', pattern)
           try:
              ctx.run('touch {0}'.format(pattern))
           except Exception:
              print ("Error creating file {0}".format(pattern))

@task
def deps(ctx):
    '''Install or update development dependencies'''
    header(deps.__doc__)
    ctx.run('/usr/local/bin/pip3 install -r requirements.txt', pty=True)

@task
def test(ctx):
    '''Test Project'''
    header(test.__doc__)
    ctx.run('pytest test.py', pty=True)

@task
def test_verbose(ctx):
    '''Test Project'''
    header(test_verbose.__doc__)
    ctx.run('pytest test.py -s', pty=True)

#@task(clean, deps, test, doc, qa, assets, dist, default=True)
@task(test, default=True)
def all(ctx):
    '''Run default Project Tasks'''
    header(all.__doc__)
    pass
