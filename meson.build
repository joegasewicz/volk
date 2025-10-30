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
    output: '_volk.cython-*.so',
    command: ['python3', 'setup.py', 'build_ext', '--inplace'],
    depend_files: ['volk/volk.pyx', 'volk.c', 'volk.h'],
    build_by_default: true
)
