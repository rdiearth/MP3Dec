"""
paudio - python binding for portaudio library
- simple
- blocking
- LGPL
- Ardi Nursyamsu (rdiearth@yahoo.com)

package:
- this module
- _portaudio.py for function wrapper
- portaudio.dll for the dynamic-linked-library written in C

version:
0.1
- convert sample format from paudio to bytes per sample
- convert bytes per sample to pyaudiosampleformat
- Initializing Output device
- write data to audio
- Exiting library upon object destruction
0.2
- fix buffer problem so you can input any number of bytes of data into write function
"""

# PAudio : Python Bindings for PortAudio

# Copyright (c) 2015 Ardi Nursyamsu

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
	
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WAARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

"""
PAudio provides Python bindings for PortAudio, the cross-platform 
audio I/O library. But with this PAudio, you can easily play PCM raw 
audio data in Windows using function that have blocking-behaviour so 
you don't have to calculate the timing between writing two or more buffer.

This PAudio is written as supported module for Author's final project
due to limitation of PyAudio limitation that often enduring error when
importing the library.
"""

import _portaudio as pa

#####################################################################
# GLOBALS
#####################################################################

#### PaSampleFormat Sample Format #####

paFloat32 		= pa.paFloat32			#: 32 bit float
paInt32			= pa.paInt32			#: 32 bit int
paInt24			= pa.paInt24			#: 24 bit int
paInt16			= pa.paInt16			#: 16 bit int
paInt8			= pa.paInt8				#: 8 bit int
paUInt8			= pa.paUInt8			#: 8 bit unsigned int
paCustomFormat 	= pa.paCustomFormat		#: a custom data format

def get_sample_size(format):
	"""
	Returns the size (in bytes) for the specified sample *format*.
	
	:param format: A |PaSampleFormat| constant.
	:raises ValueError: on invalid specified 'format'.
	:rtype: integer
	"""
	if format == paFloat32:
		return 0 # TODO: find about float 32 sample size
	elif format == paInt32:
		return 4
	elif format == paInt24:
		return 3
	elif format == paInt16:
		return 2
	elif format == paInt8:
		return 1
	elif format == paUInt8:
		return 0 # TODO: find about unsigned int 8 sample size
	elif format == paCustomFormat:
		return 0 # TODO: find about custom format sample size 
	else:
		raise ValueError("Invalid PortAudio format")

def get_format_from_width(width, unsigned=True):
    """
    Returns a PortAudio format constant for the specified *width*.

    :param width: The desired sample width in bytes (1, 2, 3, or 4)
    :param unsigned: For 1 byte width, specifies signed or unsigned format.

    :raises ValueError: when invalid *width*
    :rtype: A |PaSampleFormat| constant
    """

    if width == 1:
        if unsigned:
            return paUInt8
        else:
            return paInt8
    elif width == 2:
        return paInt16
    elif width == 3:
        return paInt24
    elif width == 4:
        return paFloat32
    else:
        raise ValueError("Invalid width: %d" % width)
		
###################################################################
# Versioning
###################################################################

def get_portaudio_version_text():
    """
    Returns PortAudio version as a text string.

    :rtype: string
    """

    return pa.Pa_GetVersionText()

class PAudio(object):
	def __init__(self, numInputChannels,
					   numOutputChannels,
					   bitPerSample,
					   sampleRate):
		"""
    	Function to initialize basic parameter for audio output device stream
		
    	:param numInputChannels: Number of input channels. Use value 0 if stream
			is not configured as input device.
			 
    	:param numOutputChannels: Number of output channels. Use value 0 if stream
			is not configured as output device.
			
		:param bitPerSample: Sample format in PaSampleFormat form.
		
		:param sampleRate: Number of samples per second.

    	:raises TODO: 
    	"""
		# initialize device
		pa.Pa_Initialize()
		# TODO: add debug() for error-checking
	
		self._stream = pa.POINTER(pa.PaStream)() # object as handler for stream returned
	
		# referencing parameter variable to class object-bounded attributes
		self._numInputChannels 	= numInputChannels
		self._numOutputChannels = numOutputChannels
		self._bitPerSample		= bitPerSample
		self._sampleRate		= sampleRate
	 
		# simple method for opening device either or both input-output stream
		pa.Pa_OpenDefaultStream(pa.byref(self._stream),
								self._numInputChannels,
								self._numOutputChannels,
								self._bitPerSample,
								self._sampleRate, 
								1024,				# the help says that this should be the same number as Pa_WriteStream() function. 
								None,
								None)
		# TODO: add error checking and more explanation. And conversion in bitpersample
	
		# start stream
		pa.Pa_StartStream(self._stream)
		# TODO: considering put it as a class method
	
	# function to read data from audio input device
	def read(probably_number_of_bytes_recorded):
		"""
		This is TODO
    	Returns a PortAudio format constant for the specified *width*.

    	:param width: The desired sample width in bytes (1, 2, 3, or 4)
    	:param unsigned: For 1 byte width, specifies signed or unsigned format.

    	:raises ValueError: when invalid *width*
    	:rtype: A |PaSampleFormat| constant
    	"""
		pass
		# TODO: Add implementation 
		
	# function to pass raw PCM data to audio ouptut stream
	def write(self, data):
		"""
    	Function to write RAW PCM data to audio output stream

    	:param data: RAW PCM data

    	:raises ValueError: TODO
    	:rtype: TODO
    	"""
		if self._numOutputChannels < 1:
			return -1 # error happens
			
		#TODO: Add mechanism to prevent write data if output is disabled
		block_align = 16 * self._numOutputChannels / 8 
		block_data = len(data) / block_align
		pa.Pa_WriteStream(self._stream, data, block_data)
		# TODO: Add error checking mehcanism or return, or debug()
		
	# destructor to cleaning up process
	def __del__(self):
		"""
    	Destructor to clean up the process like closing stream and
		terminating PortAudio.

    	"""
		pa.Pa_CloseStream(self._stream)
		# TODO: Considering put closestream as separate function
		pa.Pa_Terminate(self._stream)
		# TODO: Add error checking mechanism. Or not (?)
		
if __name__ == "__main__":
	import wave
	
	CHUNK = 1000
	wf = wave.open('input.wav', 'rb')
	
	print get_portaudio_version_text()
	stream = PAudio(0, 2, paInt16, 44100)
	
	data = wf.readframes(CHUNK)
	
	while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)
		
	stream = None
	
# Somehow it tells me that it only play 1024 or as BLOCK_DATA constants defined data length
# perhaps I should check the length of gived data and pass it to write function (?)