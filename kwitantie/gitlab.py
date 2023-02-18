import os
import base64
import gitlab


def commit_file(kwitantie):
    gl = gitlab.Gitlab('https://gitlab.com', job_token=os.environ['CI_JOB_TOKEN'])
    gl.auth()

    data = {
        'branch': 'main',
        'commit_message': 'new kwitantie added',
        'actions': [
            {
                # Binary files need to be base64 encoded
                'action': 'create',
                'file_path': 'kwitanties/kwitantie-%s.pdf' % kwitantie.kwitantienummer,
                'content': base64.b64encode(open('kwitanties/kwitantie-%s.pdf' % kwitantie.kwitantienummer).read()),
                'encoding': 'base64',
            }
        ]
    }

    project = gl.projects.get(1)
    commit = project.commits.create(data)
