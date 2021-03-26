from waflib.Tools.compiler_cxx import cxx_compiler
#from scripts.waf import utils

# import subprocess
import os
import sys
import subprocess



APPNAME = 'querycpp' #TODO: REPLACE
VERSION = '0.0.1' #TODO: REPLACE 

cxx_compiler['linux'] = ['clang++']

def options(opt) :
    opt.load('compiler_cxx')

def configure(cnf) :
    cnf.load('compiler_cxx')

    link_flags = ['-pthread']
    cxx_flags = ['-std=c++17', '-Wall', '-Wextra', '-O3']
    
    if sys.platform == 'darwin':
        link_flags.append('-L/usr/local/opt/llvm/lib')
        cxx_flags.append('-stdlib=libc++')

    cnf.env.append_value('CXXFLAGS', cxx_flags)        
    cnf.env.append_value('LINKFLAGS',
                         link_flags)
    
def build(bld):

        
    bld(name = '{!s}-includes'.format(APPNAME),
        includes='./include/querycpp',
        export_includes='./include/querycpp')

    bld.stlib(name = APPNAME,
        features = 'cxx cxxstlib',
        target='{!s}'.format(APPNAME),
        includes='../src',
        source=bld.path.ant_glob('src/**/*.cpp'.format(APPNAME)),
        use=['{!s}-includes'.format(APPNAME)]
    )

    bld(name = '{!s}-test-includes'.format(APPNAME),
        includes='./include',
        export_includes='./include')


    bld.recurse('test/test_column')    
    bld.recurse('test/test_table')





def test(ctx):

    subprocess.call(['./build/test/test_column/test_column'], encoding='utf-8')        
    subprocess.call(['./build/test/test_table/test_table'], encoding='utf-8')
