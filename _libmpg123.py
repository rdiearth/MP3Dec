'''Wrapper for mpg123.h

Generated with:
G:\ctypesgen\ctypesgen.py -llibmpg123 mpg123.h -o _libmpg123.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["libmpg123"] = load_library("libmpg123")

# 1 libraries
# End libraries

# No modules

_off_t = c_long # c:\\mingw\\include\\sys\\types.h: 52

off_t = _off_t # c:\\mingw\\include\\sys\\types.h: 55

# G:\\ctypesgen\\mpg123.h: 105
class struct_mpg123_handle_struct(Structure):
    pass

mpg123_handle = struct_mpg123_handle_struct # G:\\ctypesgen\\mpg123.h: 110

# G:\\ctypesgen\\mpg123.h: 117
if hasattr(_libs['libmpg123'], 'mpg123_init'):
    mpg123_init = _libs['libmpg123'].mpg123_init
    mpg123_init.argtypes = []
    mpg123_init.restype = c_int

# G:\\ctypesgen\\mpg123.h: 121
if hasattr(_libs['libmpg123'], 'mpg123_exit'):
    mpg123_exit = _libs['libmpg123'].mpg123_exit
    mpg123_exit.argtypes = []
    mpg123_exit.restype = None

# G:\\ctypesgen\\mpg123.h: 129
if hasattr(_libs['libmpg123'], 'mpg123_new'):
    mpg123_new = _libs['libmpg123'].mpg123_new
    mpg123_new.argtypes = [String, POINTER(c_int)]
    mpg123_new.restype = POINTER(mpg123_handle)

# G:\\ctypesgen\\mpg123.h: 132
if hasattr(_libs['libmpg123'], 'mpg123_delete'):
    mpg123_delete = _libs['libmpg123'].mpg123_delete
    mpg123_delete.argtypes = [POINTER(mpg123_handle)]
    mpg123_delete.restype = None

enum_mpg123_parms = c_int # G:\\ctypesgen\\mpg123.h: 135

MPG123_VERBOSE = 0 # G:\\ctypesgen\\mpg123.h: 135

MPG123_FLAGS = (MPG123_VERBOSE + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_ADD_FLAGS = (MPG123_FLAGS + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_FORCE_RATE = (MPG123_ADD_FLAGS + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_DOWN_SAMPLE = (MPG123_FORCE_RATE + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_RVA = (MPG123_DOWN_SAMPLE + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_DOWNSPEED = (MPG123_RVA + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_UPSPEED = (MPG123_DOWNSPEED + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_START_FRAME = (MPG123_UPSPEED + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_DECODE_FRAMES = (MPG123_START_FRAME + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_ICY_INTERVAL = (MPG123_DECODE_FRAMES + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_OUTSCALE = (MPG123_ICY_INTERVAL + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_TIMEOUT = (MPG123_OUTSCALE + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_REMOVE_FLAGS = (MPG123_TIMEOUT + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_RESYNC_LIMIT = (MPG123_REMOVE_FLAGS + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_INDEX_SIZE = (MPG123_RESYNC_LIMIT + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_PREFRAMES = (MPG123_INDEX_SIZE + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_FEEDPOOL = (MPG123_PREFRAMES + 1) # G:\\ctypesgen\\mpg123.h: 135

MPG123_FEEDBUFFER = (MPG123_FEEDPOOL + 1) # G:\\ctypesgen\\mpg123.h: 135

enum_mpg123_param_flags = c_int # G:\\ctypesgen\\mpg123.h: 159

MPG123_FORCE_MONO = 7 # G:\\ctypesgen\\mpg123.h: 159

MPG123_MONO_LEFT = 1 # G:\\ctypesgen\\mpg123.h: 159

MPG123_MONO_RIGHT = 2 # G:\\ctypesgen\\mpg123.h: 159

MPG123_MONO_MIX = 4 # G:\\ctypesgen\\mpg123.h: 159

MPG123_FORCE_STEREO = 8 # G:\\ctypesgen\\mpg123.h: 159

MPG123_FORCE_8BIT = 16 # G:\\ctypesgen\\mpg123.h: 159

MPG123_QUIET = 32 # G:\\ctypesgen\\mpg123.h: 159

MPG123_GAPLESS = 64 # G:\\ctypesgen\\mpg123.h: 159

MPG123_NO_RESYNC = 128 # G:\\ctypesgen\\mpg123.h: 159

MPG123_SEEKBUFFER = 256 # G:\\ctypesgen\\mpg123.h: 159

MPG123_FUZZY = 512 # G:\\ctypesgen\\mpg123.h: 159

MPG123_FORCE_FLOAT = 1024 # G:\\ctypesgen\\mpg123.h: 159

MPG123_PLAIN_ID3TEXT = 2048 # G:\\ctypesgen\\mpg123.h: 159

MPG123_IGNORE_STREAMLENGTH = 4096 # G:\\ctypesgen\\mpg123.h: 159

MPG123_SKIP_ID3V2 = 8192 # G:\\ctypesgen\\mpg123.h: 159

MPG123_IGNORE_INFOFRAME = 16384 # G:\\ctypesgen\\mpg123.h: 159

MPG123_AUTO_RESAMPLE = 32768 # G:\\ctypesgen\\mpg123.h: 159

MPG123_PICTURE = 65536 # G:\\ctypesgen\\mpg123.h: 159

enum_mpg123_param_rva = c_int # G:\\ctypesgen\\mpg123.h: 182

MPG123_RVA_OFF = 0 # G:\\ctypesgen\\mpg123.h: 182

MPG123_RVA_MIX = 1 # G:\\ctypesgen\\mpg123.h: 182

MPG123_RVA_ALBUM = 2 # G:\\ctypesgen\\mpg123.h: 182

MPG123_RVA_MAX = MPG123_RVA_ALBUM # G:\\ctypesgen\\mpg123.h: 182

# G:\\ctypesgen\\mpg123.h: 196
if hasattr(_libs['libmpg123'], 'mpg123_param'):
    mpg123_param = _libs['libmpg123'].mpg123_param
    mpg123_param.argtypes = [POINTER(mpg123_handle), enum_mpg123_parms, c_long, c_double]
    mpg123_param.restype = c_int

# G:\\ctypesgen\\mpg123.h: 202
if hasattr(_libs['libmpg123'], 'mpg123_getparam'):
    mpg123_getparam = _libs['libmpg123'].mpg123_getparam
    mpg123_getparam.argtypes = [POINTER(mpg123_handle), enum_mpg123_parms, POINTER(c_long), POINTER(c_double)]
    mpg123_getparam.restype = c_int

enum_mpg123_feature_set = c_int # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_ABI_UTF8OPEN = 0 # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_OUTPUT_8BIT = (MPG123_FEATURE_ABI_UTF8OPEN + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_OUTPUT_16BIT = (MPG123_FEATURE_OUTPUT_8BIT + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_OUTPUT_32BIT = (MPG123_FEATURE_OUTPUT_16BIT + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_INDEX = (MPG123_FEATURE_OUTPUT_32BIT + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_PARSE_ID3V2 = (MPG123_FEATURE_INDEX + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_DECODE_LAYER1 = (MPG123_FEATURE_PARSE_ID3V2 + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_DECODE_LAYER2 = (MPG123_FEATURE_DECODE_LAYER1 + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_DECODE_LAYER3 = (MPG123_FEATURE_DECODE_LAYER2 + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_DECODE_ACCURATE = (MPG123_FEATURE_DECODE_LAYER3 + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_DECODE_DOWNSAMPLE = (MPG123_FEATURE_DECODE_ACCURATE + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_DECODE_NTOM = (MPG123_FEATURE_DECODE_DOWNSAMPLE + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_PARSE_ICY = (MPG123_FEATURE_DECODE_NTOM + 1) # G:\\ctypesgen\\mpg123.h: 205

MPG123_FEATURE_TIMEOUT_READ = (MPG123_FEATURE_PARSE_ICY + 1) # G:\\ctypesgen\\mpg123.h: 205

# G:\\ctypesgen\\mpg123.h: 224
if hasattr(_libs['libmpg123'], 'mpg123_feature'):
    mpg123_feature = _libs['libmpg123'].mpg123_feature
    mpg123_feature.argtypes = [enum_mpg123_feature_set]
    mpg123_feature.restype = c_int

enum_mpg123_errors = c_int # G:\\ctypesgen\\mpg123.h: 261

MPG123_DONE = (-12) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NEW_FORMAT = (-11) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NEED_MORE = (-10) # G:\\ctypesgen\\mpg123.h: 261

MPG123_ERR = (-1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_OK = 0 # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_OUTFORMAT = (MPG123_OK + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_CHANNEL = (MPG123_BAD_OUTFORMAT + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_RATE = (MPG123_BAD_CHANNEL + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_ERR_16TO8TABLE = (MPG123_BAD_RATE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_PARAM = (MPG123_ERR_16TO8TABLE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_BUFFER = (MPG123_BAD_PARAM + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_OUT_OF_MEM = (MPG123_BAD_BUFFER + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NOT_INITIALIZED = (MPG123_OUT_OF_MEM + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_DECODER = (MPG123_NOT_INITIALIZED + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_HANDLE = (MPG123_BAD_DECODER + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_BUFFERS = (MPG123_BAD_HANDLE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_RVA = (MPG123_NO_BUFFERS + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_GAPLESS = (MPG123_BAD_RVA + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_SPACE = (MPG123_NO_GAPLESS + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_TYPES = (MPG123_NO_SPACE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_BAND = (MPG123_BAD_TYPES + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_ERR_NULL = (MPG123_BAD_BAND + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_ERR_READER = (MPG123_ERR_NULL + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_SEEK_FROM_END = (MPG123_ERR_READER + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_WHENCE = (MPG123_NO_SEEK_FROM_END + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_TIMEOUT = (MPG123_BAD_WHENCE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_FILE = (MPG123_NO_TIMEOUT + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_SEEK = (MPG123_BAD_FILE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_READER = (MPG123_NO_SEEK + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_PARS = (MPG123_NO_READER + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_INDEX_PAR = (MPG123_BAD_PARS + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_OUT_OF_SYNC = (MPG123_BAD_INDEX_PAR + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_RESYNC_FAIL = (MPG123_OUT_OF_SYNC + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_8BIT = (MPG123_RESYNC_FAIL + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_ALIGN = (MPG123_NO_8BIT + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NULL_BUFFER = (MPG123_BAD_ALIGN + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_RELSEEK = (MPG123_NULL_BUFFER + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NULL_POINTER = (MPG123_NO_RELSEEK + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_KEY = (MPG123_NULL_POINTER + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_NO_INDEX = (MPG123_BAD_KEY + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_INDEX_FAIL = (MPG123_NO_INDEX + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_DECODER_SETUP = (MPG123_INDEX_FAIL + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_MISSING_FEATURE = (MPG123_BAD_DECODER_SETUP + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_VALUE = (MPG123_MISSING_FEATURE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_LSEEK_FAILED = (MPG123_BAD_VALUE + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_BAD_CUSTOM_IO = (MPG123_LSEEK_FAILED + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_LFS_OVERFLOW = (MPG123_BAD_CUSTOM_IO + 1) # G:\\ctypesgen\\mpg123.h: 261

MPG123_INT_OVERFLOW = (MPG123_LFS_OVERFLOW + 1) # G:\\ctypesgen\\mpg123.h: 261

# G:\\ctypesgen\\mpg123.h: 314
if hasattr(_libs['libmpg123'], 'mpg123_plain_strerror'):
    mpg123_plain_strerror = _libs['libmpg123'].mpg123_plain_strerror
    mpg123_plain_strerror.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        mpg123_plain_strerror.restype = ReturnString
    else:
        mpg123_plain_strerror.restype = String
        mpg123_plain_strerror.errcheck = ReturnString

# G:\\ctypesgen\\mpg123.h: 320
if hasattr(_libs['libmpg123'], 'mpg123_strerror'):
    mpg123_strerror = _libs['libmpg123'].mpg123_strerror
    mpg123_strerror.argtypes = [POINTER(mpg123_handle)]
    if sizeof(c_int) == sizeof(c_void_p):
        mpg123_strerror.restype = ReturnString
    else:
        mpg123_strerror.restype = String
        mpg123_strerror.errcheck = ReturnString

# G:\\ctypesgen\\mpg123.h: 325
if hasattr(_libs['libmpg123'], 'mpg123_errcode'):
    mpg123_errcode = _libs['libmpg123'].mpg123_errcode
    mpg123_errcode.argtypes = [POINTER(mpg123_handle)]
    mpg123_errcode.restype = c_int

# G:\\ctypesgen\\mpg123.h: 339
if hasattr(_libs['libmpg123'], 'mpg123_decoders'):
    mpg123_decoders = _libs['libmpg123'].mpg123_decoders
    mpg123_decoders.argtypes = []
    mpg123_decoders.restype = POINTER(POINTER(c_char))

# G:\\ctypesgen\\mpg123.h: 342
if hasattr(_libs['libmpg123'], 'mpg123_supported_decoders'):
    mpg123_supported_decoders = _libs['libmpg123'].mpg123_supported_decoders
    mpg123_supported_decoders.argtypes = []
    mpg123_supported_decoders.restype = POINTER(POINTER(c_char))

# G:\\ctypesgen\\mpg123.h: 347
if hasattr(_libs['libmpg123'], 'mpg123_decoder'):
    mpg123_decoder = _libs['libmpg123'].mpg123_decoder
    mpg123_decoder.argtypes = [POINTER(mpg123_handle), String]
    mpg123_decoder.restype = c_int

# G:\\ctypesgen\\mpg123.h: 354
if hasattr(_libs['libmpg123'], 'mpg123_current_decoder'):
    mpg123_current_decoder = _libs['libmpg123'].mpg123_current_decoder
    mpg123_current_decoder.argtypes = [POINTER(mpg123_handle)]
    if sizeof(c_int) == sizeof(c_void_p):
        mpg123_current_decoder.restype = ReturnString
    else:
        mpg123_current_decoder.restype = String
        mpg123_current_decoder.errcheck = ReturnString

enum_mpg123_enc_enum = c_int # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_8 = 15 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_16 = 64 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_24 = 16384 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_32 = 256 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_SIGNED = 128 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_FLOAT = 3584 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_SIGNED_16 = ((MPG123_ENC_16 | MPG123_ENC_SIGNED) | 16) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_UNSIGNED_16 = (MPG123_ENC_16 | 32) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_UNSIGNED_8 = 1 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_SIGNED_8 = (MPG123_ENC_SIGNED | 2) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_ULAW_8 = 4 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_ALAW_8 = 8 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_SIGNED_32 = ((MPG123_ENC_32 | MPG123_ENC_SIGNED) | 4096) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_UNSIGNED_32 = (MPG123_ENC_32 | 8192) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_SIGNED_24 = ((MPG123_ENC_24 | MPG123_ENC_SIGNED) | 4096) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_UNSIGNED_24 = (MPG123_ENC_24 | 8192) # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_FLOAT_32 = 512 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_FLOAT_64 = 1024 # G:\\ctypesgen\\mpg123.h: 391

MPG123_ENC_ANY = (((((((((((MPG123_ENC_SIGNED_16 | MPG123_ENC_UNSIGNED_16) | MPG123_ENC_UNSIGNED_8) | MPG123_ENC_SIGNED_8) | MPG123_ENC_ULAW_8) | MPG123_ENC_ALAW_8) | MPG123_ENC_SIGNED_32) | MPG123_ENC_UNSIGNED_32) | MPG123_ENC_SIGNED_24) | MPG123_ENC_UNSIGNED_24) | MPG123_ENC_FLOAT_32) | MPG123_ENC_FLOAT_64) # G:\\ctypesgen\\mpg123.h: 391

enum_mpg123_channelcount = c_int # G:\\ctypesgen\\mpg123.h: 419

MPG123_MONO = 1 # G:\\ctypesgen\\mpg123.h: 419

MPG123_STEREO = 2 # G:\\ctypesgen\\mpg123.h: 419

# G:\\ctypesgen\\mpg123.h: 430
if hasattr(_libs['libmpg123'], 'mpg123_rates'):
    mpg123_rates = _libs['libmpg123'].mpg123_rates
    mpg123_rates.argtypes = [POINTER(POINTER(c_long)), POINTER(c_size_t)]
    mpg123_rates.restype = None

# G:\\ctypesgen\\mpg123.h: 436
if hasattr(_libs['libmpg123'], 'mpg123_encodings'):
    mpg123_encodings = _libs['libmpg123'].mpg123_encodings
    mpg123_encodings.argtypes = [POINTER(POINTER(c_int)), POINTER(c_size_t)]
    mpg123_encodings.restype = None

# G:\\ctypesgen\\mpg123.h: 441
if hasattr(_libs['libmpg123'], 'mpg123_encsize'):
    mpg123_encsize = _libs['libmpg123'].mpg123_encsize
    mpg123_encsize.argtypes = [c_int]
    mpg123_encsize.restype = c_int

# G:\\ctypesgen\\mpg123.h: 447
if hasattr(_libs['libmpg123'], 'mpg123_format_none'):
    mpg123_format_none = _libs['libmpg123'].mpg123_format_none
    mpg123_format_none.argtypes = [POINTER(mpg123_handle)]
    mpg123_format_none.restype = c_int

# G:\\ctypesgen\\mpg123.h: 453
if hasattr(_libs['libmpg123'], 'mpg123_format_all'):
    mpg123_format_all = _libs['libmpg123'].mpg123_format_all
    mpg123_format_all.argtypes = [POINTER(mpg123_handle)]
    mpg123_format_all.restype = c_int

# G:\\ctypesgen\\mpg123.h: 461
if hasattr(_libs['libmpg123'], 'mpg123_format'):
    mpg123_format = _libs['libmpg123'].mpg123_format
    mpg123_format.argtypes = [POINTER(mpg123_handle), c_long, c_int, c_int]
    mpg123_format.restype = c_int

# G:\\ctypesgen\\mpg123.h: 467
if hasattr(_libs['libmpg123'], 'mpg123_format_support'):
    mpg123_format_support = _libs['libmpg123'].mpg123_format_support
    mpg123_format_support.argtypes = [POINTER(mpg123_handle), c_long, c_int]
    mpg123_format_support.restype = c_int

# G:\\ctypesgen\\mpg123.h: 472
if hasattr(_libs['libmpg123'], 'mpg123_getformat'):
    mpg123_getformat = _libs['libmpg123'].mpg123_getformat
    mpg123_getformat.argtypes = [POINTER(mpg123_handle), POINTER(c_long), POINTER(c_int), POINTER(c_int)]
    mpg123_getformat.restype = c_int

# G:\\ctypesgen\\mpg123.h: 493
if hasattr(_libs['libmpg123'], 'mpg123_open'):
    mpg123_open = _libs['libmpg123'].mpg123_open
    mpg123_open.argtypes = [POINTER(mpg123_handle), String]
    mpg123_open.restype = c_int

# G:\\ctypesgen\\mpg123.h: 498
if hasattr(_libs['libmpg123'], 'mpg123_open_fd'):
    mpg123_open_fd = _libs['libmpg123'].mpg123_open_fd
    mpg123_open_fd.argtypes = [POINTER(mpg123_handle), c_int]
    mpg123_open_fd.restype = c_int

# G:\\ctypesgen\\mpg123.h: 505
if hasattr(_libs['libmpg123'], 'mpg123_open_handle'):
    mpg123_open_handle = _libs['libmpg123'].mpg123_open_handle
    mpg123_open_handle.argtypes = [POINTER(mpg123_handle), POINTER(None)]
    mpg123_open_handle.restype = c_int

# G:\\ctypesgen\\mpg123.h: 511
if hasattr(_libs['libmpg123'], 'mpg123_open_feed'):
    mpg123_open_feed = _libs['libmpg123'].mpg123_open_feed
    mpg123_open_feed.argtypes = [POINTER(mpg123_handle)]
    mpg123_open_feed.restype = c_int

# G:\\ctypesgen\\mpg123.h: 516
if hasattr(_libs['libmpg123'], 'mpg123_close'):
    mpg123_close = _libs['libmpg123'].mpg123_close
    mpg123_close.argtypes = [POINTER(mpg123_handle)]
    mpg123_close.restype = c_int

# G:\\ctypesgen\\mpg123.h: 524
if hasattr(_libs['libmpg123'], 'mpg123_read'):
    mpg123_read = _libs['libmpg123'].mpg123_read
    mpg123_read.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), c_size_t, POINTER(c_size_t)]
    mpg123_read.restype = c_int

# G:\\ctypesgen\\mpg123.h: 532
if hasattr(_libs['libmpg123'], 'mpg123_feed'):
    mpg123_feed = _libs['libmpg123'].mpg123_feed
    mpg123_feed.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), c_size_t]
    mpg123_feed.restype = c_int

# G:\\ctypesgen\\mpg123.h: 548
if hasattr(_libs['libmpg123'], 'mpg123_decode'):
    mpg123_decode = _libs['libmpg123'].mpg123_decode
    mpg123_decode.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), c_size_t, POINTER(c_ubyte), c_size_t, POINTER(c_size_t)]
    mpg123_decode.restype = c_int

# G:\\ctypesgen\\mpg123.h: 557
if hasattr(_libs['libmpg123'], 'mpg123_decode_frame'):
    mpg123_decode_frame = _libs['libmpg123'].mpg123_decode_frame
    mpg123_decode_frame.argtypes = [POINTER(mpg123_handle), POINTER(off_t), POINTER(POINTER(c_ubyte)), POINTER(c_size_t)]
    mpg123_decode_frame.restype = c_int

# G:\\ctypesgen\\mpg123.h: 567
if hasattr(_libs['libmpg123'], 'mpg123_framebyframe_decode'):
    mpg123_framebyframe_decode = _libs['libmpg123'].mpg123_framebyframe_decode
    mpg123_framebyframe_decode.argtypes = [POINTER(mpg123_handle), POINTER(off_t), POINTER(POINTER(c_ubyte)), POINTER(c_size_t)]
    mpg123_framebyframe_decode.restype = c_int

# G:\\ctypesgen\\mpg123.h: 574
if hasattr(_libs['libmpg123'], 'mpg123_framebyframe_next'):
    mpg123_framebyframe_next = _libs['libmpg123'].mpg123_framebyframe_next
    mpg123_framebyframe_next.argtypes = [POINTER(mpg123_handle)]
    mpg123_framebyframe_next.restype = c_int

# G:\\ctypesgen\\mpg123.h: 590
if hasattr(_libs['libmpg123'], 'mpg123_framedata'):
    mpg123_framedata = _libs['libmpg123'].mpg123_framedata
    mpg123_framedata.argtypes = [POINTER(mpg123_handle), POINTER(c_ulong), POINTER(POINTER(c_ubyte)), POINTER(c_size_t)]
    mpg123_framedata.restype = c_int

# G:\\ctypesgen\\mpg123.h: 595
if hasattr(_libs['libmpg123'], 'mpg123_framepos'):
    mpg123_framepos = _libs['libmpg123'].mpg123_framepos
    mpg123_framepos.argtypes = [POINTER(mpg123_handle)]
    mpg123_framepos.restype = off_t

# G:\\ctypesgen\\mpg123.h: 624
if hasattr(_libs['libmpg123'], 'mpg123_tell'):
    mpg123_tell = _libs['libmpg123'].mpg123_tell
    mpg123_tell.argtypes = [POINTER(mpg123_handle)]
    mpg123_tell.restype = off_t

# G:\\ctypesgen\\mpg123.h: 629
if hasattr(_libs['libmpg123'], 'mpg123_tellframe'):
    mpg123_tellframe = _libs['libmpg123'].mpg123_tellframe
    mpg123_tellframe.argtypes = [POINTER(mpg123_handle)]
    mpg123_tellframe.restype = off_t

# G:\\ctypesgen\\mpg123.h: 634
if hasattr(_libs['libmpg123'], 'mpg123_tell_stream'):
    mpg123_tell_stream = _libs['libmpg123'].mpg123_tell_stream
    mpg123_tell_stream.argtypes = [POINTER(mpg123_handle)]
    mpg123_tell_stream.restype = off_t

# G:\\ctypesgen\\mpg123.h: 639
if hasattr(_libs['libmpg123'], 'mpg123_seek'):
    mpg123_seek = _libs['libmpg123'].mpg123_seek
    mpg123_seek.argtypes = [POINTER(mpg123_handle), off_t, c_int]
    mpg123_seek.restype = off_t

# G:\\ctypesgen\\mpg123.h: 646
if hasattr(_libs['libmpg123'], 'mpg123_feedseek'):
    mpg123_feedseek = _libs['libmpg123'].mpg123_feedseek
    mpg123_feedseek.argtypes = [POINTER(mpg123_handle), off_t, c_int, POINTER(off_t)]
    mpg123_feedseek.restype = off_t

# G:\\ctypesgen\\mpg123.h: 651
if hasattr(_libs['libmpg123'], 'mpg123_seek_frame'):
    mpg123_seek_frame = _libs['libmpg123'].mpg123_seek_frame
    mpg123_seek_frame.argtypes = [POINTER(mpg123_handle), off_t, c_int]
    mpg123_seek_frame.restype = off_t

# G:\\ctypesgen\\mpg123.h: 656
if hasattr(_libs['libmpg123'], 'mpg123_timeframe'):
    mpg123_timeframe = _libs['libmpg123'].mpg123_timeframe
    mpg123_timeframe.argtypes = [POINTER(mpg123_handle), c_double]
    mpg123_timeframe.restype = off_t

# G:\\ctypesgen\\mpg123.h: 666
if hasattr(_libs['libmpg123'], 'mpg123_index'):
    mpg123_index = _libs['libmpg123'].mpg123_index
    mpg123_index.argtypes = [POINTER(mpg123_handle), POINTER(POINTER(off_t)), POINTER(off_t), POINTER(c_size_t)]
    mpg123_index.restype = c_int

# G:\\ctypesgen\\mpg123.h: 676
if hasattr(_libs['libmpg123'], 'mpg123_set_index'):
    mpg123_set_index = _libs['libmpg123'].mpg123_set_index
    mpg123_set_index.argtypes = [POINTER(mpg123_handle), POINTER(off_t), off_t, c_size_t]
    mpg123_set_index.restype = c_int

# G:\\ctypesgen\\mpg123.h: 684
if hasattr(_libs['libmpg123'], 'mpg123_position'):
    mpg123_position = _libs['libmpg123'].mpg123_position
    mpg123_position.argtypes = [POINTER(mpg123_handle), off_t, off_t, POINTER(off_t), POINTER(off_t), POINTER(c_double), POINTER(c_double)]
    mpg123_position.restype = c_int

enum_mpg123_channels = c_int # G:\\ctypesgen\\mpg123.h: 694

MPG123_LEFT = 1 # G:\\ctypesgen\\mpg123.h: 694

MPG123_RIGHT = 2 # G:\\ctypesgen\\mpg123.h: 694

MPG123_LR = 3 # G:\\ctypesgen\\mpg123.h: 694

# G:\\ctypesgen\\mpg123.h: 707
if hasattr(_libs['libmpg123'], 'mpg123_eq'):
    mpg123_eq = _libs['libmpg123'].mpg123_eq
    mpg123_eq.argtypes = [POINTER(mpg123_handle), enum_mpg123_channels, c_int, c_double]
    mpg123_eq.restype = c_int

# G:\\ctypesgen\\mpg123.h: 713
if hasattr(_libs['libmpg123'], 'mpg123_geteq'):
    mpg123_geteq = _libs['libmpg123'].mpg123_geteq
    mpg123_geteq.argtypes = [POINTER(mpg123_handle), enum_mpg123_channels, c_int]
    mpg123_geteq.restype = c_double

# G:\\ctypesgen\\mpg123.h: 718
if hasattr(_libs['libmpg123'], 'mpg123_reset_eq'):
    mpg123_reset_eq = _libs['libmpg123'].mpg123_reset_eq
    mpg123_reset_eq.argtypes = [POINTER(mpg123_handle)]
    mpg123_reset_eq.restype = c_int

# G:\\ctypesgen\\mpg123.h: 722
if hasattr(_libs['libmpg123'], 'mpg123_volume'):
    mpg123_volume = _libs['libmpg123'].mpg123_volume
    mpg123_volume.argtypes = [POINTER(mpg123_handle), c_double]
    mpg123_volume.restype = c_int

# G:\\ctypesgen\\mpg123.h: 725
if hasattr(_libs['libmpg123'], 'mpg123_volume_change'):
    mpg123_volume_change = _libs['libmpg123'].mpg123_volume_change
    mpg123_volume_change.argtypes = [POINTER(mpg123_handle), c_double]
    mpg123_volume_change.restype = c_int

# G:\\ctypesgen\\mpg123.h: 731
if hasattr(_libs['libmpg123'], 'mpg123_getvolume'):
    mpg123_getvolume = _libs['libmpg123'].mpg123_getvolume
    mpg123_getvolume.argtypes = [POINTER(mpg123_handle), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    mpg123_getvolume.restype = c_int

enum_mpg123_vbr = c_int # G:\\ctypesgen\\mpg123.h: 744

MPG123_CBR = 0 # G:\\ctypesgen\\mpg123.h: 744

MPG123_VBR = (MPG123_CBR + 1) # G:\\ctypesgen\\mpg123.h: 744

MPG123_ABR = (MPG123_VBR + 1) # G:\\ctypesgen\\mpg123.h: 744

enum_mpg123_version = c_int # G:\\ctypesgen\\mpg123.h: 751

MPG123_1_0 = 0 # G:\\ctypesgen\\mpg123.h: 751

MPG123_2_0 = (MPG123_1_0 + 1) # G:\\ctypesgen\\mpg123.h: 751

MPG123_2_5 = (MPG123_2_0 + 1) # G:\\ctypesgen\\mpg123.h: 751

enum_mpg123_mode = c_int # G:\\ctypesgen\\mpg123.h: 760

MPG123_M_STEREO = 0 # G:\\ctypesgen\\mpg123.h: 760

MPG123_M_JOINT = (MPG123_M_STEREO + 1) # G:\\ctypesgen\\mpg123.h: 760

MPG123_M_DUAL = (MPG123_M_JOINT + 1) # G:\\ctypesgen\\mpg123.h: 760

MPG123_M_MONO = (MPG123_M_DUAL + 1) # G:\\ctypesgen\\mpg123.h: 760

enum_mpg123_flags = c_int # G:\\ctypesgen\\mpg123.h: 769

MPG123_CRC = 1 # G:\\ctypesgen\\mpg123.h: 769

MPG123_COPYRIGHT = 2 # G:\\ctypesgen\\mpg123.h: 769

MPG123_PRIVATE = 4 # G:\\ctypesgen\\mpg123.h: 769

MPG123_ORIGINAL = 8 # G:\\ctypesgen\\mpg123.h: 769

# G:\\ctypesgen\\mpg123.h: 777
class struct_mpg123_frameinfo(Structure):
    pass

struct_mpg123_frameinfo.__slots__ = [
    'version',
    'layer',
    'rate',
    'mode',
    'mode_ext',
    'framesize',
    'flags',
    'emphasis',
    'bitrate',
    'abr_rate',
    'vbr',
]
struct_mpg123_frameinfo._fields_ = [
    ('version', enum_mpg123_version),
    ('layer', c_int),
    ('rate', c_long),
    ('mode', enum_mpg123_mode),
    ('mode_ext', c_int),
    ('framesize', c_int),
    ('flags', enum_mpg123_flags),
    ('emphasis', c_int),
    ('bitrate', c_int),
    ('abr_rate', c_int),
    ('vbr', enum_mpg123_vbr),
]

# G:\\ctypesgen\\mpg123.h: 795
if hasattr(_libs['libmpg123'], 'mpg123_info'):
    mpg123_info = _libs['libmpg123'].mpg123_info
    mpg123_info.argtypes = [POINTER(mpg123_handle), POINTER(struct_mpg123_frameinfo)]
    mpg123_info.restype = c_int

# G:\\ctypesgen\\mpg123.h: 798
if hasattr(_libs['libmpg123'], 'mpg123_safe_buffer'):
    mpg123_safe_buffer = _libs['libmpg123'].mpg123_safe_buffer
    mpg123_safe_buffer.argtypes = []
    mpg123_safe_buffer.restype = c_size_t

# G:\\ctypesgen\\mpg123.h: 806
if hasattr(_libs['libmpg123'], 'mpg123_scan'):
    mpg123_scan = _libs['libmpg123'].mpg123_scan
    mpg123_scan.argtypes = [POINTER(mpg123_handle)]
    mpg123_scan.restype = c_int

# G:\\ctypesgen\\mpg123.h: 810
if hasattr(_libs['libmpg123'], 'mpg123_length'):
    mpg123_length = _libs['libmpg123'].mpg123_length
    mpg123_length.argtypes = [POINTER(mpg123_handle)]
    mpg123_length.restype = off_t

# G:\\ctypesgen\\mpg123.h: 816
if hasattr(_libs['libmpg123'], 'mpg123_set_filesize'):
    mpg123_set_filesize = _libs['libmpg123'].mpg123_set_filesize
    mpg123_set_filesize.argtypes = [POINTER(mpg123_handle), off_t]
    mpg123_set_filesize.restype = c_int

# G:\\ctypesgen\\mpg123.h: 819
if hasattr(_libs['libmpg123'], 'mpg123_tpf'):
    mpg123_tpf = _libs['libmpg123'].mpg123_tpf
    mpg123_tpf.argtypes = [POINTER(mpg123_handle)]
    mpg123_tpf.restype = c_double

# G:\\ctypesgen\\mpg123.h: 822
if hasattr(_libs['libmpg123'], 'mpg123_spf'):
    mpg123_spf = _libs['libmpg123'].mpg123_spf
    mpg123_spf.argtypes = [POINTER(mpg123_handle)]
    mpg123_spf.restype = c_int

# G:\\ctypesgen\\mpg123.h: 825
if hasattr(_libs['libmpg123'], 'mpg123_clip'):
    mpg123_clip = _libs['libmpg123'].mpg123_clip
    mpg123_clip.argtypes = [POINTER(mpg123_handle)]
    mpg123_clip.restype = c_long

enum_mpg123_state = c_int # G:\\ctypesgen\\mpg123.h: 829

MPG123_ACCURATE = 1 # G:\\ctypesgen\\mpg123.h: 829

MPG123_BUFFERFILL = (MPG123_ACCURATE + 1) # G:\\ctypesgen\\mpg123.h: 829

MPG123_FRANKENSTEIN = (MPG123_BUFFERFILL + 1) # G:\\ctypesgen\\mpg123.h: 829

MPG123_FRESH_DECODER = (MPG123_FRANKENSTEIN + 1) # G:\\ctypesgen\\mpg123.h: 829

# G:\\ctypesgen\\mpg123.h: 843
if hasattr(_libs['libmpg123'], 'mpg123_getstate'):
    mpg123_getstate = _libs['libmpg123'].mpg123_getstate
    mpg123_getstate.argtypes = [POINTER(mpg123_handle), enum_mpg123_state, POINTER(c_long), POINTER(c_double)]
    mpg123_getstate.restype = c_int

# G:\\ctypesgen\\mpg123.h: 863
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'p',
    'size',
    'fill',
]
struct_anon_4._fields_ = [
    ('p', String),
    ('size', c_size_t),
    ('fill', c_size_t),
]

mpg123_string = struct_anon_4 # G:\\ctypesgen\\mpg123.h: 863

# G:\\ctypesgen\\mpg123.h: 866
if hasattr(_libs['libmpg123'], 'mpg123_init_string'):
    mpg123_init_string = _libs['libmpg123'].mpg123_init_string
    mpg123_init_string.argtypes = [POINTER(mpg123_string)]
    mpg123_init_string.restype = None

# G:\\ctypesgen\\mpg123.h: 869
if hasattr(_libs['libmpg123'], 'mpg123_free_string'):
    mpg123_free_string = _libs['libmpg123'].mpg123_free_string
    mpg123_free_string.argtypes = [POINTER(mpg123_string)]
    mpg123_free_string.restype = None

# G:\\ctypesgen\\mpg123.h: 873
if hasattr(_libs['libmpg123'], 'mpg123_resize_string'):
    mpg123_resize_string = _libs['libmpg123'].mpg123_resize_string
    mpg123_resize_string.argtypes = [POINTER(mpg123_string), c_size_t]
    mpg123_resize_string.restype = c_int

# G:\\ctypesgen\\mpg123.h: 879
if hasattr(_libs['libmpg123'], 'mpg123_grow_string'):
    mpg123_grow_string = _libs['libmpg123'].mpg123_grow_string
    mpg123_grow_string.argtypes = [POINTER(mpg123_string), c_size_t]
    mpg123_grow_string.restype = c_int

# G:\\ctypesgen\\mpg123.h: 883
if hasattr(_libs['libmpg123'], 'mpg123_copy_string'):
    mpg123_copy_string = _libs['libmpg123'].mpg123_copy_string
    mpg123_copy_string.argtypes = [POINTER(mpg123_string), POINTER(mpg123_string)]
    mpg123_copy_string.restype = c_int

# G:\\ctypesgen\\mpg123.h: 887
if hasattr(_libs['libmpg123'], 'mpg123_add_string'):
    mpg123_add_string = _libs['libmpg123'].mpg123_add_string
    mpg123_add_string.argtypes = [POINTER(mpg123_string), String]
    mpg123_add_string.restype = c_int

# G:\\ctypesgen\\mpg123.h: 893
if hasattr(_libs['libmpg123'], 'mpg123_add_substring'):
    mpg123_add_substring = _libs['libmpg123'].mpg123_add_substring
    mpg123_add_substring.argtypes = [POINTER(mpg123_string), String, c_size_t, c_size_t]
    mpg123_add_substring.restype = c_int

# G:\\ctypesgen\\mpg123.h: 897
if hasattr(_libs['libmpg123'], 'mpg123_set_string'):
    mpg123_set_string = _libs['libmpg123'].mpg123_set_string
    mpg123_set_string.argtypes = [POINTER(mpg123_string), String]
    mpg123_set_string.restype = c_int

# G:\\ctypesgen\\mpg123.h: 903
if hasattr(_libs['libmpg123'], 'mpg123_set_substring'):
    mpg123_set_substring = _libs['libmpg123'].mpg123_set_substring
    mpg123_set_substring.argtypes = [POINTER(mpg123_string), String, c_size_t, c_size_t]
    mpg123_set_substring.restype = c_int

# G:\\ctypesgen\\mpg123.h: 911
if hasattr(_libs['libmpg123'], 'mpg123_strlen'):
    mpg123_strlen = _libs['libmpg123'].mpg123_strlen
    mpg123_strlen.argtypes = [POINTER(mpg123_string), c_int]
    mpg123_strlen.restype = c_size_t

# G:\\ctypesgen\\mpg123.h: 917
if hasattr(_libs['libmpg123'], 'mpg123_chomp_string'):
    mpg123_chomp_string = _libs['libmpg123'].mpg123_chomp_string
    mpg123_chomp_string.argtypes = [POINTER(mpg123_string)]
    mpg123_chomp_string.restype = c_int

enum_mpg123_text_encoding = c_int # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_unknown = 0 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_utf8 = 1 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_latin1 = 2 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_icy = 3 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_cp1252 = 4 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_utf16 = 5 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_utf16bom = 6 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_utf16be = 7 # G:\\ctypesgen\\mpg123.h: 920

mpg123_text_max = 7 # G:\\ctypesgen\\mpg123.h: 920

enum_mpg123_id3_enc = c_int # G:\\ctypesgen\\mpg123.h: 940

mpg123_id3_latin1 = 0 # G:\\ctypesgen\\mpg123.h: 940

mpg123_id3_utf16bom = 1 # G:\\ctypesgen\\mpg123.h: 940

mpg123_id3_utf16be = 2 # G:\\ctypesgen\\mpg123.h: 940

mpg123_id3_utf8 = 3 # G:\\ctypesgen\\mpg123.h: 940

mpg123_id3_enc_max = 3 # G:\\ctypesgen\\mpg123.h: 940

# G:\\ctypesgen\\mpg123.h: 950
if hasattr(_libs['libmpg123'], 'mpg123_enc_from_id3'):
    mpg123_enc_from_id3 = _libs['libmpg123'].mpg123_enc_from_id3
    mpg123_enc_from_id3.argtypes = [c_ubyte]
    mpg123_enc_from_id3.restype = enum_mpg123_text_encoding

# G:\\ctypesgen\\mpg123.h: 962
if hasattr(_libs['libmpg123'], 'mpg123_store_utf8'):
    mpg123_store_utf8 = _libs['libmpg123'].mpg123_store_utf8
    mpg123_store_utf8.argtypes = [POINTER(mpg123_string), enum_mpg123_text_encoding, POINTER(c_ubyte), c_size_t]
    mpg123_store_utf8.restype = c_int

# G:\\ctypesgen\\mpg123.h: 974
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'lang',
    'id',
    'description',
    'text',
]
struct_anon_5._fields_ = [
    ('lang', c_char * 3),
    ('id', c_char * 4),
    ('description', mpg123_string),
    ('text', mpg123_string),
]

mpg123_text = struct_anon_5 # G:\\ctypesgen\\mpg123.h: 974

enum_mpg123_id3_pic_type = c_int # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_other = 0 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_icon = 1 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_other_icon = 2 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_front_cover = 3 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_back_cover = 4 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_leaflet = 5 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_media = 6 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_lead = 7 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_artist = 8 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_conductor = 9 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_orchestra = 10 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_composer = 11 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_lyricist = 12 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_location = 13 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_recording = 14 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_performance = 15 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_video = 16 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_fish = 17 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_illustration = 18 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_artist_logo = 19 # G:\\ctypesgen\\mpg123.h: 977

mpg123_id3_pic_publisher_logo = 20 # G:\\ctypesgen\\mpg123.h: 977

# G:\\ctypesgen\\mpg123.h: 1013
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'type',
    'description',
    'mime_type',
    'size',
    'data',
]
struct_anon_6._fields_ = [
    ('type', c_char),
    ('description', mpg123_string),
    ('mime_type', mpg123_string),
    ('size', c_size_t),
    ('data', POINTER(c_ubyte)),
]

mpg123_picture = struct_anon_6 # G:\\ctypesgen\\mpg123.h: 1013

# G:\\ctypesgen\\mpg123.h: 1039
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'version',
    'title',
    'artist',
    'album',
    'year',
    'genre',
    'comment',
    'comment_list',
    'comments',
    'text',
    'texts',
    'extra',
    'extras',
    'picture',
    'pictures',
]
struct_anon_7._fields_ = [
    ('version', c_ubyte),
    ('title', POINTER(mpg123_string)),
    ('artist', POINTER(mpg123_string)),
    ('album', POINTER(mpg123_string)),
    ('year', POINTER(mpg123_string)),
    ('genre', POINTER(mpg123_string)),
    ('comment', POINTER(mpg123_string)),
    ('comment_list', POINTER(mpg123_text)),
    ('comments', c_size_t),
    ('text', POINTER(mpg123_text)),
    ('texts', c_size_t),
    ('extra', POINTER(mpg123_text)),
    ('extras', c_size_t),
    ('picture', POINTER(mpg123_picture)),
    ('pictures', c_size_t),
]

mpg123_id3v2 = struct_anon_7 # G:\\ctypesgen\\mpg123.h: 1039

# G:\\ctypesgen\\mpg123.h: 1054
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'tag',
    'title',
    'artist',
    'album',
    'year',
    'comment',
    'genre',
]
struct_anon_8._fields_ = [
    ('tag', c_char * 3),
    ('title', c_char * 30),
    ('artist', c_char * 30),
    ('album', c_char * 30),
    ('year', c_char * 4),
    ('comment', c_char * 30),
    ('genre', c_ubyte),
]

mpg123_id3v1 = struct_anon_8 # G:\\ctypesgen\\mpg123.h: 1054

# G:\\ctypesgen\\mpg123.h: 1063
if hasattr(_libs['libmpg123'], 'mpg123_meta_check'):
    mpg123_meta_check = _libs['libmpg123'].mpg123_meta_check
    mpg123_meta_check.argtypes = [POINTER(mpg123_handle)]
    mpg123_meta_check.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1066
if hasattr(_libs['libmpg123'], 'mpg123_meta_free'):
    mpg123_meta_free = _libs['libmpg123'].mpg123_meta_free
    mpg123_meta_free.argtypes = [POINTER(mpg123_handle)]
    mpg123_meta_free.restype = None

# G:\\ctypesgen\\mpg123.h: 1072
if hasattr(_libs['libmpg123'], 'mpg123_id3'):
    mpg123_id3 = _libs['libmpg123'].mpg123_id3
    mpg123_id3.argtypes = [POINTER(mpg123_handle), POINTER(POINTER(mpg123_id3v1)), POINTER(POINTER(mpg123_id3v2))]
    mpg123_id3.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1077
if hasattr(_libs['libmpg123'], 'mpg123_icy'):
    mpg123_icy = _libs['libmpg123'].mpg123_icy
    mpg123_icy.argtypes = [POINTER(mpg123_handle), POINTER(POINTER(c_char))]
    mpg123_icy.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1083
if hasattr(_libs['libmpg123'], 'mpg123_icy2utf8'):
    mpg123_icy2utf8 = _libs['libmpg123'].mpg123_icy2utf8
    mpg123_icy2utf8.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mpg123_icy2utf8.restype = ReturnString
    else:
        mpg123_icy2utf8.restype = String
        mpg123_icy2utf8.errcheck = ReturnString

# G:\\ctypesgen\\mpg123.h: 1105
class struct_mpg123_pars_struct(Structure):
    pass

mpg123_pars = struct_mpg123_pars_struct # G:\\ctypesgen\\mpg123.h: 1108

# G:\\ctypesgen\\mpg123.h: 1111
if hasattr(_libs['libmpg123'], 'mpg123_parnew'):
    mpg123_parnew = _libs['libmpg123'].mpg123_parnew
    mpg123_parnew.argtypes = [POINTER(mpg123_pars), String, POINTER(c_int)]
    mpg123_parnew.restype = POINTER(mpg123_handle)

# G:\\ctypesgen\\mpg123.h: 1114
if hasattr(_libs['libmpg123'], 'mpg123_new_pars'):
    mpg123_new_pars = _libs['libmpg123'].mpg123_new_pars
    mpg123_new_pars.argtypes = [POINTER(c_int)]
    mpg123_new_pars.restype = POINTER(mpg123_pars)

# G:\\ctypesgen\\mpg123.h: 1117
if hasattr(_libs['libmpg123'], 'mpg123_delete_pars'):
    mpg123_delete_pars = _libs['libmpg123'].mpg123_delete_pars
    mpg123_delete_pars.argtypes = [POINTER(mpg123_pars)]
    mpg123_delete_pars.restype = None

# G:\\ctypesgen\\mpg123.h: 1123
if hasattr(_libs['libmpg123'], 'mpg123_fmt_none'):
    mpg123_fmt_none = _libs['libmpg123'].mpg123_fmt_none
    mpg123_fmt_none.argtypes = [POINTER(mpg123_pars)]
    mpg123_fmt_none.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1129
if hasattr(_libs['libmpg123'], 'mpg123_fmt_all'):
    mpg123_fmt_all = _libs['libmpg123'].mpg123_fmt_all
    mpg123_fmt_all.argtypes = [POINTER(mpg123_pars)]
    mpg123_fmt_all.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1137
if hasattr(_libs['libmpg123'], 'mpg123_fmt'):
    mpg123_fmt = _libs['libmpg123'].mpg123_fmt
    mpg123_fmt.argtypes = [POINTER(mpg123_pars), c_long, c_int, c_int]
    mpg123_fmt.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1143
if hasattr(_libs['libmpg123'], 'mpg123_fmt_support'):
    mpg123_fmt_support = _libs['libmpg123'].mpg123_fmt_support
    mpg123_fmt_support.argtypes = [POINTER(mpg123_pars), c_long, c_int]
    mpg123_fmt_support.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1147
if hasattr(_libs['libmpg123'], 'mpg123_par'):
    mpg123_par = _libs['libmpg123'].mpg123_par
    mpg123_par.argtypes = [POINTER(mpg123_pars), enum_mpg123_parms, c_long, c_double]
    mpg123_par.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1151
if hasattr(_libs['libmpg123'], 'mpg123_getpar'):
    mpg123_getpar = _libs['libmpg123'].mpg123_getpar
    mpg123_getpar.argtypes = [POINTER(mpg123_pars), enum_mpg123_parms, POINTER(c_long), POINTER(c_double)]
    mpg123_getpar.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1170
if hasattr(_libs['libmpg123'], 'mpg123_replace_buffer'):
    mpg123_replace_buffer = _libs['libmpg123'].mpg123_replace_buffer
    mpg123_replace_buffer.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), c_size_t]
    mpg123_replace_buffer.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1174
if hasattr(_libs['libmpg123'], 'mpg123_outblock'):
    mpg123_outblock = _libs['libmpg123'].mpg123_outblock
    mpg123_outblock.argtypes = [POINTER(mpg123_handle)]
    mpg123_outblock.restype = c_size_t

# G:\\ctypesgen\\mpg123.h: 1183
if hasattr(_libs['libmpg123'], 'mpg123_replace_reader'):
    mpg123_replace_reader = _libs['libmpg123'].mpg123_replace_reader
    mpg123_replace_reader.argtypes = [POINTER(mpg123_handle), CFUNCTYPE(UNCHECKED(c_ptrdiff_t), c_int, POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(off_t), c_int, off_t, c_int)]
    mpg123_replace_reader.restype = c_int

# G:\\ctypesgen\\mpg123.h: 1194
if hasattr(_libs['libmpg123'], 'mpg123_replace_reader_handle'):
    mpg123_replace_reader_handle = _libs['libmpg123'].mpg123_replace_reader_handle
    mpg123_replace_reader_handle.argtypes = [POINTER(mpg123_handle), CFUNCTYPE(UNCHECKED(c_ptrdiff_t), POINTER(None), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(off_t), POINTER(None), off_t, c_int), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    mpg123_replace_reader_handle.restype = c_int

# G:\\ctypesgen\\mpg123.h: 15
try:
    MPG123_API_VERSION = 41
except:
    pass

# G:\\ctypesgen\\mpg123.h: 1056
try:
    MPG123_ID3 = 3
except:
    pass

# G:\\ctypesgen\\mpg123.h: 1057
try:
    MPG123_NEW_ID3 = 1
except:
    pass

# G:\\ctypesgen\\mpg123.h: 1058
try:
    MPG123_ICY = 12
except:
    pass

# G:\\ctypesgen\\mpg123.h: 1059
try:
    MPG123_NEW_ICY = 4
except:
    pass

mpg123_handle_struct = struct_mpg123_handle_struct # G:\\ctypesgen\\mpg123.h: 105

mpg123_frameinfo = struct_mpg123_frameinfo # G:\\ctypesgen\\mpg123.h: 777

mpg123_pars_struct = struct_mpg123_pars_struct # G:\\ctypesgen\\mpg123.h: 1105

# No inserted files

