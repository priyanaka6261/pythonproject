with open("story.txt","r") as first,open("new.txt","a") as secondfile:

    for line in first:
        secondfile.write(line)




