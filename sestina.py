import twitter, random

api = twitter.Api("3Og7JZnknSSynR3aVMyAtA","rNIFraLUiU1rHOOLdiCzJbridIgtzUwv61o0S8TqJ5c", "1038282800-lgeJ24XkCRoRmV8Az2xiNLMhEtTk7xwo6hGeyUk", "tKdIL7lNgN1cuTGL53fcUzskPppfTn1iMHHvimyL34")



def HashtagSentences():
    tag = raw_input("word: ")
    lines = []
    hashtag = "#"+tag
    results = api.GetSearch(term=hashtag, count=100)
    for x in results:
        if x.text.split()[-1].lower().startswith(hashtag):
            lines.append(x.text)
    lines = list(set(lines))
    if len(lines)<7:
        print "sorry, the muses are unmoved by '{0}' try again".format(tag)
        return HashtagSentences()
    else: return random.sample(lines, 7)
    
        


def sestinafy(a,b,c,d,e,f):
	if len(a) == 1:
		return [(b[0]+", "+e[0], d[0]+", "+c[0], f[0]+", "+a[0])]
	else: return [(a.pop(0), b.pop(0), c.pop(0), d.pop(0), e.pop(0), f.pop(0))]+sestinafy(f,a,e,b,d,c)


#"sorry, the muses are unmoved by {0} ".format(tag)

print "INSPIRE ME (with six words)\n"
a = HashtagSentences()
b = HashtagSentences()
c = HashtagSentences()
d = HashtagSentences()
e = HashtagSentences()
f = HashtagSentences()

sestinaraw= sestinafy(a,b,c,d,e,f)

for x in sestinaraw:
    for y in x:
        print "<p class=\"poem\">"+y+"</p>"
    print "<p><br/><br/></p>"


#print "\n"
#for x in sestinaraw:
#    for y in x:
#        print y
#    print "\n"
