from tweepy import Stream, OAuthHandler, StreamListener
import sys, json, os, string, random

## TODO
## Test getNextFile with empty directory


# Add auth token
atoken = ...
asecret = ...
# Add consumer token
ckey = ...
csecret = ...
# Set working directory for out file data
wd = "/media/sf_F_DRIVE/"
r_chars = range(0x25A0,0x25F0)+range(0x2300,0x232D)

def getNextFile(path):
	"""
	Assists stream resume
	Returns filename of last file written
	"""
	f_names = os.listdir(path)

	if len(f_names) == 0:
		return 0

	f_names.sort()
	try:
		last = int(f_names.pop()[4:])
	except ValueError:
		print "Output directory is not clean.  Ensure output directory contains only files created by this program, and your padding argument matches the files in the directory."
	return last

def getWords(d):
	"""
	Extracts raw lower case words from tweets by removing punctuation
	Ex, "Oh My Gosh a #Pony!!!!" becomes "oh my gosh a pony"
	"""
	words = d['text'].encode('utf-8', 'ignore')
	words = words.translate(string.maketrans("",""), string.punctuation)
	words = words.split()
	words = ' '.join([a.lower() for a in words])
	return words

class listener(StreamListener):
	"""
	Handles twitter stream data
	"""
	def on_connect(self):
		print "Connected successfully, reading tweets..."

	def on_error(self, status_code):
		print "Error %s encountered" % str(status_code)

	def on_disconnect(self, notice):
		raise Exception("Stream disconnected with notification %s" % str(notice))

	def on_data(self, data):
		try:
			d = json.loads(data)
			# Only process original tweets
			if 'retweeted_status' not in d:
				# Write the raw json formatted tweets in batches of 10,000
				if (self.n%1000 == 0):
					self.outfile_number += 1
					print "\nStarting new file ", self.outfile_number
					self.js = open('%s/%s/json/json%s' % (wd, output_dir, string.zfill(str(self.outfile_number),pad_n)),"wb")
				self.js.write(json.dumps(d)+'\n')
				# Also parse the words and append them onto a giant file because I'm lazy
				self.txt.write(getWords(d)+'\n')
				self.n+=1
				# Prints an amusing unicode symbol to the console to make sure the thing is still running
				# Need to use Python3x style print statement so it doesn't add a bunch of spaces
				sys.stdout.write(unichr(random.choice(r_chars)))
				sys.stdout.flush()
		except:
			print "Error parsing tweet, skipped"

	def __init__(self):
		# Get the starting file number
		self.outfile_number = getNextFile(wd+output_dir+'/json/')
		self.txt = open('%s/%s/text' % (wd,output_dir),"ab")
		self.n = 0
		if self.outfile_number > 0:
			# If resuming, find the last line of the last file and pick up where we left off
			self.js = open('%s/%s/json/json%s' % (wd, output_dir, string.zfill(str(self.outfile_number),pad_n)),"rb")
			self.n = sum(1 for line in self.js)
			# Reopen the file for writing...there's probably a better way to do this
			self.js = open('%s/%s/json/json%s' % (wd, output_dir, string.zfill(str(self.outfile_number),pad_n)),"ab")
			print "resuming run on file %s from line %s /n" % (self.outfile_number, self.n)



if __name__ == '__main__':
	"""
	Run with arguments:
	pad_n :
		Number of padding digits to add to file partitions. Set 1 higher than you'll need.
		Ex, 7 -> "file0000000"
	output_dir :
		Output directory found under the working directory set at the start of this file.
	hashtags :
		Hashtags to grab tweets for. Separate with spaces.
	"""
	if len(sys.argv)<3:
		raise Exception('All arguments are mandatory, see docs')
	global output_dir 
	global pad_n
	output_dir = sys.argv[1]

	# Check output directory filetree. If not present, create it
	if not os.access(wd+output_dir, os.F_OK):
		os.mkdir(wd+output_dir)
	if not os.access(wd+output_dir+'/json/', os.F_OK):
		os.mkdir(wd+output_dir+'/json')

	pad_n = int(sys.argv[2])
	# Grab remaining arguments and parse into a list of hashtags
	hashtags = ['#%s' % a.lower() for a in sys.argv[3:]]
	print "Searching Twitter live feed for "+', '.join(['%s' % s for s in hashtags])
	while True:
		try:
			auth = OAuthHandler(ckey,csecret)
			auth.set_access_token(atoken,asecret)
			tStream = Stream(auth, listener(), stall_warnings = True)
			tStream.filter(track = hashtags)
		except KeyboardInterrupt:
			print "\nRun terminated by user request"
			sys.exit(0)
