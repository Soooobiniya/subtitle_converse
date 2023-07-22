f_in=open("./before_convert.vtt","r", encoding='UTF8')
f_out=open("./after_convert.srt","w", encoding='UTF8')
a = 1
for line in f_in:
    if line == "WEBVTT\n":
        line = ""
        f_out.write(line)
    elif line == "\n":
        line = "\n"+str(a)+"\n"
        a += 1
        f_out.write(line)
    else:
        f_out.write(line)
f_in.close()
f_out.close()