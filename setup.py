from setuptools import setup

setup(  
        name = 'LANfactory',
        version='0.3.0dev',
        author = 'Alexander Fenger',
        url = 'https://github.com/AlexanderFengler/LANfactory',
        packages= ['lanfactory', 'lanfactory.config', 'lanfactory.trainers', 'lanfactory.utils'], # , 'ssms.basic_simulators', 'ssms.config', 'ssms.dataset_generators', 'ssms.support_utils'],
        description='Package with convenience functions to train LANs',
        install_requires=['NumPy >= 1.17.0', 'SciPy >= 1.6.3', 'pandas >= 1.2.4', 'torch >= 1.7', 'jax >= 0.4.2', 'flax >= 0.6.4', 'optax >= 0.1.4', 'tqdm >= 4.0.0', 'onnx >= 1.13.1', 'argparse>=1.1'],
        setup_requires=['NumPy >= 1.17.0', 'SciPy >= 1.6.3', 'pandas >= 1.2.4', 'torch >= 1.7', 'jax >= 0.4.2', 'flax >= 0.6.4', 'optax >= 0.1.4', 'tqdm >= 4.0.0', 'onnx >= 1.13.1', 'argparse>=1.1'],
        classifiers=['Development Status :: 1 - Planning',
                      'Environment :: Console',
                      'License :: OSI Approved :: MIT License',
                      'Programming Language :: Python',
                      'Topic :: Scientific/Engineering'
                    ]
    )