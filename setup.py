from setuptools import setup, find_packages
import os

version = '2.0.5.dev0'

setup(name='wildcard.media',
      version=version,
      description="HTML5 audio and video integration with plone",
      long_description="%s\n%s" % (
          open("README.rst").read(),
          open(os.path.join("docs", "HISTORY.txt")).read()
      ),
      classifiers=[
          'Framework :: Plone',
          'Framework :: Plone :: 5.2',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation :: CPython'
      ],
      keywords='video audio media plone tiny html5 mediaelement',
      author='Nathan Van Gheem',
      author_email='nathan@vangheem.us',
      url='https://github.com/collective/wildcard.media',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wildcard'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools-git'],
      install_requires=[
          'setuptools',
          'six',
          'plone.transformchain',
          'plone.app.dexterity',
          'plone.autoform',
          'plone.app.textfield',
          'plone.rfc822',
          'plone.supermodel>=1.1',
          'five.globalrequest',
          'plone.api',
          'requests'
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ],
          'youtube': [
              'requests',
              'oauthlib'
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone

      [celery_tasks]
      media = wildcard.media.tasks
      """,
      )
