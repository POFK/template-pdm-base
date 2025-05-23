import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)
pyproj_cfg = config.get("tool", {}).get("builder-opt", {})
core_modules_path = pyproj_cfg["cython_modules_path"]
core_modules_exclude_py = [
        i.removeprefix("src/").replace("/", ".") for i in core_modules_path
        ]


def find_cython_modules(base_path):
    modules = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                module_path = os.path.join(root, file)
                module_name = module_path.replace(".py", "").replace("/", ".")
                modules.append(Extension(
                    name=module_name.replace("src.", ""),
                    sources=[module_path],
                    extra_compile_args=["-O3"]
                ))
    return modules

core_modules = []
for path in pyproj_cfg["cython_modules_path"]:
    core_modules += find_cython_modules(path)

setup(
    ext_modules=cythonize(
        core_modules,
        compiler_directives={
            'language_level': "3",
            'embedsignature': True
        },
        nthreads=4
    ),
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=core_modules_exclude_py),
    include_package_data=True,
    exclude_package_data={
        "template_project_name": ["*.c", ]
        },
    zip_safe=False,
)
