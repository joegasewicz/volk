project('volk', 'c',
        version : '1.0.0',
        default_options : ['warning_level=3', 'c_std=c11'])

# These arguments are only used to build the shared library
# not the executables that use the library.
lib_args = ['-DBUILDING_MESON_LIBRARY']

shared_library('volk', 'volk.c',
               install : true,
               c_args : lib_args
)

cython_build = custom_target(
    'cython_build',
    output: '_volk.cpython-314-x86_64-linux-gnu.so',
    command: [
        'python3', '-c',
        'import os, subprocess; os.chdir("' + meson.source_root() + '"); ',
        'subprocess.check_call(["python3", "setup.py", "build_ext", "--inplace"])'
    ],
    depend_files: [
        meson.source_root() + '/volk/volk.pyx',
        meson.source_root() + '/volk.c',
        meson.source_root() + '/volk.h'
    ],
    build_by_default: true
)
