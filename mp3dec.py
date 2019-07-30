"""
MP3Dec - MP3 Decoder implementation based on libmpg123 for python
- simple
- blocking
- LGPL
- Ardi Nursyamsu (ardinursyamsu@yahoo.com)

packages:
- this file
- _libmpg123.py
- libmpg123.dll
- libgcc_s_sjlj-1.dll

version 0.1
- Decode a chunk of audio data based ono input parameter given
- Get the audio file format parameter like sample rate, bit per sample, and number of channels
- Get the information from id3 tag
- Get duration in samples from audiofile
version 0.2
- seek into sample offset
"""

# MP3Dec : Python Bindings for mpg123

# Copyright (c) 2015 Ardi Nursyamsu

# Permission is hereby granted, free of charge, to any person obtainning
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, includeing
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell of copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
	
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHERS DEALINGS IN THE SOFTWARE

"""
MP3Dec provides Python bindings for mpg123, the cross-platform MPEG-1, 2
2.5 Layer 1, 2, and 3 decoder library. With this MP3Dec, you can easily 
decode file that supported by those working group, most prominent, mp3
format file. There's a lot of feature like gapless playback and feed 
streaming.

This MP3Dec is written as supported module for Author's final project
to support's author final project feature of playig and modifying 
compressed audio file like mp3. This small-sized decoder would support
basic decoder function like decode, and seeking into desirable offset.
It also supports function of reading id3 tags and get frame informations.
"""
import _libmpg123 as lm

import sys

#######################################################################
# GLOBALS
#######################################################################
SEEK_SET = 0	# seek into the offset's setted posistion
SEEK_CUR = 1	# seek into current position plus offset given
SEEK_END = 2	# seek to the end of the file

class _audiofile(object):
	"""
	Internal class to represent audio file information
	"""
	def __init__(self, rate, channels, coding,
					   artist, title, album, genre, duration):
		"""
		Function to pool information about audio file like format, 
		channels, bit depth, artist, and so on ...
		
		:param rate: Sample rate or number of samples per second
		
		:param channels: Number of channels of the file
		
		:param coding: is nummber of bytes per sample
		
		:param artist: artist name got from id3 tag
		
		:param title: title name got from id3 tag
		
		:param album: album name got from id3 tag
		
		:param duration: duration length in number of samples
		"""
		self._rate = rate
		self._channels = channels
		self._sampwidth = coding
		
		self._artist = artist
		self._title = title
		self._album = album
		self._genre = genre
		self._totalsamples = duration
		
	def SampleRate(self):
		"""
		Function to obtain audio file sample rate
		"""
		return self._rate.value
		
	def NumOfChannels(self):
		"""
		Function to obtain number of channels of audio file
		"""
		return self._channels.value
		
	def SampleWidth(self, bit=False):
		"""
		Function to obtain number of bytes in a sample.
		
		:param bit: To change from bytes per sample to bit per sample
		"""
		if bit:
			return self._sampwidth * 8
		else:
			return self._sampwidth
			
	def Artist(self):
		"""
		Function to obtain artist name
		"""
		return self._artist
		
	def Title(self):
		"""
		Function to obtain title name
		"""
		return self._title
		
	def Album(self):
		"""
		Function to obtain album name
		"""
		return self._album
	
	def Genre(self):
		"""
		Function to obtain genre name from converted genre code
		"""
		if self._genre == 0:
			return "Blues"
		elif self._genre == 1:
			return "Classic Rock"
		elif self._genre == 2:
			return "Country"
		elif self._genre == 3:
			return "Dance"
		elif self._genre == 4:
			return "Disco"
		elif self._genre == 5:
			return "Funk"
		elif self._genre == 6:
			return "Grunge"
		elif self._genre == 7:
			return "Hip-Hop"
		elif self._genre == 8:
			return "Jazz"
		elif self._genre == 9:
			return "Metal"
		elif self._genre == 10:
			return "New Age"
		elif self._genre == 11:
			return "Oldies"
		elif self._genre == 12:
			return "Other"
		elif self._genre == 13:
			return "Pop"
		elif self._genre == 14:
			return "R&B"
		elif self._genre == 15:
			return "Rap"
		elif self._genre == 16:
			return "Reggae"
		elif self._genre == 17:
			return "Rock"
		elif self._genre == 18:
			return "Techno"
		elif self._genre == 19:
			return "Industrial"
		elif self._genre == 20:
			return "Alternative"
		elif self._genre == 21:
			return "Ska"
		elif self._genre == 22:
			return "Death Metal"
		elif self._genre == 23:
			return "Pranks"
		elif self._genre == 24:
			return "Soundtrack"
		elif self._genre == 25:
			return "Euro-Techno"
		else:
			return self._genre
	
	def Duration(self):
		"""
		function to get duration of audio data in second
		"""
		return self._totalsamples / self._rate.value
		
		
class _audiodata(object):
	"""
	internal class to represent audio data
	"""
	def __init__(self, data, fileinfo):
		"""
		Initialization of data and it's information
		
		:param data: pointer to decoded audio PCM data that got from ctypes
			module
			
		:param fileInfo: contain _audiofile class to maintain the format
			and information about the audio data
		"""
		self._data = data
		self._len = len(data)
		self.FileInfo = fileinfo
		
	def GetRaw(self):
		"""
		Function to get raw PCM data as bytes of string in python native
		data type.
		"""
		return lm.string_at(self._data, self._len)
		
	def GetData(self):
		"""
		Function to get pointer of decoded audio PCM data
		"""
		return self._data


class MP3Dec(object):
	"""
	Class to operate against MPEG-1 Layer 3 audio file (MP3).
	Like decoding, seek, get information, etc...
	"""
	def __init__(self, filename):
		"""
		Function to preparing and initializing decoder library and load
		determined mp3 compressed file into decoder and get it's basic
		information.
		
		:param filename: corresponding audio file that would be decoded
		"""
		
		# TODO: Error handling mechanism/debug
		self._file = filename
		
		if lm.mpg123_init():
			print "Library cannot be initialized..."
			sys.exit(0)
			
		err = lm.c_int()
		done = lm.c_size_t()
		self._mh = lm.mpg123_new(None, lm.byref(err))	# create decode stream handle
		
		if lm.mpg123_open(self._mh, self._file):
			print "Couldn't open %s... " % self._file
			sys.exit(0)
			
		# get audio format
		rate = lm.c_int()
		channels = lm.c_int()
		encoding = lm.c_int()
		if lm.mpg123_getformat(self._mh, lm.byref(rate), lm.byref(channels), lm.byref(encoding)):
			print "Couldn't get format..."
			sys.exit(0)
			
		bitpersample = lm.mpg123_encsize(encoding.value)
		
		# get audio data
		v1 = lm.POINTER(lm.mpg123_id3v1)()
		v2 = lm.POINTER(lm.mpg123_id3v2)()
		ret = lm.mpg123_id3(self._mh, lm.byref(v1), lm.byref(v2))
		
		# get duration of file in number of samples (divided by sample rate to get actual duration in second of audiofile)
		# TODO: Add error handling or something mechanism.
		
		ret = lm.mpg123_scan(self._mh)
		sample_len = lm.mpg123_length(self._mh)
		self._duration = sample_len
		
		try:
			artist = v1.contents.artist
			title =  v1.contents.title
			album = v1.contents.album
			genre = v1.contents.genre
			
			self.FileInfo = _audiofile(rate, channels, bitpersample,
								   artist, title, album, genre, sample_len)
		except ValueError as e:
			print e
			# TODO: create something that could handle id3v2. I'm begging yuuuuu ~
			self.FileInfo = _audiofile(rate, channels, bitpersample, "N/A", "N/A", "N/A", "N/A", sample_len)
		
		# variables containt 
		
								   
		
	def Decode(self, bytes_to_be_decoded):
		"""
		Function used to decode MPEG-1 Layer 3 compressed data into
		PCM format
		
		:param bytes_to_be_decoded: Number of bytes that will be outputted
			by the decoder.
		"""
		bytes = bytes_to_be_decoded
		buff = (lm.c_uint8 * bytes)()
		done = lm.c_size_t()
		
		if not lm.mpg123_read(self._mh, buff, bytes, lm.byref(done)):
			return _audiodata(buff, self.FileInfo)
		else:
			return None
			
	def Seek(self, seconds):
		"""
		Function to seek into determined sample offset.
		
		:param seconds: Seek to desired second of the audio file length.
		"""
		param = SEEK_SET
		duration_to = 0
		
		if self._duration <= 0: # if the length of file cannot be determined by the library
			return -1
		
		duration_to = seconds * self.FileInfo.SampleRate() # convert seconds to sample offset
		
		if duration_to >= self._duration:	# if we try to seek more than the length of the file
			duration_to = self._duration	# we try to seek at the end of the file
			param = SEEK_END
		elif duration_to <= 0:	# if we try to seek into negative or zero,
			duration_to = 0		# we try to seek at the beginning instead
			param = SEEK_SET
				
		ret = lm.mpg123_seek(self._mh, int(duration_to), param)
		print ret
		
			
if __name__ == "__main__":
	import paudio
	
	audio_out = paudio.PAudio(0, 2, paudio.paInt16, 44100)
	
	dec = MP3Dec("music2.mp3")
	duration = dec.FileInfo.Duration()
	print "The duration of file is %d min %d sec." % (duration/60, duration % 60)
	
	data = dec.Decode(1000)
	dec.Seek(20) # seek to 20 second
	
	while data is not None:
		audio_out.write(data.GetRaw())
		data = dec.Decode(1000)
	