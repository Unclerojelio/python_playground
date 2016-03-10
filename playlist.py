import re, argparse
import plistlib

def findCommonTracks(fileNames):
	# a list od sets of track names
	trackNameSets = []
	for fileName in fileNames:
		# create a new set
		trackNames = set()
		# read in a playlist
		plist = plistlib.readPlist(fileName)
		# get the tracks
		tracks = plist['Tracks']
		# iterate through the tracks
		for trackID, track in tracks.items():
			try:
				# add the track name to a set
				trackNames.add(track['Name'])
			except:
				# ignore
				pass
		# add to list
		trackNameSets.append(trackNames)
	# get the set of common tracks
	commonTracks = set.intersection(*trackNameSets)
	# write to file
	if len(commonTracks) > 0:
		f = open("common.txt", "w")
		for val in commonTracks:
			s = "%s\n" % val
			f.write(s.encode("UTF-8"))
		f.close()
		print("%d common tracks found. "
		      "Track names written to common.txt." % len(commonTracks))
	else:
		print("No common tracks!")

def findDuplicates(filename):
	print('Finding duplicate tracks in %s...' % filename)
	# read in a playlist
	plist = plistlib.readPlist(filename)
	# get the tracks from the Tracks dictionary
	tracks = plist['Tracks']
	# create a track name dictionary
	trackNames = {}
	# iterate through the tracks
	for trackId, track in tracks.items():
		try:
			name = track['Name']
			duration = track['Total Time']
			# look for existing entries
			if name in trackNames:
				# if a name and duration match, increment the count
				# round the track length to the nearest second
				if duration//1000 == trackNames[name][0]//1000:
					count = trackNames[name][1]
					trackNames[name] = (duration, count+1)
			else:
				# add dictionary entry as tuple (duration, count)
				trackNames[name] = (duration, 1)
		except:
			# ignore
			pass
	
	dups = []
	for k, v, in trackNames.items():
		if v[1] > 1:
			dups.append((v[1], k))
	# saves duplicates to a file
	if len(dups) > 0:
		print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
	else:
		print("No duplicate tracks found!")
	f = open("dups.txt", "w")
	for val in dups:
		f.write("[%d] %s\n" % (val[0], val[1]))
	f.close
	
def main():
	# create parser
	descStr = """
	This program analyzes playlist files (.xml) exported from iTunes.
	"""
	
	parser = argparse.ArgumentParser(description=descStr)
	# add a mutually exclusive group of arguments
	group = parser.add_mutually_exclusive_group()
	
	# add expected arguments
	group.add_argument('--common', nargs='*', dest='plFiles', required=False)
	group.add_argument('--stats', dest='plFile', required=False)
	group.add_argument('--dup',dest='plFileD', required=False)
	
	# parse args
	args = parser.parse_args()
	
	if args.plFiles:
		# find common tracks
		findCommonTracks(args.plFiles)
	elif args.plFile:
		# plot stats
		plotStats(args.plFile)
	elif args.plFileD:
		# find duplicate tracks
		findDuplicates(args.plFileD)
	else:
		print("These are not the tracks you are looking for.")
	#findDuplicates("Music.xml")
	
#main method
if __name__ == '__main__':
	main()	