import plistlib

def findDuplicates(filename):
	print('Finding duplicate tracks in %s...' % filename)
	#read in a playlist
	plist = plistlib.readPlist(filename)
	#get the tracks from the Tracks dictionary
	tracks = plist['Tracks']
	#create a track name dictionary
	trackNames = {}
	#iterate through the tracks
	for trackId, track in tracks.items():
		try:
			name = track['Name']
			duration = track['Total Time']
			#look for existing entries
			if name in trackNames:
				#if a name and duration match, increment the count
				#round the track length to the nearest second
				if duration//1000 == trackNames[name][0]//1000:
					count = trackNames[name][1]
					trackNames[name] = (duration, count+1)
			else:
				#add dictionary entry as tuple (duration, count)
				trackNames[name] = (duration, 1)
		except:
			#ignore
			pass
	
	dups = []
	for k, v, in trackNames.items():
		if v[1] > 1:
			dups.append((v[1], k))
	#saves duplicates to a file
	if len(dups) > 0:
		print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
	else:
		print("No duplicate tracks found!")
	f = open("dups.txt", "w")
	for val in dups:
		f.write("[%d] %s\n" % (val[0], val[1]))
	f.close
	
def main():

	findDuplicates("Music.xml")
	
#main method
if __name__ == '__main__':
	main()	