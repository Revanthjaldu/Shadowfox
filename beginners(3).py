justice_league=["Superman","Batman","Wonder Women","Flash","Aquaman","Green Lantern"]
print("Length of list",len(justice_league))
#length will be 6
justice_league.append("batgirl")
justice_league.append("Night wing")
print(justice_league) 
#append makes the list to add the batgirl & night wing 
justice_league[0]="Wonder Women"
print(justice_league)
#By making the Wonder Women to arrange at array index 0 the leader can be made.
justice_league.remove("Green Lantern")
pos=justice_league.index("Flash")
justice_league.insert(pos+1, "Green Lantern")
print(justice_league)
#this adds "Green Latern" in between Aquaman and Flasgh
justice_league=["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print(justice_league)
justice_league.sort()
print(justice_league)
#by using sort() the elements in the list will be sorted
#Bonus
#After sorting the leader will be Cyborg
